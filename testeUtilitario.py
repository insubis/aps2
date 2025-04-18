import unittest
from math_operations import soma

class TestMathOperations(unittest.TestCase):
    def test_soma_simples(self):
        self.assertEqual(soma(2, 3), 5)

    def test_soma_negativos(self):
        self.assertEqual(soma(-1, -1), -2)

if __name__ == '__main__':
    unittest.main()


from django.test import TestCase
from .models import Animal

class AnimalModelTest(TestCase):
    def test_criacao_animal(self):
        animal = Animal.objects.create(nome='Rex', especie='Cachorro')
        self.assertEqual(animal.nome, 'Rex')
        self.assertEqual(animal.especie, 'Cachorro')

    def test_busca_animal(self):
        Animal.objects.create(nome='Mimi', especie='Gato')
        resultado = Animal.objects.filter(nome='Mimi').first()
        self.assertIsNotNone(resultado)
        self.assertEqual(resultado.especie, 'Gato')

teste =  "111111"