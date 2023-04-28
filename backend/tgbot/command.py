from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_commands(bot: Bot):
    commands = [
        BotCommand(command="/help", description="Get info about me"),
        BotCommand(command="/qna", description="set bot for a QnA task"),
        BotCommand(command="/chat", description="set bot for free chat")
    ]
    await bot.delete_my_commands(BotCommandScopeDefault())
    await bot.set_my_commands(commands, BotCommandScopeDefault())
