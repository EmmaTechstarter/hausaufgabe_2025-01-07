class Zutat:
    def __init__(self, name: str, kalorien: int, zeit: int):
        self.name = name
        self.kalorien_pro_100g = kalorien
        self.zubereitungszeit = zeit

    def __str__(self):
        return f"Zutat: {self.name}, Kalorien: {self.kalorien_pro_100g} kcal/100g, Zubereitungszeit: {self.zubereitungszeit} Minuten"
