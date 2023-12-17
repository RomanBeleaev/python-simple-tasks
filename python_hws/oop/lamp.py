class Lamp:
    def __init__(self, power):
        self.power = power
    def on(self):
        print("#" * self.power + "-" * (10 - self.power))
    def off(self):
        print("-" * 10)

smallLamp = Lamp(1)
mediumLamp = Lamp(5)
bigLamp = Lamp(10)

smallLamp.on()
mediumLamp.off()
bigLamp.on()