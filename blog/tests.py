from datetime import datetime

import pytest as pytest
from django.urls import reverse

from blog.models import ZodiacSign, FamousPerson, Professions
from blog.services import get_zodiac_sign_from_birthdate


# from views import create_new_famous_person


@pytest.mark.django_db
def test_list_albuns_view(client):
    # GIVEN:
    # Criar um objeto de Zodiac_sign para ser usado no teste
    zodiac_sign_one = ZodiacSign.objects.create(name='Sign one')
    zodiac_sign_two = ZodiacSign.objects.create(name='Sign two')

    # WHEN:
    # Cria uma solicitação GET para a view
    response = client.get(reverse('zodiac_sign_list'))

    # THEN:
    # Verifica se a resposta tem o código de status 200 (OK)
    assert response.status_code == 200

    # Verifica se a lista de famous_person está presente no contexto da resposta
    # um queryset
    assert list(response.context['zodiac_sign_list']) == [zodiac_sign_one, zodiac_sign_two]


@pytest.mark.django_db
def test_delete_famous_person(client):
    # GIVEN:
    # Crie uma pessoa famosa para excluir
    profession = Professions.objects.create(name='Bascketball player')
    zodiac_sign = ZodiacSign.objects.create(name='Leo')
    famous_person = FamousPerson.objects.create(name='Test Famous Person', birth_date='1963-08-17', profession_id=1,
                                                zodiac_sign_id=1)

    # WHEN:
    # Crie uma solicitação POST para a view de exclusão
    response = client.post(reverse('delete_famous_person', kwargs={'pk': famous_person.pk}))

    # THEN:
    assert response.status_code == 302

    # Verifique se o álbum foi excluído
    assert FamousPerson.objects.filter(pk=famous_person.pk).exists() is False


@pytest.mark.django_db
def test_update_famous_person(client):
    # GIVEN: Criar um objeto ZodiacSign e FamousPerson para serem usados no teste
    zodiac_sign = ZodiacSign.objects.create(name='Sign One')
    profession = Professions.objects.create(name='Bascketball player')
    famous_person = FamousPerson.objects.create(name='Old Name', birth_date='2000-01-01', zodiac_sign=zodiac_sign,
                                                profession_id=profession.id)

    # Novo nome para atualizar
    new_name = "New Name"

    # WHEN: Criar uma solicitação POST para a view com o novo nome
    response = client.post(reverse('update_famous_person', kwargs={'pk': famous_person.person_id}),
                           data={'name': new_name})

    # THEN: Verificar se o objeto FamousPerson foi atualizado corretamente
    famous_person.refresh_from_db()
    assert famous_person.name == new_name

    # Verificar se a resposta redireciona para a URL esperada
    assert response.status_code == 302  # Código de status de redirecionamento
    assert response.url == reverse('get_zodiac_sign', kwargs={'pk': famous_person.zodiac_sign.pk})


@pytest.mark.django_db
def test_delete_famous_perso(client):
    # GIVEN:
    # Crie uma famous person para excluir
    zodiac_sign = ZodiacSign.objects.create(name='Sign One')
    profession = Professions.objects.create(name='Bascketball player')
    famous_person = FamousPerson.objects.create(name='Old Name', birth_date='2000-01-01', zodiac_sign=zodiac_sign,
                                                profession_id=1)

    # WHEN:
    # Crie uma solicitação POST para a view de exclusão
    response = client.post(reverse('delete_famous_person', kwargs={'pk': famous_person.person_id}))

    # THEN:
    assert response.status_code == 302

    # Verifique se a famous person foi excluído
    assert FamousPerson.objects.filter(pk=famous_person.pk).exists() is False


@pytest.mark.django_db
def test_get_zodiac_sign_from_birthdate(client):
    # GIVEN:

    # Crie os signos do zodíaco no banco de dados
    capricorn = ZodiacSign.objects.create(name="Capricorn")
    aquarius = ZodiacSign.objects.create(name="Aquarius")
    pisces = ZodiacSign.objects.create(name="Pisces")
    aries = ZodiacSign.objects.create(name="Aries")
    taurus = ZodiacSign.objects.create(name="Taurus")
    gemini = ZodiacSign.objects.create(name="Gemini")
    cancer = ZodiacSign.objects.create(name="Cancer")
    leo = ZodiacSign.objects.create(name="Leo")
    virgo = ZodiacSign.objects.create(name="Virgo")
    libra = ZodiacSign.objects.create(name="Libra")
    scorpio = ZodiacSign.objects.create(name="Scorpio")
    sagittarius = ZodiacSign.objects.create(name="Sagittarius")

    # Converta a string birth_date para um objeto datetime.date
    birth_date_str = "2000-01-01"
    birth_date = datetime.strptime(birth_date_str, "%Y-%m-%d").date()
    zodiac_sign = get_zodiac_sign_from_birthdate(birth_date)
    profession = Professions.objects.create(name='Bascketball player')
    famous_person = FamousPerson.objects.create(name='Old Name', birth_date=birth_date, zodiac_sign=zodiac_sign,
                                                profession=profession)

    # WHEN:
    # Cria uma solicitação GET para a view
    response = client.get(reverse('create_new_famous_person'))

    # THEN:
    # Verifica se a resposta tem o código de status 200 (OK)
    assert response.status_code == 200

    # Verifica se a lista de famous_person está presente no contexto da resposta
    # um queryset
    assert 'form' in response.context
    # assert list(response.context['create_new_famous_person']) == [famous_person]


# birth_date = form.cleaned_data["birth_date"]
# zodiac_sign = get_zodiac_sign_from_birthdate(birth_date)
