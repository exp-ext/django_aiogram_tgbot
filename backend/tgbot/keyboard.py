from aiogram import types

from .loader import bot


async def send_keyboard(chat_id: int):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(
        types.InlineKeyboardButton(
            text='Нажми меня', callback_data='button_pressed'
        )
    )
    await bot.send_message(chat_id, 'Привет, мир!', reply_markup=keyboard)
