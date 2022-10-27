import unittest

from ..KontoFirmowe import KontoFirmowe


nazwa_firmy = "Paruwex sp. z o.o"
nip = "1234567890"
class TestTworzenieKontaFirmowego(unittest.TestCase):
    def test_tworzenie_konta(self):
        pierwsze_konto = KontoFirmowe(nazwa_firmy, nip)
        self.assertEqual(pierwsze_konto.nazwa_firmy, nazwa_firmy, "Nazwa firmy nie została zapisana!")
        self.assertEqual(pierwsze_konto.nip, nip, "Nr NIP nie został zapisany!")
        self.assertEqual(pierwsze_konto.saldo, 0, "Saldo nie jest zerowe!")


