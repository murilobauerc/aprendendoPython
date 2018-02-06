import unittest
from jokenpo import jokenpo
class TestJokenpo(unittest.TestCase):
    def test_ao_receber_pedra_e_pedra_retorna_empate(self):
        resultado = jokenpo("pedra", "pedra")
        self.assertEqual(resultado, "empate")

    def test_ao_receber_papel_e_pedra_retorna_papel(self):
        resultado = jokenpo("papel", "pedra")
        self.assertEqual(resultado, "papel")



unittest.main()
