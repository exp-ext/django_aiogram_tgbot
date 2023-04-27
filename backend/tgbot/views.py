import asyncio
import json
from typing import Any, Dict

from aiogram import Bot, Dispatcher, types
from asgiref.sync import async_to_sync
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.utils.decorators import classonlymethod
from django.views import View

from .loader import bot, dp


class TelegramBotWebhookView(View):
    """Получение запроса от Телеграмм."""
    @classonlymethod
    def as_view(self, **initkwargs):
        view = super().as_view(**initkwargs)
        view._is_coroutine = asyncio.coroutines._is_coroutine
        return view

    async def post(self,
                   request: HttpRequest, *args, **kwargs) -> Dict[str, Any]:
        Dispatcher.set_current(dp)
        Bot.set_current(bot)
        update = types.Update(**(json.loads(request.body)))
        await dp.process_update(update)
        return HttpResponse(content=b"Ok", status=200)

    async def get(self,
                  request: HttpRequest, *args, **kwargs) -> Dict[str, Any]:
        await asyncio.sleep(1)
        return JsonResponse({"ok": "Get request received! But nothing done"})
