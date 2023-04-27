import unittest

from aiogram_unittest import Requester
from aiogram_unittest.handler import MessageHandler
from aiogram_unittest.types.dataset import MESSAGE

from ..loader import echo


class TestHandlers(unittest.IsolatedAsyncioTestCase):

    async def test_echo(self):
        request = Requester(request_handler=MessageHandler(echo))
        calls = await request.query(
            message=MESSAGE.as_object(text="Hello, Bot!")
        )
        answer_message = calls.send_message.fetchone().text
        self.assertEqual(answer_message, 'Hello, Bot!')
