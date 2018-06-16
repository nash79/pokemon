import requests
import os.path
from bs4 import BeautifulSoup


class ExtractWEB(object):
    def __init__(self, filename, url):
        if os.path.exists(filename):
            fichier = open(filename, "r")
            html = fichier.read()
            fichier.close()
        else:
            response = requests.get(url)
            html = str(response.content)
            fichier = open(filename, "w")
            fichier.write(html)
            fichier.close()
        self.soup = BeautifulSoup(html, "html.parser")

    def extracttypefromhtml(self):
        ligne = []
        tab = self.soup.find(id="filter-pkmn-type")
        for v in tab.find_all("option"):
            ligne.append(v.text)
        del (ligne[0])
        return ligne

    def extractpokemonfromhtml(self):
        tableau = []
        tab = self.soup.find(id="pokedex")
        for link in tab.find_all("tr"):
            lstcolonne = []
            indexcolonne = 0
            for v in link.find_all("td"):
                if indexcolonne == 0:
                    lstcolonne.append(v.text)

                kk = []
                if indexcolonne == 1:
                    for b in v.find_all("a"):
                        kk.append(b.text)
                    for b in v.find_all("small"):
                        kk.append(b.text)
                    lstcolonne.append(kk)

                fg = []
                if indexcolonne == 2:
                    for c in v.find_all("a"):
                        fg.append(c.text)
                    lstcolonne.append(fg)

                if indexcolonne == 3:
                    lstcolonne.append(v.text)
                if indexcolonne == 4:
                    lstcolonne.append(v.text)
                if indexcolonne == 5:
                    lstcolonne.append(v.text)
                if indexcolonne == 6:
                    lstcolonne.append(v.text)
                if indexcolonne == 7:
                    lstcolonne.append(v.text)
                if indexcolonne == 8:
                    lstcolonne.append(v.text)
                if indexcolonne == 9:
                    lstcolonne.append(v.text)

                indexcolonne = indexcolonne + 1

                if indexcolonne == 9:
                    indexcolonne = 0

            tableau.append(lstcolonne)
        del (tableau[0])
        return tableau
