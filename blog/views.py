from django.shortcuts import render, redirect
from django.urls import reverse

from .models import ZodiacSign, FamousPerson, Professions
from .forms import FamousPersonForm
from .services import get_zodiac_sign_from_birthdate


def zodiac_sign_list(request):
    # context = {"zodiac_sign_list": ZodiacSign.objects.all}
    # return render(request, "blog/zodiac_sign_list.html", context)
    zodiac_signs = ZodiacSign.objects.all()
    context = {"zodiac_sign_list": zodiac_signs}
    return render(request, "blog/zodiac_sign_list.html", context)


def get_zodiac_sign(request, pk):
    context = {"get_zodiac_sign": FamousPerson.objects.filter(zodiac_sign=pk)}
    return render(request, 'blog/get_zodiac_sign.html', context)


def create_new_famous_person(request):
    if request.method == 'POST':
        form = FamousPersonForm(request.POST)
        if form.is_valid():
            # Salva a instância do form, mas não commita ao banco ainda
            new_person = form.save(commit=False)

            # Obtém o signo do zodíaco baseado na data de nascimento
            birth_date = form.cleaned_data["birth_date"]
            zodiac_sign = get_zodiac_sign_from_birthdate(birth_date)

            # Atribui o signo do zodíaco à nova pessoa
            new_person.zodiac_sign = zodiac_sign

            # Salva a nova pessoa com todos os dados
            new_person.save()

            # Redireciona para a visualização do signo do zodíaco
            return redirect(reverse("get_zodiac_sign", kwargs={"pk": new_person.zodiac_sign.pk}))
        else:
            return render(request, 'blog/create_new_famous_person.html', context={"form": form, "errors": form.errors})
    else:
        form = FamousPersonForm()
    return render(request, 'blog/create_new_famous_person.html', context={"form": form})


def get_famous_person(request, pk):
    context = {"get_famous_person": FamousPerson.objects.get(person_id=pk)}
    return render(request, 'blog/delete_or_update_famous_person.html', context)


def delete_famous_person(_, pk):
    FamousPerson.objects.filter(person_id=pk).delete()
    return redirect(reverse("zodiac_sign_list"))


def update_famous_person(request, pk):
    FamousPerson.objects.filter(person_id=pk).update(name=request.POST["name"])
    return redirect(reverse("get_zodiac_sign", kwargs={"pk": pk}))

