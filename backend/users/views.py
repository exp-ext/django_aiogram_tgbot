from asgiref.sync import sync_to_async
from django.contrib.auth import get_user_model

User = get_user_model()


@sync_to_async
def get_or_create_user(message):
    user, _ = User.objects.get_or_create(
        id=message.chat.id,
        defaults={
            'first_name': message.chat.first_name,
            'last_name': message.chat.last_name,
            'username': message.chat.username,
        }
    )
    return user
