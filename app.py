import os

from flask import Flask, render_template

from config import Config
from models import Source, db, ensure_schema
from seed_data import seed_database

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)


@app.route("/")
def index():
    website_count = Source.query.filter_by(
        source_type=Source.WEBSITE, is_active=True
    ).count()
    vk_count = Source.query.filter_by(source_type=Source.VK, is_active=True).count()
    return render_template(
        "index.html",
        website_count=website_count,
        vk_count=vk_count,
        total_count=website_count + vk_count,
    )


@app.route("/sources")
def sources():
    from flask import request

    status_filter = request.args.get("status", "")
    org_filter = request.args.get("org", "")

    def _query(source_type):
        query = Source.query.filter_by(source_type=source_type, is_active=True)
        if status_filter:
            query = query.filter_by(verification_status=status_filter)
        if org_filter:
            query = query.filter_by(organization=org_filter)
        return query.order_by(Source.city, Source.name).all()

    websites = _query(Source.WEBSITE)
    vk_groups = _query(Source.VK)

    organizations = [
        row[0]
        for row in db.session.query(Source.organization)
        .filter(Source.organization.isnot(None))
        .distinct()
        .order_by(Source.organization)
        .all()
    ]
    status_counts = {
        row[0]: row[1]
        for row in db.session.query(
            Source.verification_status, db.func.count(Source.id)
        )
        .filter_by(is_active=True)
        .group_by(Source.verification_status)
        .all()
    }

    return render_template(
        "sources.html",
        websites=websites,
        vk_groups=vk_groups,
        website_count=len(websites),
        vk_count=len(vk_groups),
        organizations=organizations,
        status_filter=status_filter,
        org_filter=org_filter,
        status_counts=status_counts,
    )


def init_db():
    with app.app_context():
        db.create_all()
        ensure_schema()
        seed_database()


if __name__ == "__main__":
    init_db()
    debug = os.environ.get("FLASK_DEBUG", "0") == "1"
    host = os.environ.get("HOST", "127.0.0.1")
    port = int(os.environ.get("PORT", "5002"))
    app.run(debug=debug, host=host, port=port)
