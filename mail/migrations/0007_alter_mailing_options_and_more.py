# Generated by Django 4.1.3 on 2022-11-18 20:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0006_mailing_subscribermailingrelation_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mailing',
            options={'verbose_name': 'Рассылка', 'verbose_name_plural': 'Рассылки'},
        ),
        migrations.AlterModelOptions(
            name='subscribermailingrelation',
            options={},
        ),
    ]