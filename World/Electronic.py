class Electronic:
    def __init__(self):
        self.size = 1
        self.rad = 0
        self.vision = 0
        self.fuel = type("", (), dict(need=True, bank=100))()
        self.location = type("", (), dict(x=0, y=0))()

    def get_fuel_need(self):
        return self.fuel.need

    def get_fuel_bank(self):
        return self.fuel.bank

    def set_fuel_need(self, param):
        self.fuel.need = param

    def set_fuel_bank(self, param):
        self.fuel.bank = param

    def get_location_x(self):
        return self.location.x

    def get_location_y(self):
        return self.location.y

    def set_location_x(self, param):
        self.location.x = param

    def set_location_y(self, param):
        self.location.y = param
