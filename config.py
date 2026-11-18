import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


def _load_dotenv():
    """Простая загрузка .env без лишних зависимостей."""
    path = os.path.join(BASE_DIR, ".env")
    if not os.path.isfile(path):
        return
    with open(path, encoding="utf-8") as handle:
        for raw in handle:
            line = raw.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            key = key.strip()
            value = value.strip().strip("'").strip('"')
            os.environ.setdefault(key, value)


_load_dotenv()


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-circus-podpisant-key")
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL", f"sqlite:///{os.path.join(BASE_DIR, 'circus.db')}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
