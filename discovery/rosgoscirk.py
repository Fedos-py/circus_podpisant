import re
import urllib.parse
import urllib.request

from discovery.normalize import clean_name, normalize_url

LETTERS = "абвгдежзиклмнопрстуфхцчшщэюя"
URL_RE = re.compile(r"https?://(?:www\.)?circus[^\s<\"']+", re.I)
NAME_RE = re.compile(
    r"<(?:h\d|p|div)[^>]*>\s*([^<]*(?:цирк|шапито|Цирк|Шапито)[^<]{0,120})",
    re.I,
)


def _fetch_letter(letter):
    query = urllib.parse.quote(letter)
    url = f"https://www.circus.ru/kontakty/filialy/?qa={query}"
    request = urllib.request.Request(
        url, headers={"User-Agent": "CircusPodpisant/1.0 (+discovery)"}
    )
    with urllib.request.urlopen(request, timeout=20) as response:
        return response.read().decode("utf-8", errors="ignore")


def scrape_filials():
    """Парсит каталог филиалов Росгосцирка."""
    websites = []
    seen_urls = set()

    for letter in LETTERS:
        try:
            html = _fetch_letter(letter)
        except Exception:
            continue

        plain = re.sub(r"<[^>]+>", "\n", html)
        blocks = [b.strip() for b in plain.split("\n") if b.strip()]

        for index, block in enumerate(blocks):
            for match in URL_RE.finditer(block):
                site_url = normalize_url(match.group(0).rstrip(".,)"))
                if "circus.ru/kontakty" in site_url:
                    continue
                if site_url.lower() in seen_urls:
                    continue

                name = None
                for prev in reversed(blocks[max(0, index - 3) : index + 1]):
                    if "цирк" in prev.lower() or "шапито" in prev.lower():
                        if "http" not in prev and len(prev) < 160:
                            name = clean_name(prev)
                            break

                if not name:
                    name = site_url.replace("https://www.", "").replace("https://", "")

                seen_urls.add(site_url.lower())
                websites.append(
                    {
                        "name": name,
                        "url": site_url,
                        "organization": "Росгосцирк",
                        "verification_status": "verified",
                        "description": "С каталога филиалов circus.ru",
                    }
                )

    return websites
