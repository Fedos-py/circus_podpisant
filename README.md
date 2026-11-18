# Подписант

MVP-сервис мониторинга источников цирковых гастролей: сайты и группы ВКонтакте.

## Что умеет MVP

- Главная со счётчиками источников
- Страница `/sources` со списком сайтов и VK, фильтрами по статусу и организации
- Seed ручного каталога + `discover.py` для автодобора
- SQLite-база (`circus.db`), статусы `verified` / `candidate` / `dead`

## Требования

- Python **3.7–3.12** (рекомендуем **3.11** на сервере)
- Зависимости из `requirements.txt`

> На Python 3.13 пакеты текущего pin (`Flask<3`, `SQLAlchemy<2`) могут собираться из исходников и падать. Для тестового контура ставьте 3.11.

## Быстрый старт (локально)

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux:
source .venv/bin/activate

pip install -r requirements.txt
cp .env.example .env
python seed_data.py
python discover.py --skip-vk-api
FLASK_DEBUG=1 python app.py
```

Откройте http://127.0.0.1:5002

## Выкладка на тестовый сервер

1. Создайте репозиторий на GitHub и запушьте код (без `.env` и `*.db`).
2. На сервере:

```bash
git clone <URL> podpisant
cd podpisant
python3.11 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# отредактируйте SECRET_KEY, HOST, PORT
```

База `circus.db` **не хранится в репозитории**. На сервер её переносят отдельно (scp/rsync), затем:

```bash
gunicorn -w 2 -b 0.0.0.0:5002 wsgi:app
```

Опционально: systemd-unit или reverse-proxy (nginx) на этот порт.

> Не коммитьте и не публикуйте `circus.db` — это рабочий каталог источников для тестового/боевого контура.

## Полезные команды

```bash
python discover.py                 # полный автодобор
python discover.py --skip-vk-api   # без VK API
python discover.py --seed-only     # только ручной каталог
```

Для VK API задайте `VK_SERVICE_TOKEN` в окружении / `.env`.

## Структура

```
app.py                 # Flask-приложение
wsgi.py                # gunicorn entrypoint
config.py              # конфиг + загрузка .env
models.py              # Source
seed_data.py           # базовый каталог
seed_catalog_extra.py  # доп. шапито / сцена
discover.py            # CLI автодобора
discovery/             # парсер circus.ru, каталоги, VK API
templates/ static/     # UI
```
