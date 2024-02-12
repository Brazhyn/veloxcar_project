from django import forms
from .models import Category, CarPost


class CategoryForm(forms.ModelForm):

    class Meta:

        model = Category
        fields = '__all__'

        labels = {
            'name': 'Категорія',
            'image': 'Фото',
            'description': 'Опис'
        }

        error_messages = {
            'name': {
                'required': 'Це поле є обов\'язковим.',
                'max_length': 'Дозволено не більше 150 символів.',
            },
            'image': {
                'required': 'Це поле є обов\'язковим.',
            },
            'description': {
                'required': 'Це поле є обов\'язковим.',
                'min_length': 'Мінімальна довжина повинна бути 20 символів.',
            },
        }


class CarPostForm(forms.ModelForm):

    class Meta:
        model = CarPost

        exclude = ['slug', 'date_published', 'author']

        labels = {
            'brand': 'Марка',
            'car_model': 'Модель',
            'year': 'Рік',
            'price': 'Ціна',
            'excerpt': 'Короткий опис',
            'image': 'Фото',
            'date_published': 'Дата публікації',
            'content': 'Головний текст',
            'category': 'Категорія',
            'author': 'Автор'
        }

        error_messages = {
            'brand': {
                'required': 'Це поле є обов\'язковим.',
                'max_length': 'Дозволено не більше 150 символів.'
            },

            'car_model': {
                'required': 'Це поле є обов\'язковим.',
                'max_length': 'Дозволено не більше 150 символів.'
            },

            'year': {
                'min_value': 'Рік не може бути менше 0.',
            },
            'price': {
                'min_value': 'Ціна не може бути менше 0.',
            },
            'excerpt': {
                'max_length': 'Максимальна довжина витримки - 200 символів.',
            },
            'image': {
                'required': 'Це поле є обов\'язковим.',
            },
            'content': {
                'min_length': 'Мінімальна довжина змісту повинна бути 10 символів.',
            },
            'category': {
                'required': 'Це поле є обов\'язковим.',
            },
            'author': {
                'required': 'Це поле є обов\'язковим.',
            }
        }


class CarPostUpdateForn(forms.ModelForm):
    class Meta:
        model = CarPost

        exclude = ['slug', 'date_published', 'author']

        labels = {
            'brand': 'Марка',
            'car_model': 'Модель',
            'year': 'Рік',
            'price': 'Ціна',
            'excerpt': 'Короткий опис',
            'image': 'Фото',
            'date_published': 'Дата публікації',
            'content': 'Головний текст',
            'category': 'Категорія',
            'author': 'Автор'
        }
        
        widgets = {
            'image': forms.FileInput(),
        }

        error_messages = {
            'brand': {
                'required': 'Це поле є обов\'язковим.',
                'max_length': 'Дозволено не більше 150 символів.'
            },

            'car_model': {
                'required': 'Це поле є обов\'язковим.',
                'max_length': 'Дозволено не більше 150 символів.'
            },

            'year': {
                'min_value': 'Рік не може бути менше 0.',
            },
            'price': {
                'min_value': 'Ціна не може бути менше 0.',
            },
            'excerpt': {
                'max_length': 'Максимальна довжина витримки - 200 символів.',
            },
            'image': {
                'required': 'Це поле є обов\'язковим.',
            },
            'content': {
                'min_length': 'Мінімальна довжина змісту повинна бути 10 символів.',
            },
            'category': {
                'required': 'Це поле є обов\'язковим.',
            },
            'author': {
                'required': 'Це поле є обов\'язковим.',
            }
        }
