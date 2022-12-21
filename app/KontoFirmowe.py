from app.Konto import Konto
from datetime import date
import os
import requests


class KontoFirmowe(Konto):
    def __init__(self, nazwa_firmy, nip):
        self.nip = nip if self.zapytaj_o_nip(nip) else "Pranie!"
        self.nazwa_firmy = nazwa_firmy
        self.saldo = 0
        self.oplata_za_ekspres = 5
        self.historia = []

    def czy_poprawny_nip(self, nip):
        return len(nip) == 10
    
    def zapytaj_o_nip(self, nip):
        url = os.environ('BANK_APP_MF_URL')
        date = date.today().strftime("%Y-%m-%d")
        response = requests.get(url + nip, json={"date": date})
        return response.status_code == 200

    def kredyt_zasluzony(self, kwota):
        if -1755 in self.historia:
            if self.saldo >= kwota * 2:
                return True
        return False
    
    def zaciagnij_kredyt(self, kwota):
        if self.kredyt_zasluzony(kwota):
            self.saldo += kwota
            return True
        return False