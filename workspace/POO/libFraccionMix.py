from Fraccion import Fraccion

class FracMix(Fraccion):
    def __init__(self, ent, num=0,den=1):
        self.ent =ent
        super().__init__(num,den)

    def __str__(self):
        return str(self.ent)+super().__str__()
