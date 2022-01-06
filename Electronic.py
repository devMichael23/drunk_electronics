class Electronic:
    def __init__(self):
        self.size = 1
        self.rad = 0
        self.vision = 0
        self.fuel = {
            "need": True,
            "bank": 25
        }
        self.location = {
            "x": 0,
            "y": 0
        }

    def move(self, x, y):
        if self.fuel['need']:
            if self.fuel['bank'] > 0:
                self.fuel["bank"] = self.fuel["bank"] - 1
            else:
                exit(0)
        self.location = {
            'x': x,
            'y': y
        }
