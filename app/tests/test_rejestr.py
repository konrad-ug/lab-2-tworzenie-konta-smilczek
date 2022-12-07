import unittest
from parameterized import parameterized

from ..RejestrKont import RejestrKont
from ..Konto import Konto

imie = "dariusz"
nazwisko = "januszewski"
pesel = "65345678910"

imie2 = "Maciek"
nazwisko2 = "Kowalski"
pesel2 = "69345612377"

update_body = {
    "imie": "janusz",
    "nazwisko": "mickiewicz",
    "pesel": "66100987654",
    "saldo": 1000
}

class TestRejestr(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        RejestrKont.dodaj_konto(Konto(imie, nazwisko, pesel))
    
    @classmethod
    def tearDownClass(cls):
        RejestrKont.konta = []

    # def test_1_dodawanie_pierwszego_konta(self):
    #     konto = Konto(imie, nazwisko, pesel)
    #     RejestrKont.dodaj_konto(konto)
    #     self.assertEqual(RejestrKont.ile_kont(), 1)
        
    def test_2_dodawanie_duplikatu_konta(self):
        konto = Konto(imie, nazwisko, pesel)
        czy_dodane = RejestrKont.dodaj_konto(konto)
        self.assertEqual(czy_dodane, False)
        
    def test_3_szukanie_konta(self):
        konto = Konto(imie2, nazwisko2, pesel2)
        RejestrKont.dodaj_konto(konto)
        self.assertEqual(RejestrKont.wyszukaj_konto_z_peselem(pesel2), konto)
        
    def test_4_ile_kont(self):
        self.assertEqual(RejestrKont.ile_kont(), 2)
    
    def test_5_edycja_konta(self):
        konto = RejestrKont.wyszukaj_konto_z_peselem(pesel)
        RejestrKont.edytuj_konto(update_body, pesel)
        self.assertEqual(konto.imie, update_body["imie"])
        self.assertEqual(konto.nazwisko, update_body["nazwisko"])
        self.assertEqual(konto.pesel, update_body["pesel"])
        self.assertEqual(konto.saldo, update_body["saldo"])
        
    def test_6_usuwanie_konta(self):
        RejestrKont.usun_konto(pesel)
        RejestrKont.usun_konto(pesel)
        self.assertEqual(RejestrKont.wyszukaj_konto_z_peselem(pesel), None)
