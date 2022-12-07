import json
from django.forms import model_to_dict
from django.test import TestCase
import factory
import requests

from apps.endereco.models import Endereco


# Create your tests here.
class EnderecoFactory(factory.Factory):
    class Meta:
        model = Endereco


class EnderecoTestCase(TestCase):
    def setUp(self):
        self.numero_cep = 58900000

    def test_cadastrar_cep_errado(self):
        req = requests.get(f"https://viacep.com.br/ws/{self.numero_cep}/json/")

        data = json.loads(req.text)

        endereco = EnderecoFactory()
        endereco.cep = data["cep"]
        endereco.logradouro = data["logradouro"]
        endereco.complemento = data["complemento"]
        endereco.bairro = data["bairro"]
        endereco.localidade = data["localidade"]
        endereco.uf = data["uf"]
        endereco.ibge = data["ibge"]
        endereco.gia = data["gia"]
        endereco.ddd = data["ddd"]
        endereco.siafi = data["siafi"]
        endereco.save()

        model = model_to_dict(endereco, exclude=["id"])

        self.assertEquals(data, model)
        # self.assertNotEquals(model["logradouro"], "")
