import json
import os
import time
import urllib.parse
import urllib.request

from discovery.normalize import is_circus_related, vk_url_from_id

API_VERSION = "5.131"
SEARCH_QUERIES = [
    "цирк шапито",
    "цирк гастроли",
    "гастрольный цирк",
    "цирк на сцене",
    "государственный цирк",
    "цирк тигры",
    "цирк львы",
    "цирк медведи",
    "цирк официальный",
    "circus show",
    "circus russia",
    "шапито билеты",
    "цирк купол",
    "цирк афиша",
    "цирк дрессировка",
    "цирк детский",
    "цирк семейный",
    "цирк воды",
    "цирк на льду",
    "зооцирк",
    "cirque",
    "цирк звезда",
    "цирк гранд",
    "цирк премьер",
    "цирк сказка",
    "цирк магия",
    "цирк экстрим",
    "цирк династия",
    "цирк королевский",
    "цирк никулин",
]


def _api_call(method, params, token):
    params = dict(params)
    params["access_token"] = token
    params["v"] = API_VERSION
    query = urllib.parse.urlencode(params)
    url = f"https://api.vk.com/method/{method}?{query}"
    request = urllib.request.Request(
        url, headers={"User-Agent": "CircusPodpisant/1.0"}
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        payload = json.loads(response.read().decode("utf-8"))
    if "error" in payload:
        raise RuntimeError(payload["error"].get("error_msg", str(payload["error"])))
    return payload.get("response", {})


def search_groups(token=None):
    token = token or os.environ.get("VK_SERVICE_TOKEN") or os.environ.get("VK_ACCESS_TOKEN")
    if not token:
        return [], "VK_SERVICE_TOKEN не задан — пропуск API-поиска"

    found = {}
    for query in SEARCH_QUERIES:
        offset = 0
        while offset < 1000:
            try:
                response = _api_call(
                    "groups.search",
                    {
                        "q": query,
                        "type": "page",
                        "count": 200,
                        "offset": offset,
                    },
                    token,
                )
            except RuntimeError:
                break

            items = response.get("items", [])
            if not items:
                break

            for group in items:
                name = group.get("name", "")
                if not is_circus_related(name):
                    continue
                gid = group.get("id")
                screen_name = group.get("screen_name")
                url = vk_url_from_id(gid, screen_name)
                found[url.lower()] = {
                    "name": name,
                    "url": url,
                    "organization": "Шапито",
                    "verification_status": "candidate",
                    "description": f"VK API groups.search: «{query}»",
                }

            if len(items) < 200:
                break
            offset += 200
            time.sleep(0.35)

    return list(found.values()), None
