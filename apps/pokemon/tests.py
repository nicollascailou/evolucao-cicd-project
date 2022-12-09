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
        self.name = "fletchinder"

    def test_register_valid_name(self):
        req = requests.get(f"https://pokeapi.co/api/v2/pokemon/{self.name}/")

        data = json.loads(req.text)

        pokemon = PokemonFactory()
        pokemon.id = data["id"]
        pokemon.name = data["name"]
        pokemon.weight = data["weight"]
        pokemon.height = data["height"]
        pokemon.base_experience = data["base_experience"]

        pokemon.save()

        model = model_to_dict(pokemon)
        self.assertNotEquals(model["name"], "")
        self.assertLessEqual(len(model["name"]), 11)

    def test_register_valid_atr(self):
        req = requests.get(f"https://pokeapi.co/api/v2/pokemon/{self.name}/")

        data = json.loads(req.text)

        pokemon = PokemonFactory()
        pokemon.id = data["id"]
        pokemon.name = data["name"]
        pokemon.weight = data["weight"]
        pokemon.height = data["height"]
        pokemon.base_experience = data["base_experience"]

        pokemon.save()

        model = model_to_dict(pokemon)
        self.assertTrue(type(model["weight"]) == int)
        self.assertGreater(model["weight"], 0)
        self.assertTrue(type(model["height"]) == int)
        self.assertGreater(model["height"], 0)
        self.assertTrue(type(model["base_experience"]) == int)
        self.assertGreater(model["base_experience"], 0)

    def test_register_valid_id(self):
        req = requests.get(f"https://pokeapi.co/api/v2/pokemon/{self.name}/")

        data = json.loads(req.text)

        pokemon = PokemonFactory()
        pokemon.id = data["id"]
        pokemon.name = data["name"]
        pokemon.weight = data["weight"]
        pokemon.height = data["height"]
        pokemon.base_experience = data["base_experience"]

        pokemon.save()

        model = model_to_dict(pokemon)
        self.assertTrue(type(model["id"]) == int)
        self.assertGreaterEqual(model["id"], 0)
