from telegram_users.models import TelegramUser


def create_user(user_id, user_name):
    TelegramUser.objects.get_or_create(name=user_name, telegram_id=user_id)



def subscribe(user_id):
    tg_user = TelegramUser.objects.get(telegram_id=user_id)
    if tg_user.subscription:
        return True
    tg_user.subscription = True
    tg_user.save(update_fields=["subscription"])
    return False


def unsubscribe(user_id):
    tg_user = TelegramUser.objects.get(telegram_id=user_id)
    if not tg_user.subscription:
        return True
    tg_user.subscription = False
    tg_user.save(update_fields=["subscription"])
    return False


def get_request_number(user_id):
    user = TelegramUser.objects.get(telegram_id=user_id)
    return user.request_number

def add_requests_number(user_id):
    user = TelegramUser.objects.get(telegram_id=user_id)
    user.request_number += 1
    user.save()


def is_subscribe(user_id):
    return TelegramUser.objects.get(telegram_id=user_id).subscription
