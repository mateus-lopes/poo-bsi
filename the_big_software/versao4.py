from enum import Enum
from abc import ABC, abstractmethod

class Builder(Enum):
    FENDER = "fender"
    MARTIN = "martin"
    GIBSON = "gibson"
    COLLINGS = "collings"
    OLSON = "olson"
    RYAN = "ryan"
    PRS = "prs"
    ANY = "any"

    def toString(self):
        return self.value

class TypeG(Enum):
    ACOUSTIC = "acoustic"
    ELECTRIC = "electric"

    def toString(self):
        return self.value

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

    def toString(self):
        return self.value

class Style(Enum):
    A = "A"
    F = "F"

    def toString(self):
        return self.value

class InstrumentSpec:
    def __init__(self, builder, model, typeG, backWood, topWood):
        self.builder = builder
        self.model = model
        self.typeG = typeG
        self.backWood = backWood
        self.topWood = topWood

    def getBuilder(self):
        return self.builder

    def getModel(self):
        return self.model

    def getType(self):
        return self.typeG

    def getBackWood(self):
        return self.backWood

    def getTopWood(self):
        return self.topWood

    def matches(self, otherSpec):
        if self.builder != otherSpec.getBuilder():
            return False
        if self.model and self.model.lower() != otherSpec.getModel().lower():
            return False
        if self.typeG != otherSpec.getType():
            return False
        if self.backWood != otherSpec.getBackWood():
            return False
        if self.topWood != otherSpec.getTopWood():
            return False
        return True

class GuitarSpec(InstrumentSpec):
    def __init__(self, builder, model, typeG, backWood, topWood, numStrings):
        super().__init__(builder, model, typeG, backWood, topWood)
        self.numStrings = numStrings

    def getNumStrings(self):
        return self.numStrings

    def matches(self, otherSpec):
        if not isinstance(otherSpec, GuitarSpec):
            return False
        if not super().matches(otherSpec):
            return False
        if self.numStrings != otherSpec.getNumStrings():
            return False
        return True

class MandolinSpec(InstrumentSpec):
    def __init__(self, builder, model, typeG, backWood, topWood, style):
        super().__init__(builder, model, typeG, backWood, topWood)
        self.style = style

    def getStyle(self):
        return self.style

    def matches(self, otherSpec):
        if not isinstance(otherSpec, MandolinSpec):
            return False
        if not super().matches(otherSpec):
            return False
        if self.style != otherSpec.getStyle():
            return False
        return True

class Instrument(ABC):
    def __init__(self, serialNumber, price, spec):
        self.serialNumber = serialNumber
        self.price = price
        self.spec = spec

    def getSerialNumber(self):
        return self.serialNumber

    def getPrice(self):
        return self.price

    def setPrice(self, new_price):
        self.price = new_price

    def getSpec(self):
        return self.spec

class Guitar(Instrument):
    pass

class Mandolin(Instrument):
    pass

class Inventory:
    def __init__(self):
        self.instruments = []

    def addInstrument(self, serialNumber, price, spec):
        if isinstance(spec, GuitarSpec):
            instrument = Guitar(serialNumber, price, spec)
        elif isinstance(spec, MandolinSpec):
            instrument = Mandolin(serialNumber, price, spec)
        else:
            instrument = Instrument(serialNumber, price, spec)
        self.instruments.append(instrument)

    def getInstrument(self, serialNumber):
        for instrument in self.instruments:
            if instrument.getSerialNumber() == serialNumber:
                return instrument
        return None

    def search(self, searchSpec):
        matchingInstruments = []
        for instrument in self.instruments:
            if instrument.getSpec().matches(searchSpec):
                matchingInstruments.append(instrument)
        return matchingInstruments

def initializeInventory(inventory):
    spec1 = GuitarSpec(Builder.FENDER, "stratocastor", TypeG.ELECTRIC, Wood.ALDER, Wood.ALDER, 6)
    inventory.addInstrument("V95693", 1499.95, spec1)
    inventory.addInstrument("V99999", 1599.95, spec1)

def main():
    inventory = Inventory()
    initializeInventory(inventory)

    whatErinLikes = GuitarSpec(Builder.FENDER, "Stratocastor", TypeG.ELECTRIC, Wood.ALDER, Wood.ALDER, 6)
    matchingGuitars = inventory.search(whatErinLikes)

    if matchingGuitars:
        print("Erin, talvez você goste destes: ")
        for guitar in matchingGuitars:
            spec = guitar.getSpec()
            print(f"\nGuitar: {guitar.getSerialNumber()} {spec.getBuilder().toString()} {spec.getModel()} {spec.getType().toString()} guitar:\n{spec.getBackWood().toString()} na traseira e laterais,\n{spec.getTopWood().toString()} no tampo, com {spec.getNumStrings()} cordas\nEla pode ser sua por apenas US${guitar.getPrice():.2f}!")
    else:
        print("Desculpe Erin, não temos nada para você")

if __name__ == '__main__':
    main()
