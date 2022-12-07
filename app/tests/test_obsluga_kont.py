import unittest
import requests
from parameterized import parameterized

from ..RejestrKont import RejestrKont
from ..Konto import Konto

class TestObslugaKont(unittest.TestCase):
    body = {
        "imie": "maciej",
        "nazwisko": "kowalski",
        "pesel": "70345678910"
    }
    update_body = {
        "imie": "janusz",
        "nazwisko": "mickiewicz",
        "pesel": "66100987654",
        "saldo": 1000
    }
    
    url = "http://localhost:5000"
    
    def test_1_tworzenie_kont_poprawne(self):
        create_resp = requests.post(self.url + "/konta/stworz_konto", json=self.body)
        self.assertEqual(create_resp.status_code, 201)
        
    def test_2_get_po_peselu(self):
        get_resp = requests.get(self.url + f"/konta/konto/{self.body['pesel']}")
        self.assertEqual(get_resp.status_code, 200)
        resp_body = get_resp.json()
        self.assertEqual(resp_body['imie'], self.body['imie'])
        self.assertEqual(resp_body["nazwisko"], self.body['nazwisko'])
        self.assertEqual(resp_body["saldo"], 0)
        
    # def test_3_ile_kont(self):
    #     get_resp = requests.get(self.url + "/konta/ile_kont")
    #     self.assertEqual(get_resp.status_code, 200)
    #     resp_body = get_resp.json()
    #     self.assertEqual(resp_body, 1)
    
    def test_4_put_po_peselu(self):
        put_resp = requests.put(self.url + f"/konta/konto/{self.body['pesel']}", json=self.update_body)
        self.assertEqual(put_resp.status_code, 200)
        get_resp = requests.get(self.url + f"/konta/konto/{self.update_body['pesel']}")
        resp_body = get_resp.json()
        self.assertEqual(resp_body["imie"], self.update_body["imie"])
        self.assertEqual(resp_body["nazwisko"], self.update_body['nazwisko'])
        self.assertEqual(resp_body["pesel"], self.update_body['pesel'])
        self.assertEqual(resp_body["saldo"], self.update_body['saldo'])
        
    def test_5_delete_po_peselu(self):
        requests.post(self.url + "/konta/stworz_konto", json=self.body)
        delete_resp = requests.delete(self.url + f"/konta/konto/{self.body['pesel']}")
        self.assertEqual(delete_resp.status_code, 202)
        get_resp = requests.get(self.url + f"/konta/konto/{self.body['pesel']}")
        resp_body = get_resp.json()
        self.assertEqual(resp_body, "Konto nie istnieje")
