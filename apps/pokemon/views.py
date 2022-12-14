import json

import requests
from django.forms import model_to_dict
from django.http import JsonResponse

from apps.pokemon.models import Pokemon


# Create your views here.


def register_pokemon_by_name(request, name):
    req = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name}/")
    data = json.loads(req.text)

    pokemon = Pokemon.objects.create(**data)

    model = model_to_dict(pokemon)

    return JsonResponse(model)


def buscar_name(request, name):
    pokemon = Pokemon.objects.get(name=name)

    model = model_to_dict(pokemon)

    print(model)

    return JsonResponse(model)
