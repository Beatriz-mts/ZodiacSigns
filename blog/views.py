from django.shortcuts import render
from .models import ZodiacSign, FamousPerson


def zodiac_sign_list(request):
    # Query the ZodiacSign model and order by the first letter of the name
    zodiac_signs = ZodiacSign.objects.all().order_by('name')
    return render(request, 'blog/zodiac_sign_list.html', {'zodiac_signs': zodiac_signs})


def aries_list(request):
    # Query the FamousPerson model and order by the ones that have Aries as solar zodiac sign by the sign_id
    signs_aries = FamousPerson.objects.filter(zodiac_sign=1)
    return render(request, 'blog/aries_list.html', {'signs_aries': signs_aries})


def taurus_list(request):
    # Query the FamousPerson model and order by the ones that have Taurus as solar zodiac sign by the sign_id
    signs_taurus = FamousPerson.objects.filter(zodiac_sign=2)
    return render(request, 'blog/taurus_list.html', {'signs_taurus': signs_taurus})


def gemini_list(request):
    # Query the FamousPerson model and order by the ones that have Gemini as solar zodiac sign by the sign_id
    signs_gemini = FamousPerson.objects.filter(zodiac_sign=3)
    return render(request, 'blog/gemini_list.html', {'signs_gemini': signs_gemini})


def cancer_list(request):
    # Query the FamousPerson model and order by the ones that have Cancer as solar zodiac sign by the sign_id
    signs_cancer = FamousPerson.objects.filter(zodiac_sign=4)
    return render(request, 'blog/cancer_list.html', {'signs_cancer': signs_cancer})


def leo_list(request):
    # Query the FamousPerson model and order by the ones that have Leo as solar zodiac sign by the sign_id
    signs_leo = FamousPerson.objects.filter(zodiac_sign=5)
    return render(request, 'blog/leo_list.html', {'signs_leo': signs_leo})


def virgo_list(request):
    # Query the FamousPerson model and order by the ones that have Virgo as solar zodiac sign by the sign_id
    signs_virgo = FamousPerson.objects.filter(zodiac_sign=6)
    return render(request, 'blog/virgo_list.html', {'signs_virgo': signs_virgo})


def libra_list(request):
    # Query the FamousPerson model and order by the ones that have Libra as solar zodiac sign by the sign_id
    signs_libra = FamousPerson.objects.filter(zodiac_sign=7)
    return render(request, 'blog/libra_list.html', {'signs_libra': signs_libra})


def scorpio_list(request):
    # Query the FamousPerson model and order by the ones that have Scorpio as solar zodiac sign by the sign_id
    signs_scorpio = FamousPerson.objects.filter(zodiac_sign=8)
    return render(request, 'blog/scorpio_list.html', {'signs_scorpio': signs_scorpio})


def sagittarius_list(request):
    # Query the FamousPerson model and order by the ones that have Sagittarius as solar zodiac sign by the sign_id
    signs_sagittarius = FamousPerson.objects.filter(zodiac_sign=9)
    return render(request, 'blog/sagittarius_list.html', {'signs_sagittarius': signs_sagittarius})


def capricorn_list(request):
    # Query the FamousPerson model and order by the ones that have Capricorn as solar zodiac sign by the sign_id
    signs_capricorn = FamousPerson.objects.filter(zodiac_sign=10)
    return render(request, 'blog/capricorn_list.html', {'signs_capricorn': signs_capricorn})


def aquarius_list(request):
    # Query the FamousPerson model and order by the ones that have Aquarius as solar zodiac sign by the sign_id
    signs_aquarius = FamousPerson.objects.filter(zodiac_sign=11)
    return render(request, 'blog/aquarius_list.html', {'signs_aquarius': signs_aquarius})


def pisces_list(request):
    # Query the FamousPerson model and order by the ones that have Pisces as solar zodiac sign by the sign_id
    signs_pisces = FamousPerson.objects.filter(zodiac_sign=12)
    return render(request, 'blog/pisces_list.html', {'signs_pisces': signs_pisces})

