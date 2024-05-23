from django.db import models


class ZodiacSign(models.Model):
    sign_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)


class Professions(models.Model):
    profession_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)


class FamousPerson(models.Model):
    person_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    zodiac_sign = models.ForeignKey(ZodiacSign, on_delete=models.CASCADE)
    profession = models.ForeignKey(Professions, on_delete=models.CASCADE)


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    zodiac_sign = models.ForeignKey(ZodiacSign, on_delete=models.CASCADE)
