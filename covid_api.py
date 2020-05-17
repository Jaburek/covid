import requests
from flask import Flask, request, jsonify, send_from_directory

class Kraj:
    nakazeni_muzi = 0
    nakazene_zeny = 0
    muzi_vek = 0
    zeny_vek = 0

    def __init__(self, jmeno, kod):
        self.jmeno = jmeno
        self.kod = kod

    def pridat_nakazeneho(self, pohlavi, vek):
        if pohlavi == "M":
            self.nakazeni_muzi = self.nakazeni_muzi + 1
            self.muzi_vek = self.muzi_vek + vek
        elif pohlavi == "Z":
            self.nakazene_zeny = self.nakazene_zeny + 1
            self.zeny_vek = self.zeny_vek + vek

    def celkovy_pocet_nakazenych(self):
        pocet = {"Pocet nakazenych" : self.nakazeni_muzi + self.nakazene_zeny}
        return pocet

    def prumerny_vek(self):
        prumer_vek = {"Prumerny vek" : (self.muzi_vek + self.zeny_vek) / (self.nakazeni_muzi + self.nakazene_zeny)}
        return prumer_vek

    def podil_muzu(self):
        podil_m = {"Podil muzu" : self.nakazeni_muzi / (self.nakazeni_muzi + self.nakazene_zeny)}
        return podil_m

    def podil_zen(self):
        podil_z = {"Podil zen" : self.nakazene_zeny / (self.nakazeni_muzi + self.nakazene_zeny)}
        return podil_z

    def prum_vek_m(self):
        vek_m = {"Prumerny vek muzu" : self.muzi_vek / self.nakazeni_muzi}
        return vek_m
    def prum_vek_z(self):
        vek_z = {"Prumerny vek zen" : self.zeny_vek / self.nakazene_zeny}
        return vek_z

kraje = {
    "CZ010" : Kraj('Hlavní město Praha', 'CZ010'),
    "CZ020" : Kraj('Středočeský kraj', 'CZ020'),
    "CZ031" : Kraj('Jihočeský kraj', 'CZ031'),
    "CZ032" : Kraj('Plzeňský kraj', 'CZ032'),
    "CZ041" : Kraj('Karlovarský kraj', 'CZ041'),
    "CZ042" : Kraj('Ústecký kraj', 'CZ042'),
    "CZ051" : Kraj('Liberecký kraj', 'CZ051'),
    "CZ052" : Kraj('Královéhradecký kraj', 'CZ052'),
    "CZ053" : Kraj('Pardubický kraj', 'CZ053'),
    "CZ063" : Kraj('Kraj Vysočina', 'CZ063'),
    "CZ064" : Kraj('Jihomoravský kraj', 'CZ064'),
    "CZ071" : Kraj('Olomoucký kraj', 'CZ071'),
    "CZ072" : Kraj('Zlínský kraj', 'CZ072'),
    "CZ080" : Kraj('Moravskoslezský kraj', 'CZ080')
}

r = request.get("https://onemocneni-aktualne.mzcr.cz/api/v1/covid-19/osoby.json")
r = r.json()
for osoba in r:
    kraje["CZ010"].pridat_nakazeneho('pohlavi', 'vek'),
    kraje["CZ020"].pridat_nakazeneho('pohlavi', 'vek'),
    kraje["CZ031"].pridat_nakazeneho('pohlavi', 'vek'),
    kraje["CZ032"].pridat_nakazeneho('pohlavi', 'vek'),
    kraje["CZ041"].pridat_nakazeneho('pohlavi', 'vek'),
    kraje["CZ042"].pridat_nakazeneho('pohlavi', 'vek'),
    kraje["CZ051"].pridat_nakazeneho('pohlavi', 'vek'),
    kraje["CZ052"].pridat_nakazeneho('pohlavi', 'vek'),
    kraje["CZ053"].pridat_nakazeneho('pohlavi', 'vek'),
    kraje["CZ063"].pridat_nakazeneho('pohlavi', 'vek'),
    kraje["CZ064"].pridat_nakazeneho('pohlavi', 'vek'),
    kraje["CZ071"].pridat_nakazeneho('pohlavi', 'vek'),
    kraje["CZ072"].pridat_nakazeneho('pohlavi', 'vek'),
    kraje["CZ080"].pridat_nakazeneho('pohlavi', 'vek'),

app = Flask(__name__)
app.config['PROPAFATE_EXCEPTIONS'] = True

@app.route('/covid_kraje', methods=['GET'])
def covid_kraje():
    kraj = requests.args.get('kraj', '0')
    if not kraj in kraje:
        pass
    results = kraj[kraj].get_json()
    return jsonify(results)

@app.route('/covid_kraje', methods=['GET'])
def covid_kraje_geojson():
    features = []
    for kod, kraj in kraje.items():
        features.append({"type": "Features"})
        results = {"type": "FeaturesCollection", "features": features}
        return jsonify(results)

if __name__== "__main__":
    app.run(debug=True)