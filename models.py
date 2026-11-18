from datetime import datetime, timezone

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import inspect, text

db = SQLAlchemy()


class Source(db.Model):
    __tablename__ = "sources"

    WEBSITE = "website"
    VK = "vk"

    STATUS_VERIFIED = "verified"
    STATUS_CANDIDATE = "candidate"
    STATUS_DEAD = "dead"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    source_type = db.Column(db.String(20), nullable=False, index=True)
    url = db.Column(db.String(500), nullable=False, unique=True)
    city = db.Column(db.String(120))
    region = db.Column(db.String(120))
    organization = db.Column(db.String(120))
    description = db.Column(db.Text)
    verification_status = db.Column(
        db.String(20), default=STATUS_CANDIDATE, nullable=False, index=True
    )
    discovery_method = db.Column(db.String(40), default="manual", nullable=False)
    is_active = db.Column(db.Boolean, default=True, nullable=False)
    created_at = db.Column(
        db.DateTime, default=lambda: datetime.now(timezone.utc), nullable=False
    )

    def __repr__(self):
        return f"<Source {self.name} ({self.source_type})>"

    @property
    def type_label(self):
        return "Сайт" if self.source_type == self.WEBSITE else "ВКонтакте"

    @property
    def display_url(self):
        return self.url.replace("https://", "").replace("http://", "").rstrip("/")

    @property
    def status_label(self):
        labels = {
            self.STATUS_VERIFIED: "Проверен",
            self.STATUS_CANDIDATE: "Кандидат",
            self.STATUS_DEAD: "Неактивен",
        }
        return labels.get(self.verification_status, self.verification_status)


def ensure_schema():
    """Добавляет новые колонки в существующую SQLite-базу."""
    inspector = inspect(db.engine)
    if "sources" not in inspector.get_table_names():
        return

    columns = {col["name"] for col in inspector.get_columns("sources")}
    statements = []
    if "verification_status" not in columns:
        statements.append(
            "ALTER TABLE sources ADD COLUMN verification_status "
            "VARCHAR(20) NOT NULL DEFAULT 'candidate'"
        )
    if "discovery_method" not in columns:
        statements.append(
            "ALTER TABLE sources ADD COLUMN discovery_method "
            "VARCHAR(40) NOT NULL DEFAULT 'manual'"
        )

    if not statements:
        return

    with db.engine.begin() as connection:
        for statement in statements:
            connection.execute(text(statement))
        connection.execute(
            text(
                "UPDATE sources SET verification_status = 'verified' "
                "WHERE verification_status = 'candidate' "
                "AND (discovery_method = 'manual' OR discovery_method IS NULL)"
            )
        )
