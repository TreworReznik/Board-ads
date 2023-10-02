from django.db import models
from django.contrib.auth.models import User
from froala_editor.fields import FroalaField
from django.urls import reverse


class Author(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.author}'


class Post(models.Model):
    CATEGORY_TYPE = (
        ('TANKS', 'Танки'),
        ('DD', 'DD'),
        ('HILY', 'Хилы'),
        ('MERCHANTS', 'Торговцы'),
        ('GUILD_MASTERS', 'Гилдмастеры'),
        ('QUEST_GIVERS', 'Квестгиверы'),
        ('BLACKSMITHS', 'Кузнецы'),
        ('TANNERS', 'Кожевники'),
        ('POTION_MAKERS', 'Зельевары'),
        ('SPELL_MASTERS', 'Мастера заклинаний'),
    )
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category_type = models.CharField(max_length=24, choices=CATEGORY_TYPE, default='TANKS')
    title = models.CharField(max_length=128)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to='static/img')

    def __str__(self):
        return f'{self.text}: {self.title}: {self.category_type}'

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])


class Responses(models.Model):
    text = models.TextField()
    re_user = models.ForeignKey(User, related_name='responses', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    re_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.text}: {self.re_user}'

    def get_absolute_url(self):
        return reverse('responses_detail', args=[str(self.id)])


class Newsletters(models.Model):
    test = models.TextField()
    picture = FroalaField(blank=True, null=True, image_upload='static/img')
