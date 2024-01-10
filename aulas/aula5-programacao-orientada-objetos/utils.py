def mostra_dobro(x):
    dobro = x*2
    print(f"O dobro de {x} é {dobro}")
    
class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura
        
    def perimetro(self):
        return 2 * self.base + self.altura
