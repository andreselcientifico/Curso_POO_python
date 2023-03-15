class plato:

    def __init__(self,proteina,carbohidrato,grasas, salsas):
        self._proteina = proteina
        self._carbohidrato = carbohidrato
        self._grasas = grasas
        self._salsas = salsas
        self._principio = None

    @property
    def almuerzo(self):
        if self._proteina and self._carbohidrato == False:
            print(f'{self._proteina and self._carbohidrato} un almuerzo contiene carbohidrato y proteina')
        else:
            f"{self._proteina and self._carbohidrato} es un Almuerzo"
        almuerzo = [self._proteina and self._carbohidrato]
        incluye = [f"Incluye alimentos basados en grasas: {self._grasas and self._salsas}"]
        principio = f"Este almuerzo contiene principio: {self._principio}" 
        return almuerzo, incluye, principio
    

    @almuerzo.setter
    def comida(self, almuerzo, incluye, principio):
        self.almuerzo = almuerzo
        self.incluye = incluye
        self.principio = principio

       


class Carta(plato):

    def __init__(self, almuerzo,incluye, grasa,salsa, principio):
        super().__init__(almuerzo, incluye,grasa,salsa)
        self._principio = principio
