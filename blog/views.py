from django.shortcuts import render


def zodiac_signs_list(request):
    return render(request, 'blog/zodiac_signs_list.html', {})

