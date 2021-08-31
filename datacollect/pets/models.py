from django.core.validators import MinValueValidator
from django.db import models


class Pet(models.Model):
    MALE = 'male'
    FEMALE = 'female'

    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )

    name = models.CharField(
        max_length=20,
    )

    gender = models.CharField(
        max_length=6,
        choices=GENDER_CHOICES,
        default=MALE,
    )

    age = models.IntegerField(
        validators=(
            MinValueValidator(0),
        ),
        default=0,
    )

    food = models.CharField(
        max_length=20,
    )

    notes = models.TextField(
        max_length=255,
        null=True,
        blank=True,
    )
