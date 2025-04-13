from datetime import date

from django.core.exceptions import ValidationError


def real_age(value: date) -> None:
    age = (date.today() - value).days / 365
    if age < 1 or age > 120:
        raise ValidationError('Ожидается возраст от 1 года до 120 лет')


'''
Теперь нужно применить валидатор к форме. Если это форма forms.Form, то
валидатор указывается в том поле формы, которое он должен проверять, в
аргументе validators.
Для форм на основе forms.ModelForm валидатор указывается в поле самой
модели — тоже в аргументе validators:
'''
