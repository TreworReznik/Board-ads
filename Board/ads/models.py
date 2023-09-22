from django.db import models
from django.contrib.auth.models import User
from froala_editor.fields import FroalaField


class Author(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.author}'


class Post(models.Model):
    TANKS = 'TA'
    DD = 'DD'
    HILY = 'HI'
    MERCHANTS = 'MER'
    GUILD_MASTERS = 'GM'
    QUEST_GIVERS = 'QG'
    BLACKSMITHS = 'BM'
    TANNERS = 'TN'
    POTION_MAKERS = 'PM'
    SPELL_MASTERS = 'SM'
    CATEGORY_TYPE = (
        (TANKS, 'Танки'),
        (DD, 'DD'),
        (HILY, 'Хилы'),
        (MERCHANTS, 'Торговцы'),
        (GUILD_MASTERS, 'Гилдмастеры'),
        (QUEST_GIVERS, 'Квестгиверы'),
        (BLACKSMITHS, 'Кузнецы'),
        (TANNERS, 'Кожевники'),
        (POTION_MAKERS, 'Зельевары'),
        (SPELL_MASTERS, 'Мастера заклинаний'),
    )
    author = models.OneToOneField(Author, on_delete=models.CASCADE)
    category_type = models.CharField(max_length=3, choices=CATEGORY_TYPE)
    title = models.CharField(max_length=128)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    picture = models.FileField(upload_to='static/img')

    def __str__(self):
        return f'{self.text}: {self.title}: {self.category_type}'


class Responses(models.Model):
    test = models.TextField()
    re_user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    re_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)


class Newsletters(models.Model):
    test = models.TextField()
    picture = FroalaField(blank=True, null=True, image_upload='static/img')