from django.conf import settings
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path(
        f'{settings.TELEGRAM_TOKEN}/webhooks/',
        csrf_exempt(views.TelegramBotWebhookView.as_view())
    ),
]
