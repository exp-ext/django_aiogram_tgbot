import logging

from aiogram import Bot, types
from django.conf import settings

TELEGRAM_TOKEN = settings.TELEGRAM_TOKEN
logging.basicConfig(level=logging.INFO)


def check_tokens():
    """Проверка доступности переменных среды.."""
    env_vars = {
        'TELEGRAM_TOKEN': TELEGRAM_TOKEN,
        'DOMAIN_NAME': settings.DOMAIN_NAME,
    }
    for key, value in env_vars.items():
        if not value or value == '':
            raise SystemExit(f'Нет значения для: {key}')
    return True


if check_tokens():
    bot = Bot(token=TELEGRAM_TOKEN, parse_mode=types.ParseMode.HTML)
