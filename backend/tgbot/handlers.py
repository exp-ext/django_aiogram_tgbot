from aiogram import Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import Text
from users.views import get_or_create_user

from .command import set_commands
from .keyboard import send_keyboard
from .loader import bot

dp = Dispatcher(bot, storage=MemoryStorage())

# ~~~handler`s~~~ #


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    user = await get_or_create_user(message)
    await message.reply("Привет, {}. Я бот!".format(user.first_name))
    await set_commands(bot)
    await send_keyboard(message.chat.id)


@dp.message_handler(state=None)
async def echo(message: types.Message):
    print('ok')
    await message.answer(message.text)


# ~~~callback`s~~~ #


@dp.callback_query_handler(Text('button_pressed'))
async def send_random_value(callback: types.CallbackQuery):
    await callback.message.answer(
        text='Пишем в чате.'
    )
    await callback.answer(
        text='И в окне.',
        show_alert=True
    )
