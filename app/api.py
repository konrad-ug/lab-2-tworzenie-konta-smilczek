from flask import Flask, request, jsonify
from app.RejestrKont import RejestrKont
from app.Konto import Konto

app = Flask(__name__)

@app.route("/konta/stworz_konto", methods=['POST'])
def stworz_konto():
    dane = request.get_json()
    print(f"Request o stworzenie konta z danymi: {dane}")
    konto = Konto(dane['imie'], dane['nazwisko'], dane['pesel'])
    RejestrKont.dodaj_konto(konto)
    return jsonify("Konto stworzone"), 201

@app.route("/konta/ile_kont", methods=['GET'])
def ile_kont():
    print("Request o podanie liczby kont")
    liczba_kont = RejestrKont.ile_kont()
    return jsonify(liczba_kont), 200

@app.route("/konta/konto/<pesel>", methods=['GET'])
def wyszukaj_konto_z_peselem(pesel):
    print("Request o wyszukanie konta po numerze pesel")
    konto = RejestrKont.wyszukaj_konto_z_peselem(pesel)
    return jsonify(
        imie=konto.imie,
        nazwisko=konto.nazwisko,
        pesel=konto.pesel,
        saldo=konto.saldo,
        historia=konto.historia
    ), 200

@app.route("/konta/konto/<pesel>", methods=['PUT'])
def aktualizuj_konto_z_peselem(pesel):
    dane = request.get_json()
    print(f"Request o edycję konta z numerem pesel {pesel}")
    konto = RejestrKont.wyszukaj_konto_z_peselem(pesel)
    if (dane['imie']):
        konto.imie = dane['imie']
    if (dane['nazwisko']):
        konto.imie = dane['nazwisko']