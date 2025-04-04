# Generated by Django 4.2.7 on 2025-03-24 10:11

import django.contrib.auth.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebSite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='rule',
            field=models.CharField(choices=[('user', 'USER'), ('owner', 'OWNER')], default='student', max_length=16),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username'),
        ),
    ]
