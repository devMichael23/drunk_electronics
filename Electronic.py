class Electronic:
    def __init__(self):
        self.size = 1
        self.rad = 0
        self.vision = 0
        self.fuel = type("", (), dict(need=True, bank=25))()
        self.location = type("", (), dict(x=0, y=0))()
