from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import Responses
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives


@receiver(post_save, sender=Responses)
def responses_created(instance, created, **kwargs):
    if not created:
        return

    email = User.objects.filter(
        author__author=instance.re_post.author.author).values('email')
    subject = f'{instance.re_post}'

    text_context = (
        f'На ваш пост "{instance.re_post.title}" откликнулись\n'
        f'Ссылка на отклик  http://127.0.0.1:8000{instance.get_absolute_url()}'
    )

    msg = EmailMultiAlternatives(subject, text_context, None, email)
    msg.send()


@receiver(pre_save, sender=Responses)
def changing_boolean(instance, **kwargs):
    if instance.status:
        email = User.objects.filter(responses=instance).values('email')

        text_context = (
            f'Пользователь {instance.re_post.author} принял ваш отклик \n'
            f'Ссылка на отклик  http://127.0.0.1:8000{instance.get_absolute_url()}'
        )

        msg = EmailMultiAlternatives(None, text_context, None, email)
        msg.send()
