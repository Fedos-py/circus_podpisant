from discovery.catalogs import EXTRA_WEBSITES, build_vk_catalog
from discovery.rosgoscirk import scrape_filials
from discovery.upsert import upsert_sources
from discovery.vk_api import search_groups
from models import Source, db


def _count_by_status():
    rows = (
        db.session.query(Source.verification_status, db.func.count(Source.id))
        .group_by(Source.verification_status)
        .all()
    )
    return {status or "unknown": count for status, count in rows}


def run_discovery(skip_scrape=False, skip_vk_api=False):
    report = {
        "rosgoscirk_scrape": 0,
        "catalog_websites": 0,
        "catalog_vk": 0,
        "vk_api": 0,
        "warnings": [],
    }

    if not skip_scrape:
        try:
            sites = scrape_filials()
            report["rosgoscirk_scrape"] = upsert_sources(
                sites, Source.WEBSITE, "rosgoscirk_scrape", default_status="verified"
            )
        except Exception as exc:
            report["warnings"].append(f"Парсер circus.ru: {exc}")

    report["catalog_websites"] = upsert_sources(
        EXTRA_WEBSITES, Source.WEBSITE, "catalog", default_status="verified"
    )
    report["catalog_vk"] = upsert_sources(
        build_vk_catalog(), Source.VK, "catalog", default_status="candidate"
    )

    if not skip_vk_api:
        groups, warning = search_groups()
        if warning:
            report["warnings"].append(warning)
        if groups:
            report["vk_api"] = upsert_sources(
                groups, Source.VK, "vk_api", default_status="candidate"
            )

    total = Source.query.count()
    websites = Source.query.filter_by(source_type=Source.WEBSITE).count()
    vk = Source.query.filter_by(source_type=Source.VK).count()
    report["total"] = total
    report["websites"] = websites
    report["vk"] = vk
    report["by_status"] = _count_by_status()
    report["added"] = (
        report["rosgoscirk_scrape"]
        + report["catalog_websites"]
        + report["catalog_vk"]
        + report["vk_api"]
    )
    return report
