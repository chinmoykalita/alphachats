# Generated by Django 3.2 on 2021-04-30 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AlphaChats', '0005_chat_ip_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='person',
            field=models.CharField(default='anonymous', max_length=30),
        ),
        migrations.AddField(
            model_name='room',
            name='ip_address',
            field=models.GenericIPAddressField(default=''),
        ),
        migrations.AddField(
            model_name='room',
            name='room_link',
            field=models.URLField(default=''),
            preserve_default=False,
        ),
    ]
