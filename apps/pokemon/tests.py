import json
from django.forms import model_to_dict
from django.test import TestCase
import factory
import requests

from apps.pokemon.models import Pokemon


# Create your tests here.
class PokemonFactory(factory.Factory):
    class Meta:
        model = Pokemon


class PokemonTestCase(TestCase):
    def setUp(self):
        self.name = "pikachu"

    def test_register_wrong_name(self):
        req = requests.get(f"https://pokeapi.co/api/v2/pokemon/{self.name}/")

        data = json.loads(req.text)

        pokemon = PokemonFactory()
        pokemon.id = data["id"]
        pokemon.name = data["name"]
        pokemon.weight = data["weight"]
        pokemon.height = data["height"]
        pokemon.base_experience = data["base_experience"]

        pokemon.save()

        model = model_to_dict(pokemon, exclude=["id"])

        ##self.assertEquals(data, model)
        self.assertNotEquals(model["name"], "")
