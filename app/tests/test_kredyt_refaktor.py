import unittest
from parameterized import parameterized

from ..Konto import Konto

imie = "dariusz"
nazwisko = "januszewski"
pesel = "65345678910"


class TestKredytRefaktor(unittest.TestCase):

    def setUp(self):
        self.konto = Konto(imie, nazwisko, pesel)

    @parameterized.expand([
        ([100, 100, 100], 500, True, 500),
        ([-100, 100, -100, 100, 1000], 700, True, 700),
        ([-100, 20000, -100, 100, -1000], 1000, True, 1000),
        ([100], 666, False, 0),
        ([-100, 100, 100, 100, -600, 200], 500, False , 0),
    ])
    def test_zaciagnij_kredyt(self, historia, wnioskowana_kwota, oczekiwany_wynik_wniosku, oczekiwane_saldo):
        self.konto.historia = historia
        czy_przyznany = self.konto.zaciagnij_kredyt(wnioskowana_kwota)
        self.assertEqual(czy_przyznany, oczekiwany_wynik_wniosku)
        self.assertEqual(self.konto.saldo, oczekiwane_saldo)

# class TestZaciagnijKredyt(unittest.TestCase):
#     def test_liczba_transakcji_mniejsza_niz_3(self):
#         konto1 = Konto(imie, nazwisko, pesel)
#         konto1.historia = [2000]
#         czy_przyznany1 = konto1.zaciagnij_kredyt(1000)
#         self.assertFalse(czy_przyznany1, 'Kredyt został niesłusznie udzielony!')
#         self.assertEqual(konto1.saldo, 0, 'Kwota została dodana do konta, a nie powinna!')

#     def test_ostatnie_3_dodatnie_suma_5_mniejsza_od_kwoty(self):
#         konto2 = Konto(imie, nazwisko, pesel)
#         konto2.historia = [-100, 100, 100, 100, 100]
#         czy_przyznany2 = konto2.zaciagnij_kredyt(1000)
#         self.assertTrue(czy_przyznany2, 'Kredyt został niesłusznie odrzucony!')
#         self.assertEqual(konto2.saldo, 1000, 'Kwota nie została dodana do konta, a powinna!')

#     def test_dokladnie_3_transakcje(self):
#         konto1 = Konto(imie, nazwisko, pesel)
#         konto1.historia = [100, 100, 100]
#         czy_przyznany1 = konto1.zaciagnij_kredyt(300)
#         self.assertTrue(czy_przyznany1, 'Kredyt został niesłusznie odrzucony!')
#         self.assertEqual(konto1.saldo, 300, 'Kwota nie została dodana do konta, a powinna!')

#     def test_kredyt_ujemna_w_ostatnich_3(self):
#         konto2 = Konto(imie, nazwisko, pesel)
#         konto2.historia = [100, 100, -100, 100]
#         czy_przyznany2 = konto2.zaciagnij_kredyt(200)
#         self.assertTrue(czy_przyznany2, 'Kredyt został niesłusznie odrzucony!')
#         self.assertEqual(konto2.saldo, 200, 'Kwota nie została dodana do konta, a powinna!')

#     def test_suma_ostatnich_5_wieksza_od_kwoty_ujemna_ostatnie_3(self):
#         konto3 = Konto(imie, nazwisko, pesel)
#         konto3.historia = [100, 100, -100, 100]
#         czy_przyznany3 = konto3.zaciagnij_kredyt(1000)
#         self.assertFalse(czy_przyznany3, 'Kredyt został niesłusznie udzielony!')
#         self.assertEqual(konto3.saldo, 0, 'Kwota została dodana do konta, a nie powinna!')
