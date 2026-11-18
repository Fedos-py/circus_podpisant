"""CLI: автодобор источников в базу."""

import argparse

from app import app
from discovery import run_discovery
from models import Source, db, ensure_schema
from seed_data import seed_database


def main():
    parser = argparse.ArgumentParser(description="Сбор источников для «Подписант»")
    parser.add_argument(
        "--skip-scrape",
        action="store_true",
        help="Не парсить circus.ru/kontakty/filialy",
    )
    parser.add_argument(
        "--skip-vk-api",
        action="store_true",
        help="Не вызывать VK groups.search (нужен VK_SERVICE_TOKEN)",
    )
    parser.add_argument(
        "--seed-only",
        action="store_true",
        help="Только ручной seed, без discovery",
    )
    args = parser.parse_args()

    with app.app_context():
        db.create_all()
        ensure_schema()
        seed_added = seed_database()
        print(f"Seed: добавлено {seed_added} записей")

        if args.seed_only:
            _print_totals()
            return

        report = run_discovery(
            skip_scrape=args.skip_scrape,
            skip_vk_api=args.skip_vk_api,
        )

        print("\n=== Discovery ===")
        print(f"Парсер Росгосцирка: +{report['rosgoscirk_scrape']}")
        print(f"Каталог сайтов:      +{report['catalog_websites']}")
        print(f"Каталог VK:          +{report['catalog_vk']}")
        print(f"VK API:              +{report['vk_api']}")
        print(f"Всего добавлено:     +{report['added']}")
        print(
            f"\nИтого в базе: {report['total']} "
            f"(сайты: {report['websites']}, VK: {report['vk']})"
        )
        if report["by_status"]:
            print("По статусу верификации:")
            for status, count in sorted(report["by_status"].items()):
                print(f"  {status}: {count}")
        for warning in report["warnings"]:
            print("WARN:", warning)


def _print_totals():
    total = Source.query.count()
    websites = Source.query.filter_by(source_type=Source.WEBSITE).count()
    vk = Source.query.filter_by(source_type=Source.VK).count()
    print(f"Всего в базе: {total} (сайты: {websites}, VK: {vk})")


if __name__ == "__main__":
    main()
