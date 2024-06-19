import unittest
from calculadora import somar, subtrair

class TestaCalculatora(unittest.TestCase):
     def testa_soma(self):
        result = somar(2, 3)
        self.assertEqual(result, 5)

     def testa_subtrair(self):
        result = subtrair(5, 3)
        self.assertEqual(result, 2)

if __name__ == '__main__':
 unittest.main()
