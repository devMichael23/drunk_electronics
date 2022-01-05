class Electronic:
    def __init__(self):
        self.size = 1
        self.rad = 0
        self.vision = -1
        self.fuel = {
            "need": False,
            "bank": 0
        }
        self.location = {
            "x": 0,
            "y": 0
        }

    def __int__(self, size, rad, vision, fuel_need, fuel_bank):
        self.size = size
        self.rad = rad
        self.vision = vision
        self.fuel = {
            "need": fuel_need,
            "bank": fuel_bank
        }
        self.location = {
            "x": 0,
            "y": 0
        }

    def move(self):
        #pass
        if self.fuel['need']:
            if self.fuel['bank'] > 0:
                self.fuel["bank"] = self.fuel["bank"] - 1
            else:
                exit(0)
