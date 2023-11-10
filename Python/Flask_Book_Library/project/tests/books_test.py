from project.books.models import Book
import unittest


class TestBookCreation(unittest.TestCase):
    def test_name_length(self):
        with self.assertRaises(ValueError):
            Book('a'*2, 'a'*10, 2000, '2days')
        Book('a'*3, 'a'*10, 2000, '2days')
        Book('a'*50, 'a'*10, 2000, '2days')
        with self.assertRaises(ValueError):
            Book('a'*51, 'a'*10, 2000, '2days')

    def test_name_allowed_characters(self):
        Book('amnz-ZNMA: bcCB,qUd', 'a'*10, 2000, '2days')

    def test_name_forbidden_characters(self):
        for character in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                          '!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
                          '_', '=', '+', '.', '/', '<', '>', '?', ';', '\'',
                          '\\', '\"', '|', '[', ']', '{', '}', '`', '~']:
            with self.assertRaises(ValueError):
                Book(character*10, 'a'*10, 2000, '2days')

    def test_author_length(self):
        with self.assertRaises(ValueError):
            Book('a'*10, 'a'*2, 2000, '2days')
        Book('a'*10, 'a'*3, 2000, '2days')
        Book('a'*10, 'a'*40, 2000, '2days')
        with self.assertRaises(ValueError):
            Book('a'*10, 'a'*41, 2000, '2days')

    def test_author_allowed_characters(self):
        Book('a'*10, 'amnz ZNMA', 2000, '2days')

    def test_author_forbidden_characters(self):
        for character in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                          '!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
                          '-', '_', '=', '+', ',', '.', '/', '<', '>', '?',
                          ';', '\'', '\\', ':', '\"', '|', '[', ']', '{', '}',
                          '`', '~']:
            with self.assertRaises(ValueError):
                Book('a'*10, character*10, 2000, '2days')
