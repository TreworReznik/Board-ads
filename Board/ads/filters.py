from django_filters import FilterSet
from .models import Author
from django.forms import Select, DateInput, TextInput
import django_filters


class PostFilter(FilterSet):
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
    author = django_filters.ModelChoiceFilter(
        label='Author',
        queryset=Author.objects.all(),
        widget=Select(attrs={'class': 'form-select'}),
        )

    category = django_filters.ChoiceFilter(
        choices=CATEGORY_TYPE,
        field_name='category_type',
        label='Category',
        widget=Select(attrs={'class': 'form-select'}),
    )

    date_of_creation = django_filters.DateTimeFilter(
        field_name='created',
        lookup_expr='gt',
        label='Date',
        localize=True,
        widget=DateInput(format='%Y-%m-%d', attrs={'class': 'form-control', 'type': 'date'}),
    )
    title = django_filters.CharFilter(
        field_name='title',
        label='Title',
        widget=TextInput(attrs={'class': 'form-control'})
    )
