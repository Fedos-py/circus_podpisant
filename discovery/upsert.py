from discovery.normalize import normalize_url
from models import Source, db


def upsert_sources(items, source_type, discovery_method, default_status="candidate"):
    existing_urls = {
        normalize_url(source.url).lower() for source in Source.query.all()
    }
    added = 0

    for item in items:
        url = normalize_url(item["url"])
        key = url.lower()
        if not url or key in existing_urls:
            continue

        db.session.add(
            Source(
                name=item["name"],
                source_type=source_type,
                url=url,
                city=item.get("city"),
                region=item.get("region"),
                organization=item.get("organization"),
                description=item.get("description"),
                verification_status=item.get(
                    "verification_status", default_status
                ),
                discovery_method=discovery_method,
            )
        )
        existing_urls.add(key)
        added += 1

    db.session.commit()
    return added
