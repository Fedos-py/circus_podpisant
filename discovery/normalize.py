import re


def normalize_url(url):
    normalized = (url or "").strip().rstrip("/")
    if normalized.startswith("http://"):
        normalized = "https://" + normalized[7:]
    return normalized


def vk_url_from_id(group_id, screen_name=None):
    if screen_name:
        return normalize_url(f"https://vk.com/{screen_name}")
    gid = abs(int(group_id))
    return normalize_url(f"https://vk.com/club{gid}")


def is_circus_related(text):
    if not text:
        return False
    lowered = text.lower()
    keywords = (
        "цирк",
        "шапито",
        "cirque",
        "circus",
        "cirk",
        "манеж",
        "гастрол",
        "купол",
    )
    return any(word in lowered for word in keywords)


def clean_name(text):
    return re.sub(r"\s+", " ", (text or "").strip())
