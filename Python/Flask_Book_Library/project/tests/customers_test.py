from project.customers.models import Customer
import unittest


class TestBookCreation(unittest.TestCase):
    def test_name_length(self):
        with self.assertRaises(ValueError):
            Customer('a'*2, 'a'*10, 20)
        Customer('a'*3, 'a'*10, 20)
        Customer('a'*40, 'a'*10, 20)
        with self.assertRaises(ValueError):
            Customer('a'*41, 'a'*10, 20)

    def test_name_allowed_characters(self):
        Customer('amnz ZNMA', 'a'*10, 20)

    def test_name_forbidden_characters(self):
        for character in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                          '!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
                          '-', '_', '=', '+', ',', '.', '/', '<', '>', '?',
                          ';', '\'', '\\', ':', '\"', '|', '[', ']', '{', '}',
                          '`', '~']:
            with self.assertRaises(ValueError):
                Customer(character*10, 'a'*10, 20)

    def test_city_length(self):
        with self.assertRaises(ValueError):
            Customer('a'*10, 'a'*2, 20)
        Customer('a'*10, 'a'*3, 20)
        Customer('a'*10, 'a'*30, 20)
        with self.assertRaises(ValueError):
            Customer('a'*10, 'a'*31, 20)

    def test_city_allowed_characters(self):
        Customer('a'*10, 'amnz ZNMA', 20)

    def test_city_forbidden_characters(self):
        for character in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                          '!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
                          '_', '=', '+', '/', '<', '>', '?', ';', '\'', '\\',
                          ':', '\"', '|', '[', ']', '{', '}', '`', '~']:
            with self.assertRaises(ValueError):
                Customer('a'*10, character*10, 20)
