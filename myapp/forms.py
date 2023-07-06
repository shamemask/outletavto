from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
    FACE = (
        ('physical', 'Физическое лицо'),
        ('legal', 'Юридическое лицо'),
    )
    MAGAZINS = (
        ('magazin1','Магазин1'),
        ('magazin2','Магазин2'),
    )
    magazins = forms.ChoiceField(choices=MAGAZINS,widget=forms.Select(attrs={'class': 'input-silver dropped-wrapper'}))
    shop = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-silver'}))
    contact_person = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-silver'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-silver'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'input-silver'}))
    promo_code = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-silver'}), required=False)
    terms_of_service = forms.BooleanField()
    user_type = forms.ChoiceField(choices=FACE, widget=forms.RadioSelect(attrs={'class': 'transparent-btn tab-btn'}))
    city = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-silver'}))
    legal_shop = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-silver'}))
    inn = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-silver'}))
    kpp = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-silver'}))
    bank = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-silver'}))
    bik = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-silver'}))
    account_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-silver'}))
    correspondent_account = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-silver'}))
    terms_of_service_2 = forms.BooleanField()

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'shop', 'contact_person', 'phone', 'email', 'promo_code',
                  'terms_of_service', 'user_type', 'city', 'legal_shop', 'inn', 'kpp', 'bank', 'bik',
                  'account_number', 'correspondent_account', 'terms_of_service_2')
