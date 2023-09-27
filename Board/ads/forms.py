from django.forms import ModelForm, Select, ChoiceField, CharField, TextInput, Textarea, FileField, EmailField
from .models import Post, Responses


class CreateForm(ModelForm):
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
    category_type = ChoiceField(
        choices=CATEGORY_TYPE,
        label='Category_type',
        widget=Select(
        attrs={'class': 'form-control'}
        )
    )
    title = CharField(
        label='Title',
        min_length=3,
        max_length=128,
        widget=TextInput(
        attrs={'class': 'form-control'})
    )

    text = CharField(
        label='Text',
        min_length=20,
        widget=Textarea(
            attrs={'class': 'form-control'})
    )
    file = FileField(
        label='File',
    )

    class Meta:
        model = Post
        fields = ['category_type', 'title', 'text', 'file']


class FormResponses(ModelForm):
    text = CharField(
        label='Text',
        min_length=20,
        widget=Textarea(
            attrs={'class': 'form-control'})
    )

    class Meta:
        model = Responses
        fields = ['text']
