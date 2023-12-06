import unittest
from unittest.mock import MagicMock

class Calculator:
    def add(self, a, b):
        # Una funzione complessa che vogliamo testare
        result = a + b
        return result

class TestCalculator(unittest.TestCase):
    def test_add_with_stub(self):
        # Stub: Sostituisci la funzione complessa con un risultato fisso
        calculator = Calculator()
        calculator.add = lambda x, y: 10  # Stub che restituisce sempre 10

        result = calculator.add(2, 3)
        self.assertEqual(result, 10)

    def test_add_with_mock(self):
        # Mock: Registra le chiamate e specifica il comportamento atteso
        calculator = Calculator()
        calculator.add = MagicMock(return_value=10)  # Mock che restituisce sempre 10

        result = calculator.add(2, 3)
        self.assertEqual(result, 10)

        # Verifica che il metodo sia stato chiamato con i parametri attesi
        calculator.add.assert_called_once_with(2, 3)

if __name__ == '__main__':
    unittest.main()
