# Generated by Django 4.2.5 on 2023-09-22 15:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0002_alter_post_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ads.author'),
        ),
        migrations.AlterField(
            model_name='post',
            name='picture',
            field=models.FileField(default=1, upload_to='static/img'),
            preserve_default=False,
        ),
    ]