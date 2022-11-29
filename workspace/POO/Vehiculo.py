class Vehiculo():
    def __init__(self,color,ruedas):
        self.color = color
        self.ruedas = ruedas
    def __str__(self):
        return "Color {},{} ruedas".format(self.color,self.ruedas)

class Coche(Vehiculo):

    def __init__(self, color, ruedas,velocidad,cilindrada):
        Vehiculo.__init__(self,color,ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    def __str__(self):
        cad = "color{},{}km/h,{}ruedas,{}cc"
        return cad.format(self.color,self.velocidad,self.ruedas, self.cilindrada)


x = Vehiculo("azul",4)
print(x)

y = Coche("verde",5,12,20)

print(y)
