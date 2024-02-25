# Generated by Django 5.0 on 2024-01-04 15:33

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='order',
            name='order',
        ),
        migrations.AddField(
            model_name='order',
            name='order',
            field=models.ManyToManyField(to='store.orderitem'),
        ),
    ]