# Generated by Django 4.2.5 on 2023-09-22 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0004_responses_status_alter_responses_test'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category_type',
            field=models.CharField(choices=[('TANKS', 'Танки'), ('DD', 'DD'), ('HILY', 'Хилы'), ('MERCHANTS', 'Торговцы'), ('GUILD_MASTERS', 'Гилдмастеры'), ('QUEST_GIVERS', 'Квестгиверы'), ('BLACKSMITHS', 'Кузнецы'), ('TANNERS', 'Кожевники'), ('POTION_MAKERS', 'Зельевары'), ('SPELL_MASTERS', 'Мастера заклинаний')], default='TANKS', max_length=24),
        ),
    ]
