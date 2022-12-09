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

        pokemon_model = model_to_dict(pokemon)
        self.assertNotEquals(pokemon_model["name"], "")
        self.assertLessEqual(len(pokemon_model["name"]), 11)

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

        pokemon_model = model_to_dict(pokemon)
        self.assertTrue(type(pokemon_model["weight"]) == int)
        self.assertGreater(pokemon_model["weight"], 0)
        self.assertTrue(type(pokemon_model["height"]) == int)
        self.assertGreater(pokemon_model["height"], 0)
        self.assertTrue(type(pokemon_model["base_experience"]) == int)
        self.assertGreater(pokemon_model["base_experience"], 0)

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

        pokemon_model = model_to_dict(pokemon)
        self.assertTrue(type(pokemon_model["id"]) == int)
        self.assertGreaterEqual(pokemon_model["id"], 0)

    def test_is_pokemon_present(self):
        req = requests.get(f"https://pokeapi.co/api/v2/pokemon/{self.name}/")

        data = json.loads(req.text)

        pokemon = PokemonFactory()
        pokemon.id = data["id"]
        pokemon.name = data["name"]
        pokemon.weight = data["weight"]
        pokemon.height = data["height"]
        pokemon.base_experience = data["base_experience"]

        pokemon.save()

        pokemon_model = model_to_dict(pokemon)
        pokemon_db = model_to_dict(Pokemon.objects.get(name=self.name))
        self.assertNotEquals(pokemon_model, pokemon_db)

