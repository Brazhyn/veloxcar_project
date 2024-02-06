from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from . models import User
from datetime import datetime


# - Create/Register a user (ModelForm)

class RegisterForm(UserCreationForm):
    current_year = datetime.now().year + 1
    result = current_year - 12
    year_range = range(1930, result)

    profile_image = forms.ImageField(required=False)
    address = forms.CharField(max_length=130, required=False)
    date_of_birth = forms.DateField(
        required=False, widget=forms.SelectDateWidget(years=year_range))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2',
                  'profile_image', 'address', 'date_of_birth']

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

        # change labels
        self.fields['username'].label = "Ім'я користувача"
        self.fields['email'].label = 'Електронна пошта'
        self.fields['password1'].label = 'Пароль'
        self.fields['password2'].label = 'Підтвердження пароля'
        self.fields['profile_image'].label = 'Ваше фото'
        self.fields['address'].label = "Адреса проживання"
        self.fields['date_of_birth'].label = "Дата народження"

        # change help_text
        self.fields['username'].help_text = 'Вимагається. 150 символів або менше. Лише літери, цифри та @/./+/-/_.'
        self.fields['email'].help_text = ''
        self.fields['password1'].help_text = 'Ваш пароль повинен містити не менше 8 символів. Також пароль не може бути повністю цифровим.'
        self.fields['password2'].help_text = 'Для підтвердження введіть той самий пароль, що й раніше.'
        self.fields['profile_image'].help_text = "Не обов'язково для заповненння."
        self.fields['address'].help_text = "Не обов'язково для заповненння."
        self.fields['date_of_birth'].help_text = "Не обов'язково для заповненння."


# - Authenticate a user (ModelForm)

class LoginForm(AuthenticationForm):

    class Meta:
        model = User
        fields = ['username', 'password']

    def __init__(self, request: Any = ..., *args: Any, **kwargs: Any) -> None:
        super().__init__(request, *args, **kwargs)

        # change labels
        self.fields['username'].label = "Ім'я користувача"
        self.fields['password'].label = 'Пароль'
