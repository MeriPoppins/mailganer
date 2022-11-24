from django.contrib import admin
from django import forms
from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import Subscriber, Mailing
from .forms import MailingForm
from .utils import sent_mailing


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('id', 'firstname', 'lastname', 'birthday', 'email', 'is_mailing', 'mailing_id')
    list_display_links = ('id', 'firstname', 'lastname')
    search_fields = ('firstname', 'lastname', 'email', 'gender')
    list_filter = ('birthday', 'gender', 'is_mailing')
    readonly_fields = ('created_at', )

    autocomplete_fields = ('mailing_id',)

    actions = [
        '_add_mailing',
        '_sent_mailing',
        '_delete_mailing'
    ]

    def _add_mailing(self, request, queryset):
        """
        Функция для группового действия "Добавить рассылку".
        :return:
        """

        if 'apply' in request.POST:
            form = MailingForm(request.POST)
            mailing_id = form.data['mailing_id']
            count = queryset.update(mailing_id=mailing_id, is_mailing=True)
            self.message_user(request, "Для %s подписчиков добавлена рассылка" % count)
            return HttpResponseRedirect(request.get_full_path())
        else:
            form = MailingForm(
                initial={'_selected_action': request.POST.getlist(admin.helpers.ACTION_CHECKBOX_NAME)}
            )
        return render(request, 'mail/add_mailing.html', context={'subscribers': queryset, "form": form})

    _add_mailing.short_description = 'Добавить рассылку'

    def _sent_mailing(self, request, queryset):
        """
        Функция для группового действия "Отправить рассылку".
        :return:
        """
        count = 0
        for subscriber in queryset:
            if subscriber.is_mailing is True and subscriber.mailing_id is not None:
                subscriber_pk = subscriber.pk
                sent_mailing(subscriber_pk)
                count += 1

        self.message_user(
            request,
            f"Рассылка отправлена для {count} подписчиков"
        )
        return HttpResponseRedirect(request.get_full_path())

    _sent_mailing.short_description = 'Отправить рассылку'

    def _delete_mailing(self, request, queryset):
        """
        Функция для группового действия "Удалить рассылку".
        :return:
        """
        count = 0
        for subscriber in queryset:
            if subscriber.is_mailing is True:
                subscriber.is_mailing = False
                subscriber.mailing_id = None
                subscriber.clean()
                subscriber.save()
                count += 1

        self.message_user(
            request,
            f"Рассылка удалена для {count} подписчиков"
        )
        return HttpResponseRedirect(request.get_full_path())

    _delete_mailing.short_description = 'Удалить рассылку'


class MailingAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget(), help_text='Теги добавляем в двойных фигурных скобках {{}}: firstname - имя, lastname - фамилия, birthday - день рождения')
    
    class Meta:
        model = Mailing
        fields = '__all__'


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    form = MailingAdminForm
    list_display = ('id', 'title', 'created_at')
    list_display_links = ('id', 'title')
    search_fields = ('title', )
    readonly_fields = ('created_at', )

