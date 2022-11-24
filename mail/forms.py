from django import forms

from .models import Mailing


class MailingForm(forms.Form):
    _selected_action = forms.CharField(widget=forms.MultipleHiddenInput)
    mailing_id = forms.ModelChoiceField(queryset=Mailing.objects.all(), label='Выберите рассылку:')

    mailing_id.widget.attrs.update({"class": "form-control mb-2 mt-2"})
