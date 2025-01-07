class Zutat:
    def __init__(self, name: str, kalorien: int, zeit: int):
        self.name = name
        self.kalorien_pro_100g = kalorien
        self.zubereitungszeit = zeit

    def __str__(self):
        return f"Zutat: {self.name}, Kalorien: {self.kalorien_pro_100g} kcal/100g, Zubereitungszeit: {self.zubereitungszeit} Minuten"


class Rezept:
    def __init__(self, name: str, beschreibung: str):
        self.name = name
        self.beschreibung = beschreibung
        self.zutatenliste = {}

    def zutat_hinzufuegen(self, zutat: Zutat, menge: str):
        self.zutatenliste[zutat] = menge

    def kalorien(self):
        gesamt_kalorien = 0
        for zutat, menge in self.zutatenliste.items():
            if menge.endswith("g"):
                menge_in_gramm = int(menge[:-1])
                gesamt_kalorien += (zutat.kalorien_pro_100g * menge_in_gramm) / 100
        print(f"Gesamtkalorien: {gesamt_kalorien:.2f} kcal")

    def kochzeit(self):
        max_zeit = max(
            [zutat.zubereitungszeit for zutat in self.zutatenliste], default=0
        )
        print(f"Maximale Kochzeit: {max_zeit} Minuten")

    def rezept_anzeigen(self):
        print(f"Rezept: {self.name}\n")
        for zutat, menge in self.zutatenliste.items():
            print(f"- {zutat.name}: {menge}")
        print(f"\nBeschreibung: {self.beschreibung}")


# Beispielrezept mit nem Tomatensalat :3
zutat1 = Zutat("Tomate", 18, 5)
zutat2 = Zutat("Zwiebel", 40, 3)
zutat3 = Zutat("Olivenöl", 884, 0)

rezept = Rezept(
    "Tomatensalat",
    "Ein erfrischender Salat mit Tomaten und Zwiebeln (Auch wenn Zwiebeln garstig sind)",
)
rezept.zutat_hinzufuegen(zutat1, "200g")
rezept.zutat_hinzufuegen(zutat2, "50g")
rezept.zutat_hinzufuegen(zutat3, "20g")

rezept.rezept_anzeigen()
rezept.kalorien()
rezept.kochzeit()
