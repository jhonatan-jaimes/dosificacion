from decimal import Decimal as dec
from elemento import Medidas3D, Areas, Medidas2D


def calcular_3d(medidas: Medidas3D):
    return float(round(dec(medidas.largo) * dec(medidas.ancho) * dec(medidas.alto)))


def calcular_2d(medidas: Medidas2D):
    return float(round(dec(medidas.largo) * dec(medidas.ancho)))


class Calcular:
    def __init__(self):
        self.area = Areas()

    def calcular_areas_3d(self, medidas: Medidas3D, cantidad: int):
        self.area.area_one = calcular_3d(medidas)
        self.area.area_all = self.area.area_one * cantidad
        return self.area

    def calcular_areas_2d(self, medidas: Medidas2D, cantidad: int):
        self.area.area_one = calcular_2d(medidas)
        self.area.area_all = self.area.area_one * cantidad
        return self.area
