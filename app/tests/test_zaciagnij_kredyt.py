import unittest

from ..Konto import Konto

imie = "dariusz"
nazwisko = "januszewski"
pesel = "65345678910"

class TestZaciagnijKredyt(unittest.TestCase):
    def test_liczba_transakcji_mniejsza_niz_3(self):
        konto1 = Konto(imie, nazwisko, pesel)
        konto1.historia = [2000]
        czy_przyznany1 = konto1.zaciagnij_kredyt(1000)
        self.assertFalse(czy_przyznany1, 'Kredyt został niesłusznie udzielony!')
        self.assertEqual(konto1.saldo, 0, 'Kwota została dodana do konta, a nie powinna!')

    def test_ostatnie_3_dodatnie_suma_5_mniejsza_od_kwoty(self):
        konto2 = Konto(imie, nazwisko, pesel)
        konto2.historia = [-100, 100, 100, 100, 100]
        czy_przyznany2 = konto2.zaciagnij_kredyt(1000)
        self.assertFalse(czy_przyznany2, 'Kredyt został niesłusznie odrzucony!')
        self.assertEqual(konto2.saldo, 0, 'Kwota nie została dodana do konta, a powinna!')

    def test_dokladnie_3_transakcje(self):
        konto1 = Konto(imie, nazwisko, pesel)
        konto1.historia = [100, 100, 100]
        czy_przyznany1 = konto1.zaciagnij_kredyt(300)
        self.assertTrue(czy_przyznany1, 'Kredyt został niesłusznie odrzucony!')
        self.assertEqual(konto1.saldo, 300, 'Kwota nie została dodana do konta, a powinna!')

    def test_suma_ostatnich_5_wieksza_od_kwoty(self):
        konto2 = Konto(imie, nazwisko, pesel)
        konto2.historia = [-100, 100, 100, 100]
        czy_przyznany2 = konto2.zaciagnij_kredyt(1000)
        self.assertTrue(czy_przyznany2, 'Kredyt został niesłusznie odrzucony!')
        self.assertEqual(konto2.saldo, 1000, 'Kwota nie została dodana do konta, a powinna!')

    def test_kredyt_ujemna_w_ostatnich_3(self):
        konto3 = Konto(imie, nazwisko, pesel)
        konto3.historia = [100, 100, -100, 100]
        czy_przyznany3 = konto3.zaciagnij_kredyt(100)
        self.assertTrue(czy_przyznany3, 'Kredyt został niesłusznie odrzucony!')
        self.assertEqual(konto3.saldo, 100, 'Kwota nie została dodana do konta, a powinna!')
