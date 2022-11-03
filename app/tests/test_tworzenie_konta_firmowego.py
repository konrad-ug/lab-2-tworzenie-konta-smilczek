import unittest

from ..KontoFirmowe import KontoFirmowe


nazwa_firmy = "Paruwex sp. z o.o"
nip = "1234567890"
n_nip = "1234"
class TestTworzenieKontaFirmowego(unittest.TestCase):
    def test_tworzenie_konta(self):
        pierwsze_konto = KontoFirmowe(nazwa_firmy, nip)
        self.assertEqual(pierwsze_konto.nazwa_firmy, nazwa_firmy, "Nazwa firmy nie została zapisana!")
        self.assertEqual(pierwsze_konto.nip, nip, "Nr NIP nie został zapisany!")
        self.assertEqual(pierwsze_konto.saldo, 0, "Saldo nie jest zerowe!")

    def test_niepoprawny_nip(self):
        piewrsze_konto = KontoFirmowe(nazwa_firmy, n_nip)
        self.assertEqual(piewrsze_konto.nip, "Niepoprawny NIP!", "NIP nie został poprawnie sprawdzony!")

    def test_udany_przelew_wychodzacy(self):
        konto = KontoFirmowe(nazwa_firmy, nip)
        konto.saldo = 1000
        konto.zaksieguj_przelew_wychodzacy(1000)
        self.assertEqual(konto.saldo, 0, "Przelew wychadzacy nie został zaksięgowany!")

    def test_udany_przelew_przychodzacy(self):
        konto = KontoFirmowe(nazwa_firmy, nip)
        konto.saldo = 0
        konto.zaksieguj_przelew_przychodzacy(1000)
        self.assertEqual(konto.saldo, 1000, "Przelew przychodzący nie został zaksięgowany!")
