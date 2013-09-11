from django import forms
from django.forms import ModelForm
from django.core.validators import email_re
from widgets import AdminImageWidget
from models import Decoration, DecorationIngredient


class ContactForm(forms.Form):
    DecorationNote = forms.CharField(widget=forms.Textarea(attrs={'class':'notebox', "placeholder": 'Here you can write your comment!'}))
    TortNote = forms.CharField(widget=forms.Textarea(attrs={'class':'notebox', "placeholder": 'Here you can write your comment!'}))
    DecorationIngredient = forms.ChoiceField(
        widget=forms.Select(attrs={'id': 'id_decoration_ingredient'}),
        choices=[("", "Выберите состав")] + [(it.pk, it.title_ru) for it in DecorationIngredient.objects.all()]
    )
    CustomerName= forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'validate[required] inputctrl'})) #validate[required,custom[onlyLetter],funcCall[validate2fields],length[0,100]]
    EMail= forms.EmailField(required=True, widget=forms.TextInput(attrs={'class':'validate[required,custom[email]] inputctrl'}))
    Phone= forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'validate[required] inputctrl'}))
    DeliveryAddress = forms.CharField(widget=forms.Textarea(attrs={'class':'notebox'}))
    Note = forms.CharField(widget=forms.Textarea(attrs={'class':'notebox'}))


class DecorationAdminForm(ModelForm):
    class Meta:
        model = Decoration
        widgets = {
            'photo': AdminImageWidget(),
        }