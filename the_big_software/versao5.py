from enum import Enum

class InstrumentType(Enum):
    GUITAR = "Guitar"
    BANJO = "Banjo"
    DOBRO = "Dobro"
    FIDDLE = "Fiddle"
    BASS = "Bass"
    MANDOLIN = "Mandolin"
    SAX = "Sax"
    UNSPECIFIED = "Unspecified"

class Builder(Enum):
    FENDER = "fender"
    MARTIN = "martin"
    GIBSON = "gibson"
    COLLINGS = "collings"
    OLSON = "olson"
    RYAN = "ryan"
    PRS = "prs"
    ANY = "any"

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

class Type(Enum):
    ACOUSTIC = "acoustic"
    ELECTRIC = "electric"

class Style(Enum):
    A = "a"
    F = "f"

class Instrument:
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

class InstrumentSpec:
    def __init__(self, properties=None):
        if properties is None:
            self.properties = {}
        else:
            self.properties = properties.copy()

    def get_property(self, property_name):
        return self.properties.get(property_name)

    def get_properties(self):
        return self.properties

    def matches(self, other_spec):
        for property_name in other_spec.get_properties():
            if self.properties.get(property_name) != other_spec.get_property(property_name):
                return False
        return True

class Inventory:
    def __init__(self):
        self.inventory = []

    def add_instrument(self, serial_number, price, spec):
        instrument = Instrument(serial_number, price, spec)
        self.inventory.append(instrument)

    def get_instrument(self, serial_number):
        for instrument in self.inventory:
            if instrument.get_serial_number() == serial_number:
                return instrument
        return None

    def search(self, search_spec):
        matching_instruments = []
        for instrument in self.inventory:
            if instrument.get_spec().matches(search_spec):
                matching_instruments.append(instrument)
        return matching_instruments

def initialize_inventory(inventory):
    properties = {
        "instrumentType": InstrumentType.GUITAR.value,
        "builder": Builder.COLLINGS.value,
        "model": "CJ",
        "type": Type.ACOUSTIC.value,
        "numstrings": 6,
        "topwood": Wood.INDIAN_ROSEWOOD.value,
        "backwood": Wood.SITKA.value
    }
    inventory.add_instrument("11277", 3999.95, InstrumentSpec(properties))

    properties = {
        "instrumentType": InstrumentType.GUITAR.value,
        "builder": Builder.GIBSON.value,
        "model": "Les Paul",
        "type": Type.ELECTRIC.value,
        "numstrings": 6,
        "topwood": Wood.MAPLE.value,
        "backwood": Wood.MAPLE.value
    }
    inventory.add_instrument("70108276", 2295.95, InstrumentSpec(properties))

    properties = {
        "instrumentType": InstrumentType.MANDOLIN.value,
        "builder": Builder.GIBSON.value,
        "model": "F5-G",
        "type": Type.ACOUSTIC.value,
        "topwood": Wood.MAPLE.value,
        "backwood": Wood.MAPLE.value,
        "style": Style.A.value
    }
    inventory.add_instrument("9019920", 5495.99, InstrumentSpec(properties))

    properties = {
        "instrumentType": InstrumentType.BANJO.value,
        "builder": Builder.GIBSON.value,
        "model": "RB-3",
        "type": Type.ACOUSTIC.value,
        "numstrings": 5,
        "backwood": Wood.MAPLE.value
    }
    inventory.add_instrument("8900231", 2945.95, InstrumentSpec(properties))

def main():
    inventory = Inventory()
    initialize_inventory(inventory)
    client_spec = InstrumentSpec({
        "builder": Builder.GIBSON.value,
        "backwood": Wood.MAPLE.value
    })
    matching_instruments = inventory.search(client_spec)
    if matching_instruments:
        print("Talvez você goste desses instrumentos:")
        for instrument in matching_instruments:
            spec = instrument.get_spec()
            print(spec.get_property("instrumentType"), "com as seguintes propriedades:")
            for property_name, property_value in spec.get_properties().items():
                if property_name == "instrumentType":
                    continue
                print(property_name + ":", property_value)
            print("Ele pode ser seu por apenas $", instrument.get_price())
            print()
    else:
        print("Desculpe, não temos nada para você")

if __name__ == "__main__":
    main()