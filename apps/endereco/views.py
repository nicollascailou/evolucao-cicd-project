import json

import requests
from django.forms import model_to_dict
from django.http import JsonResponse

from apps.endereco.models import Endereco


# Create your views here.


def cadastrar_endereco_cep(request, cep):
    req = requests.get(f"https://viacep.com.br/ws/{cep}/json/")

    data = json.loads(req.text)

    endereco = Endereco.objects.create(**data)

    model = model_to_dict(endereco)

    return JsonResponse(model)


def buscar_cep(request, cep):
    endereco = Endereco.objects.get(cep=cep)

    model = model_to_dict(endereco)

    print(model)

    return JsonResponse(model)
