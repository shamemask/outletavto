from django import forms


class RegistrationForm(forms.Form):
    shop_choices = [
        ('','Магазины*'),
        ('Магазин 1', 'Магазин 1'),
        ('Магазин 2', 'Магазин 2'),
        # Добавьте другие варианты магазинов здесь
    ]
    city_choices = [
        ('', 'Города*'),
        ('Город 1', 'Город 1'),
        ('Город 2', 'Город 2'),
        # Добавьте другие варианты городов здесь
    ]

    forma_choices = [
        ('', 'Форма*'),
        ('Форма 1', 'Форма 1'),
        ('Форма 2', 'Форма 2'),
        # Добавьте другие варианты Форм здесь
    ]

    shop = forms.ChoiceField(choices=shop_choices, label='Магазин', widget=forms.Select(attrs={'class': 'input-silver dropped-wrapper', 'style': 'border-radius: 10px;', 'placeholder': 'Магазин*'}))
    full_name = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'class': 'input-silver', 'placeholder': 'Контактное лицо (ФИО)*'}))
    phone = forms.CharField(max_length=20,
                            widget=forms.TextInput(attrs={'class': 'input-silver', 'placeholder': 'Телефон*'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'input-silver', 'placeholder': 'Email*'}))
    promo_code = forms.CharField(max_length=255,
                                 widget=forms.TextInput(attrs={'class': 'input-silver', 'placeholder': 'Промокод'}), required=False)
    terms_of_service = forms.BooleanField( label='Я ознакомился и принимаю условия договора-оферты',
                                          widget=forms.CheckboxInput(attrs={'class': 'check-with-label', 'for': "offer"}))
    password = forms.CharField(max_length=20,
                            widget=forms.PasswordInput(attrs={'class': 'input-silver','style':'font-size:10', 'placeholder': 'Введите пароль*'}))
    password2 = forms.CharField(max_length=20,
                               widget=forms.PasswordInput(
                                   attrs={'class': 'input-silver','style':'font-size:10', 'placeholder': 'Повтор пароля*'}))
    forma = forms.ChoiceField(choices=city_choices,label='Форма', widget=forms.Select(
        attrs={'class': 'input-silver dropped-wrapper', 'placeholder': 'Форма'}))

    city = forms.ChoiceField(choices=forma_choices, label='Города', widget=forms.Select(attrs={'class': 'input-silver dropped-wrapper', 'placeholder': 'Город'}))

    legal_address = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'class': 'input-silver', 'placeholder': 'Юридический адрес*'}))

    company_name = forms.CharField(max_length=9, widget=forms.TextInput(attrs={'class': 'input-silver', 'placeholder': 'Название*'}))
    inn = forms.CharField(max_length=12, widget=forms.TextInput(attrs={'class': 'input-silver', 'placeholder': 'ИНН*'}))
    kpp = forms.CharField(max_length=9, widget=forms.TextInput(attrs={'class': 'input-silver', 'placeholder': 'КПП*'}))
    bank = forms.CharField(max_length=255,
                           widget=forms.TextInput(attrs={'class': 'input-silver', 'placeholder': 'Банк*'}))
    bik = forms.CharField(max_length=9, widget=forms.TextInput(attrs={'class': 'input-silver', 'placeholder': 'БИК*'}))
    account_number = forms.CharField(max_length=20,
                                     widget=forms.TextInput(attrs={'class': 'input-silver', 'placeholder': 'Р/с*'}))
    correspondent_account = forms.CharField(max_length=20, widget=forms.TextInput(
        attrs={'class': 'input-silver', 'placeholder': 'К/c*'}))

    def save(self, request):
        user = super().save(request)
        user.shop_name = self.cleaned_data['shop_name']
        user.full_name = self.cleaned_data['full_name']
        user.phone = self.cleaned_data['phone']
        user.promo_code = self.cleaned_data['promo_code']
        user.terms_of_service = self.cleaned_data['terms_of_service']
        user.city = self.cleaned_data['city']
        user.shop_name2 = self.cleaned_data['shop_name2']
        user.form = self.cleaned_data['form']
        user.organization_name = self.cleaned_data['organization_name']
        user.legal_address = self.cleaned_data['legal_address']
        user.inn = self.cleaned_data['inn']
        user.kpp = self.cleaned_data['kpp']
        user.bank = self.cleaned_data['bank']
        user.bik = self.cleaned_data['bik']
        user.account_number = self.cleaned_data['account_number']
        user.correspondent_account = self.cleaned_data['correspondent_account']
        user.save()
        return user

class UserSignupView:
    form_class = RegistrationForm
    template_name = 'pages/registration.html'