from flask import Flask, request, jsonify
from app.RejestrKont import RejestrKont
from app.Konto import Konto

app = Flask(__name__)

@app.route("/konta/stworz_konto", methods=['POST'])
def stworz_konto():
    dane = request.get_json()
    print(f"Request o stworzenie konta z danymi: {dane}")
    konto = Konto(dane['imie'], dane['nazwisko'], dane['pesel'])
    if RejestrKont.dodaj_konto(konto):
        return jsonify("Konto stworzone"), 201
    else:
        return jsonify("Konto już istnieje"), 400

@app.route("/konta/ile_kont", methods=['GET'])
def ile_kont():
    print("Request o podanie liczby kont")
    liczba_kont = RejestrKont.ile_kont()
    return jsonify(liczba_kont), 200

@app.route("/konta/konto/<pesel>", methods=['GET'])
def wyszukaj_konto_z_peselem(pesel):
    print("Request o wyszukanie konta po numerze pesel")
    konto = RejestrKont.wyszukaj_konto_z_peselem(pesel)
    if not konto: 
        return jsonify("Konto nie istnieje"), 404
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
    konto = RejestrKont.edytuj_konto(dane, pesel)
    return jsonify("Konto zaktualizowane"), 200

@app.route("/konta/konto/<pesel>", methods=['DELETE'])
def usun_konto(pesel):
    print(f"Request o usunięcie konta z numerem pesel {pesel}")
    RejestrKont.usun_konto(pesel)
    return jsonify("Konto usuniete"), 202