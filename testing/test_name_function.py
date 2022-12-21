import unittest
from name_funnction import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Тесты для 'name_function.py'."""
    def test_first_last_name(self):
        """Имена вида 'Janis Joplin' работают правильно?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

if __name__ == '__main__':
    unittest.__main__()