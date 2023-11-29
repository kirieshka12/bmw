class Bmw():
    def __init__(self, horse_power, color, model, weight, engine):
        self.horse_power = horse_power
        self.color = color
        self.weight = weight
        self.model = model
        self.engine = engine

    def sound(self):
        print('звучу')
    def drive(self):
        print('езжу')

m5_f90_lci = Bmw(horse_power = 625,color = 'Narda Gray', model = 'm5 F90 LCI', weight=1700, engine =4.4)
m5_f10_rest = Bmw(horse_power=510, color = 'white', model = 'M5 F10', weight=1600, engine = 4.4)
m5_e34 = Bmw(horse_power=360, color= 'violet', model = 'M5 E34', weight=1500, engine = 3.4)