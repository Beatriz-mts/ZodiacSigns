from .models import ZodiacSign
# from .views import get_zodiac_sign


def get_zodiac_sign_from_birthdate(birthdate):
    # zodiac_sign = get_zodiac_sign(birthdate)
    # TODO 1: adicionar testes para essa função com todos os cenários possíveis
    # https://www.youtube.com/watch?v=qwypH3YvMKc&list=PLbpAWbHbi5rMF2j5n6imm0enrSD9eQUaM
    # TODO 2: corrigir lógica
    # TODO 3: refatorar lógica
    if birthdate.month == 12 and birthdate.day >= 22:
        return ZodiacSign.objects.get(name="Capricorn")
    if birthdate.month == 1 and birthdate.day <= 20:
        return ZodiacSign.objects.get(name="Capricorn")
    elif birthdate.month == 1 and birthdate.day >= 21:
        return ZodiacSign.objects.get(name="Aquarius")
    elif birthdate.month == 2 and birthdate.day <= 18:
        return ZodiacSign.objects.get(name="Aquarius")
    elif birthdate.month == 2 and birthdate.day >= 19:
        return ZodiacSign.objects.get(name="Pisces")
    elif birthdate.month == 3 and birthdate.day <= 20:
        return ZodiacSign.objects.get(name="Pisces")
    elif birthdate.month == 3 and birthdate.day >= 20:
        return ZodiacSign.objects.get(name="Aries")
    elif birthdate.month == 4 and birthdate.day <= 20:
        return ZodiacSign.objects.get(name="Aries")
    elif birthdate.month == 4 and birthdate.day >= 21:
        return ZodiacSign.objects.get(name="Taurus")
    elif birthdate.month == 5 and birthdate.day <= 20:
        return ZodiacSign.objects.get(name="Taurus")
    elif birthdate.month == 5 and birthdate.day >= 21:
        return ZodiacSign.objects.get(name="Gemini")
    elif birthdate.month == 6 and birthdate.day <= 20:
        return ZodiacSign.objects.get(name="Gemini")
    elif birthdate.month == 6 and birthdate.day >= 21:
        return ZodiacSign.objects.get(name="Cancer")
    elif birthdate.month == 7 and birthdate.day <= 22:
        return ZodiacSign.objects.get(name="Cancer")
    elif birthdate.month == 7 and birthdate.day >= 23:
        return ZodiacSign.objects.get(name="Leo")
    elif birthdate.month == 8 and birthdate.day <= 22:
        return ZodiacSign.objects.get(name="Leo")
    elif birthdate.month == 8 and birthdate.day >= 23:
        return ZodiacSign.objects.get(name="Virgo")
    elif birthdate.month == 9 and birthdate.day <= 22:
        return ZodiacSign.objects.get(name="Virgo")
    elif birthdate.month == 9 and birthdate.day >= 23:
        return ZodiacSign.objects.get(name="Libra")
    elif birthdate.month == 10 and birthdate.day <= 22:
        return ZodiacSign.objects.get(name="Libra")
    elif birthdate.month == 10 and birthdate.day >= 23:
        return ZodiacSign.objects.get(name="Scorpio")
    elif birthdate.month == 11 and birthdate.day <= 21:
        return ZodiacSign.objects.get(name="Scorpio")
    elif birthdate.month == 11 and birthdate.day >= 22:
        return ZodiacSign.objects.get(name="Sagittarius")
    elif birthdate.month == 12 and birthdate.day <= 21:
        return ZodiacSign.objects.get(name="Sagittarius")
    else:
        raise ValueError("Zodiac sign not found!")



