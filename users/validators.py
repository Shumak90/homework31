from datetime import date

from django.core.exceptions import ValidationError
from rest_framework import serializers


def age_validator(value: date):
    today = date.today()
    age = today.year - value.year - ((today.month, today.day) < (value.month, value.day))
    if age < 9:
        raise ValidationError(f"Возраст {age}, не может быть меньше 9")


class MailValidator:
    def __init__(self, domains):
        if not isinstance(domains, list):
            domains = [domains]

        self.domains = domains

    def __call__(self, email):
        domain = email.split('@')[1]
        if domain in self.domains:
            raise serializers.ValidationError(f"Домен не может быть {domain}")

