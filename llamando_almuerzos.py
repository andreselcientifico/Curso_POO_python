from herencia_almuerzos import Carta

class pedir(Carta):

    def __init__(self, almuerzo, incluye, grasa, salsa, principio):
        super().__init__(almuerzo, incluye, grasa, salsa, principio)
        


if __name__ == '__main__':
    almuerzo1 = pedir(True,False,True,True,True)
    print(almuerzo1.comida)

    almuerzo2 = pedir(True,True,True,True, False)
    print(almuerzo2.comida)

