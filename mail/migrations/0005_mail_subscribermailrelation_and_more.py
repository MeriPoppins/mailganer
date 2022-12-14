# Generated by Django 4.1.3 on 2022-11-18 10:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0004_mailing_subscribermailingrelation_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField(blank=True, verbose_name='Контент')),
            ],
            options={
                'verbose_name': 'Письмо',
                'verbose_name_plural': 'Письма',
            },
        ),
        migrations.CreateModel(
            name='SubscriberMailRelation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_sent', models.BooleanField(default=False)),
                ('is_read', models.BooleanField(default=False)),
                ('mail', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='mail.mail')),
                ('subscriber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mail.subscriber')),
            ],
            options={
                'verbose_name': 'Рассылка',
                'verbose_name_plural': 'Рассылки',
            },
        ),
        migrations.RemoveField(
            model_name='subscribermailingrelation',
            name='mailing',
        ),
        migrations.RemoveField(
            model_name='subscribermailingrelation',
            name='subscriber',
        ),
        migrations.DeleteModel(
            name='Mailing',
        ),
        migrations.DeleteModel(
            name='SubscriberMailingRelation',
        ),
        migrations.AddField(
            model_name='mail',
            name='subscribers',
            field=models.ManyToManyField(related_name='subscribers', through='mail.SubscriberMailRelation', to='mail.subscriber'),
        ),
    ]
