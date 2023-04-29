import unittest

from aiogram_unittest import Requester
from aiogram_unittest.handler import MessageHandler
from aiogram_unittest.types.dataset import MESSAGE

from ..handlers import echo


class TestHandlers(unittest.IsolatedAsyncioTestCase):
    """
    https://github.com/OCCCAS/aiogram_unittest/blob/master/examples/example_tests.py
    """

    async def test_echo(self):
        request = Requester(request_handler=MessageHandler(echo))
        calls = await request.query(
            message=MESSAGE.as_object(text='Hello, Bot!')
        )
        answer_message = calls.send_message.fetchone().text
        self.assertEqual(answer_message, 'Hello, Bot!')
