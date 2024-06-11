from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.contrib import messages

@receiver(user_logged_in)
def welcome_message(sender, user, request, **kwargs):
    messages.add_message(request, messages.INFO, 'Здравствуйте, {}! Добро пожаловать на сайт.'.format(user.username))