from django.db import models


class ZodiacSign(models.Model):
    sign_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.sign_id}-{self.name}"


class Professions(models.Model):
    profession_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class FamousPerson(models.Model):
    person_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    birth_date = models.DateField(default=None)
    zodiac_sign = models.ForeignKey(ZodiacSign, on_delete=models.CASCADE, default=None, null=True, blank=True)
    profession = models.ForeignKey(Professions, on_delete=models.CASCADE)


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    zodiac_sign = models.ForeignKey(ZodiacSign, on_delete=models.CASCADE)
