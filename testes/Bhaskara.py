import math

class Bhaskara:
    def delta(self, a, b, c):
        return b ** 2 - 4 * a * c

    def main(self):
        a_recebe = float(input('Digite o valor de A: '))
        b_recebe = float(input('Digite o valor de B: '))
        c_recebe = float(input('Digite o valor de C: '))
        print(self.calcula_raiz(a_recebe, b_recebe, c_recebe))

    def calcula_raiz(self, a, b, c):
        d = self.delta(a, b, c)
        if d == 0:
            raiz1 = (-b + math.sqrt(d)) / (2 * a)
            return 1, raiz1
        else:
            if d < 0:
                return 0
            else:
                raiz1 = (-b + math.sqrt(d)) / (2 * a)
                raiz2 = (-b - math.sqrt(d)) / (2 * a)
                return 2, raiz1, raiz2
