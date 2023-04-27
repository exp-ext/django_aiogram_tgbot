from asgiref.sync import async_to_sync
from django.conf import settings
from django.core.management.base import BaseCommand

from ...loader import bot, check_tokens

DOMAIN_URL = settings.DOMAIN_NAME
TELEGRAM_TOKEN = settings.TELEGRAM_TOKEN
WEBHOOK_URL = f'https://{DOMAIN_URL}/bot/{TELEGRAM_TOKEN}/webhooks/'


class Command(BaseCommand):
    help = 'Setting webhook'

    def handle(self, *args, **options):
        if not check_tokens:
            return self.stdout.write(
                self.style.WARNING('No environmental variables!')
            )

        webhook = async_to_sync(bot.get_webhook_info)()
        if webhook.url != WEBHOOK_URL:
            async_to_sync(bot.set_webhook)(
                WEBHOOK_URL, drop_pending_updates=True
            )
            return self.stdout.write(
                self.style.SUCCESS('Webhook was successfully set!')
            )
        return self.stdout.write(self.style.WARNING('Webhook already set!'))
