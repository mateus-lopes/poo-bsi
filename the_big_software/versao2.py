from enum import Enum

class Builder(Enum):
    FENDER = "fender"
    MARTIN = "martin"
    GIBSON = "gibson"
    COLLINGS = "collings"
    OLSON = "olson"
    RYAN = "ryan"
    PRS = "prs"
    ANY = "any"

class TypeG(Enum):
    ACOUSTIC = "acoustic"
    ELECTRIC = "electric"

class Wood(Enum):
    INDIAN_ROSEWOOD = "indian_rosewood"
    BRAZILIAN_ROSEWOOD = "brazilian_rosewood"
    MAHOGANY = "mahogany"
    MAPLE = "maple"
    COCOBOLO = "cocobolo"
    CEDAR = "cedar"
    ADIRONDACK = "adirondack"
    ALDER = "alder"
    SITKA = "sitka"

class GuitarSpec:
    def __init__(self, builder, model, typeg, back_wood, top_wood):
        self.builder = builder
        self.model = model
        self.typeg = typeg
        self.back_wood = back_wood
        self.top_wood = top_wood

    def get_builder(self):
        return self.builder

    def get_model(self):
        return self.model

    def get_typeg(self):
        return self.typeg

    def get_back_wood(self):
        return self.back_wood

    def get_top_wood(self):
        return self.top_wood

    def matches(self, other_spec):
        if self.builder != other_spec.get_builder():
            return False

        model = other_spec.get_model().lower()
        if model and model != "" and model != self.model.lower():
            return False

        if self.typeg != other_spec.get_typeg():
            return False
        if self.back_wood != other_spec.get_back_wood():
            return False
        if self.top_wood != other_spec.get_top_wood():
            return False
        return True

class Guitar:
    def __init__(self, serial_number, price, spec):
        self.serial_number = serial_number
        self.price = price
        self.spec = spec

    def get_serial_number(self):
        return self.serial_number

    def get_price(self):
        return self.price

    def set_price(self, new_price):
        self.price = new_price

    def get_spec(self):
        return self.spec

class Inventory:
    def __init__(self):
        self.guitars = []

    def add_guitar(self, serial_number, price, builder, model, typeg, back_wood, top_wood):
        spec = GuitarSpec(builder, model, typeg, back_wood, top_wood)
        guitar = Guitar(serial_number, price, spec)
        self.guitars.append(guitar)

    def get_guitar(self, serial_number):
        for guitar in self.guitars:
            if guitar.get_serial_number() == serial_number:
                return guitar
        return None

    def search_guitar(self, search_spec):
        matching_guitars = []
        for guitar in self.guitars:
            if guitar.get_spec().matches(search_spec):
                matching_guitars.append(guitar)
        return matching_guitars

inventory = Inventory()

inventory.add_guitar("V95693", 1499.95, Builder.FENDER, "Stratocastor", TypeG.ELECTRIC, Wood.ALDER, Wood.ALDER)
inventory.add_guitar("11277", 3999.95, Builder.COLLINGS, "Stratocastor", TypeG.ACOUSTIC, Wood.INDIAN_ROSEWOOD, Wood.INDIAN_ROSEWOOD)

whatErinLikes = GuitarSpec(Builder.FENDER, "Stratocastor", TypeG.ELECTRIC, Wood.ALDER, Wood.ALDER)
matching_guitars = inventory.search_guitar(whatErinLikes)

if matching_guitars:
    for guitar in matching_guitars:
        spec = guitar.get_spec()
        print(f"Erin, talvez você goste desta: {spec.get_builder().value} {spec.get_model()} {spec.get_typeg().value} guitar:\n {spec.get_back_wood().value} na traseira e laterais, \n{spec.get_top_wood().value} no tampo.\n Ela pode ser sua por apenas US${guitar.get_price()}!")
else:
    print("Desculpe Erin, não temos nada para você")