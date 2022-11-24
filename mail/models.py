from django.db import models


class Gender(models.TextChoices):
    MALE = 'MALE', 'мужской'
    FEMALE = 'FEMALE', 'женский'


class Subscriber(models.Model):
    firstname = models.CharField(max_length=150, verbose_name='Имя')
    lastname = models.CharField(max_length=150, verbose_name='Фамилия')
    birthday = models.DateField(verbose_name='День рождения')
    gender = models.CharField(max_length=50, choices=Gender.choices, default=Gender.MALE, verbose_name='Пол')
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    mailing_id = models.ForeignKey('Mailing', on_delete=models.SET_NULL, blank=True, null=True, related_name='mailing')
    is_mailing = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.firstname} {self.lastname}'

    class Meta:
        verbose_name = 'Подписчик'
        verbose_name_plural = 'Подписчики'
        ordering = ['lastname']


class Mailing(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, verbose_name='Контент')
    subscribers = models.ManyToManyField(Subscriber, through='SubscriberMailingRelation', related_name='subscribers')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'
        ordering = ['-created_at']


class SubscriberMailingRelation(models.Model):
    subscriber = models.ForeignKey(Subscriber, on_delete=models.CASCADE)
    mail = models.ForeignKey(Mailing, on_delete=models.CASCADE, blank=True)
    sent_at = models.DateTimeField(blank=True, null=True)
    read_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f'{self.subscriber.firstname} {self.subscriber.lastname}: {self.mail.title}'
