# Generated by Django 4.1.3 on 2022-11-23 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0011_subscriber_mailing_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mailing',
            options={'ordering': ['-created_at'], 'verbose_name': 'Рассылка', 'verbose_name_plural': 'Рассылки'},
        ),
        migrations.AddField(
            model_name='subscriber',
            name='mailing',
            field=models.BooleanField(default=False),
        ),
    ]
