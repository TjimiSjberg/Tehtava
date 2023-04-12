import random

class Asiakas:
    """
    init(self, nimi, ika): tekee uuden olion Asikas nimen, asiakasnumeron ja iän avulla.
    luo_nro(self): Generoi uuden asiakasnumeron ja palauttaa sen.
    set_nimi(self, uusi_nimi): Antaa asiakkaan nimen uudeksi annetun nimen perusteella. Jos annettu nimi on tyhjä, tulee ValueError-poikkeuksen.
    """
    def __init__(self, nimi, ika):
        self.nimi = nimi
        self.asiakasnro = self.luo_nro()
        self.ika = ika

    def luo_nro(self):
        numero = random.randint(10**7, 10**8 - 1)
        numero_str = str(numero).zfill(8)
        return f"{numero_str[:2]}-{numero_str[2:5]}-{numero_str[5:]}"
    
    def set_nimi(self, uusi_nimi):
        if len(uusi_nimi) == 0:
            raise ValueError("Uusi nimi on annettava.")
        self.nimi = uusi_nimi

class Palvelu:
    """
    init(self, tuotenimi): Alustaa uuden Palvelu-olion tuotenimen ja asiakaslistan avulla.
    luo_asiakasrivi(self, asiakas): Muodostaa stringin, joka kuvaa annetun asiakkaan nimeä, asiakasnumeroa ja ikää.
    lisaa_asiakas(self, asiakas): Lisää asiakkas listalle. Jos asiakas on None, tulee ValueError-poikkeuksen.
    poista_asiakas(self, asiakas): Poistaa annetun asiakkaan listalta.
    tulosta_asiakkaat(self): Tulostaa kaikkien listassa olevien asiakkaiden tiedot.
    """
    def __init__(self, tuotenimi):
        self.tuotenimi = tuotenimi
        self.asiakkaat = []

    def luo_asiakasrivi(self, asiakas):
        return f"{asiakas.nimi} ({asiakas.asiakasnro}) on {asiakas.ika}-vuotias."

    def lisaa_asiakas(self, asiakas):
        if asiakas is None:
            raise ValueError("Asiakas on annettava.")
        self.asiakkaat.append(asiakas)

    def poista_asiakas(self, asiakas):
        self.asiakkaat.remove(asiakas)

    def tulosta_asiakkaat(self):
        print(f"\nTuotteen {self.tuotenimi} asiakkaat ovat:")
        for asiakas in self.asiakkaat:
            print(self.luo_asiakasrivi(asiakas))

class ParempiPalvelu(Palvelu):
    """
    init(self, tuotenimi): Luo uuden ParempiPalvelu-olion tuoteen, asiakaslistan ja etulistauksen avulla.
    lisaa_etu(self, etu): Lisää uuden edun etulistaukseen.
    poista_etu(self, etu): Poistaa annetun edun etulistauksesta, jossa se sijaitsee.
    tulosta_edut(self): Tulostaa kaikki etulistauksessa olevat edut.
    """
    def __init__(self, tuotenimi):
        super().__init__(tuotenimi)
        self.edut = []

    def lisaa_etu(self, etu):
        self.edut.append(etu)

    def poista_etu(self, etu):
        if etu in self.edut:
            self.edut.remove(etu)

    def tulosta_edut(self):
        print(f"\nTuotteen {self.tuotenimi} edut ovat:")
        for etu in self.edut:
            print(etu)
