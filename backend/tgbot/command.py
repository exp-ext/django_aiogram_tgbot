from typing import Mapping

from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault

COMMANDS: Mapping[str, Mapping[str, str]] = {
    'en': {
        'main_menu': '📲 Main menu of bot',
        'ask_registration': '📍 Register',
        'help': '❔Help',
    },
    'ru': {
        'main_menu': '📲 Основное меню бота',
        'ask_registration': '📍Пройти регистрацию',
        'help': '❔Помощь',
    }
}


async def set_commands(bot_instance: Bot):
    """Переназначение команд меню."""

    await bot_instance.delete_my_commands(BotCommandScopeDefault())

    for lc in COMMANDS:
        await bot_instance.set_my_commands(
            language_code=lc,
            commands=[
                BotCommand(key, item) for key, item in COMMANDS[lc].items()
            ]
        )
