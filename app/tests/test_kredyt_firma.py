import unittest
from parameterized import parameterized

from ..KontoFirmowe import KontoFirmowe

imie = "dariusz"
nazwisko = "januszewski"
pesel = "65345678910"
nazwa_firmy = "Paruwex sp. z o.o"
nip = "1234567890"
n_nip = "1234"


class TestKredytRefaktor(unittest.TestCase):

    def setUp(self):
        self.konto = KontoFirmowe(nazwa_firmy, nip)

    @parameterized.expand([
        ([100, 100, 1775], 500, 500, False, 500),
        ([-100, 100, -100, 100, 1000], 2000, 700, False, 2000),
        ([100, -1755], 500, 666, False, 500),
        ([-100, -1755, -100, 100, -1000], 2000, 1000, True, 3000),
        ([-100, 100, 100, 100, -600, 200], 500, False , 0),
    ])
    def test_zaciagnij_kredyt(self, historia, saldo, wnioskowana_kwota, oczekiwany_wynik_wniosku, oczekiwane_saldo):
        self.konto.historia = historia
        self.konto.saldo = saldo
        czy_przyznany = self.konto.zaciagnij_kredyt(wnioskowana_kwota)
        self.assertEqual(czy_przyznany, oczekiwany_wynik_wniosku)
        self.assertEqual(self.konto.saldo, oczekiwane_saldo)
