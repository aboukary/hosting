from django.db import models


class Student(models.Model):

    GENDER_CHOICES = [
        ("M", "Masculin"),
        ("F", "Féminin"),
    ]

    LEVEL_CHOICES = [
        ("L1", "Licence 1"),
        ("L2", "Licence 2"),
        ("L3", "Licence 3"),
        ("M1", "Master 1"),
        ("M2", "Master 2"),
    ]

    first_name = models.CharField("Prénom", max_length=100)

    last_name = models.CharField("Nom", max_length=100)

    matricule = models.CharField(
        "Matricule",
        max_length=20,
        unique=True,
    )

    email = models.EmailField(
        "Adresse email",
        unique=True,
    )

    phone = models.CharField(
        "Téléphone",
        max_length=20,
        blank=True,
    )

    gender = models.CharField(
        "Sexe",
        max_length=1,
        choices=GENDER_CHOICES,
    )

    department = models.CharField(
        "Filière",
        max_length=100,
    )

    level = models.CharField(
        "Niveau",
        max_length=2,
        choices=LEVEL_CHOICES,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        ordering = ["last_name", "first_name"]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"