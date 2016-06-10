from phonenumber_field.modelfields import PhoneNumberField
import pycountry

from django.db import models
from django.conf.global_settings import LANGUAGES


CURRENCY_CHOICES = [(currency.letter, currency.name) for currency in list(pycountry.currencies)]


class Provider(models.Model):
    """This model stores information on providers."""

    name = models.CharField(max_length=300)
    email = models.EmailField()
    phone_no = PhoneNumberField()
    language = models.CharField(max_length=7, choices=LANGUAGES)
    currency = models.CharField(
        max_length=10,
        choices=CURRENCY_CHOICES
    )

    def __str__(self):
        return self.name
