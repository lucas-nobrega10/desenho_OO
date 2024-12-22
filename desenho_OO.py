import time
import turtle

class Forma:
    def __init__ (self, nome: str, cor: str, x: int, y: int) -> None:
       self.nome = nome
       self.cor = cor
       self.x = x
       self.y = y

    def iniciar_desenho(self):
        t = turtle.Turtle()
        t.up()
        t.setx(self.x)
        t.sety(self.y)
        t.down()
        t.fillcolor(self.cor)
        t.begin_fill()
        self.desenhar(t)
        t.end_fill()

    def desenhar(self, t: turtle.Turtle):
        raise Exception('Método abstrato.') 
    
class Quadrado(Forma):
    def __init__(self, lado: int, cor: str, x: int, y: int) -> None:
        super().__init__('Quadrado', cor, x, y)
        self.lado = lado
    
    def desenhar(self, t: turtle.Turtle):
        for _ in range (3):
            t.forward(self.lado)
            t.right(90)
        t.forward(self.lado)

class Triangulo(Forma):
    def __init__(self, tamanho: int, cor: str, x: int, y: int) -> None:
        super().__init__('Triângulo', cor, x, y)
        self.tamanho = tamanho

    def desenhar(self, t: turtle.Turtle): 
        for _ in range(3):
            t.left(120)
            t.forward(self.tamanho)

class Retangulo(Forma):
    def __init__(self, largura: int, altura: int, cor: str, x: int, y: int) -> None:
        super().__init__('Retângulo', cor, x, y)
        self.largura = largura
        self.altura = altura

    def desenhar(self, t: turtle.Turtle):
        for _ in range(2):
            for tam in [self.largura, self.altura]:
                t.forward(tam)
                t.right(90)

class Circulo(Forma):
    def __init__(self, raio: int, cor: str, x: int, y: int) -> None:
        super().__init__('Circulo', cor, x, y)
        self.raio = raio

    def desenhar(self, t: turtle.Turtle):
        t.left(180)
        t.circle(self.raio)

quad = Quadrado(200, 'red', -100, 0)
tri = Triangulo(200, 'yellow', 100, 0)
ret = Retangulo(50, 100, 'blue', -20, -100)
circ = Circulo(10, 'green', 50, -50)
circ2 = Circulo(10, 'green', -40, -50)

formas = [quad, tri, ret, circ, circ2]
for f in formas:
    f.iniciar_desenho()
time.sleep(10)