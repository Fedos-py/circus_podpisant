"""Точка входа для gunicorn / waitress на тестовом контуре."""

from app import app, init_db

init_db()
