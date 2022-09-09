#!/usr/bin/python3

class Suma:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2

    def mostrar_resultado(self):
        return self.n1 + self.n2

    def mostrar_operacion_completa(self):
        return str(self.n1) + ' + ' + str(self.n2) + ' = ' \
                + str(self.mostrar_resultado())


