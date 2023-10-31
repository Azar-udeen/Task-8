#covert the UML diagram into a python class 



class TV:
    def _init_(self, brand, channel=1):
        self.brand = brand
        self.channel = channel if 1 <= channel <= 50 else 1
        self.price = None  # You can set the price separately
        self.inches = None  # You can set the inches separately
        self.volume = 50
        self.on = False

    def increase_volume(self):
        if self.volume < 100:
            self.volume += 1

    def decrease_volume(self):
        if self.volume > 0:
            self.volume -= 1

    def set_channel(self, channel):
        if 1 <= channel <= 50:
            self.channel = channel

    def reset_tv(self):
        self.channel = 1
        self.volume = 50

    def status(self):
        return f"{self.brand} at channel {self.channel}, volume {self.volume}"