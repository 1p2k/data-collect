from random import choices

from django.core.validators import MinValueValidator
from django.db import models


class Pet(models.Model):
    CAT = 'cat'
    DOG = 'dog'
    BIRD = 'bird'
    RODENT = 'rodent'
    FISH = 'fish'
    REPTILE = 'reptile'
    FERRET = 'ferret'
    OTHER = 'other'

    TYPE_CHOICES = (
        (CAT, 'Cat'),
        (DOG, 'Dog'),
        (BIRD, 'Bird'),
        (RODENT, 'Rodent'),
        (FISH, 'Fish'),
        (REPTILE, 'Reptile'),
        (FERRET, 'Ferret'),
        (OTHER, 'Other'),
    )

    MALE = 'male'
    FEMALE = 'female'

    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )

    name = models.CharField(
        max_length=20,
    )

    type = models.CharField(
        max_length=7,
        choices=TYPE_CHOICES,
        default=CAT,
    )

    gender = models.CharField(
        max_length=6,
        choices=GENDER_CHOICES,
        default=FEMALE,
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
