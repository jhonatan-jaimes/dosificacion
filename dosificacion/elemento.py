from typing import Dict


class Areas:
    def __init__(self, area_one: float, area_all: float):
        self.area_one = area_one
        self.area_all = area_all

    def json(self):
        areas = {
            "areaUnidad": self.area_one,
            "areaTotal": self.area_all
        }
        return areas


class Medidas2D:
    def __init__(self, largo: float, ancho: float):
        self.largo = largo
        self.ancho = ancho

    def json(self):
        medidas_2d = {
            "largo": self.largo,
            "ancho": self.ancho
        }
        return medidas_2d


class Medidas3D(Medidas2D):
    def __init__(self, largo: float, ancho: float, alto: float):
        super().__init__(largo, ancho)
        self.alto = alto

    def json(self):
        medidas_3d = {
            "largo": self.largo,
            "ancho": self.ancho,
            "alto": self.alto
        }
        return medidas_3d


class ElementoAbs:
    def __init__(self, name: str, units: int, areas: Areas):
        self.name = name
        self.units = units
        self.areas = areas


class Elemento2D(ElementoAbs):
    def __init__(self, name: str, units: int, areas: Areas, medidas_2d: Medidas2D):
        super().__init__(name, units, areas)
        self.medidas_2d = medidas_2d

    def json(self):
        elemento_2d = {
            "nombre": self.name,
            "cantidad": self.units,
            "medidas": self.medidas_2d.json(),
            "areas": self.areas.json()
        }
        return elemento_2d


class Elemento3D(ElementoAbs):
    def __init__(self, name: str, units: int, areas: Areas, medidas_3d: Medidas3D):
        super().__init__(name, units, areas)
        self.medidas_3d = medidas_3d

    def json(self):
        return {
            "nombre": self.name,
            "cantidad": self.units,
            "medidas": self.medidas_3d.json(),
            "areas": self.areas.json()
        }


class Mortero:
    def __init__(self, cemento: float, arena: float, agua: float):
        self.cemento = cemento
        self.arena = arena
        self.agua = agua


class Concreto(Mortero):
    def __init__(self, cemento: float, arena: float, grava: float, agua: float):
        super().__init__(cemento, arena, agua)
        self.grava = grava

    def json(self) -> Dict[str, float]:
        return {
            "cemento": self.cemento,
            "arena": self.arena,
            "grava": self.grava,
            "agua": self.agua
        }


class Pisos:
    def __init__(self, baldosas: float, area_baldosas: float, name_baldosa: str):
        self.baldosas = baldosas
        self.area_baldosas = area_baldosas
        self.name_baldosa = name_baldosa


class Elemento:
    def __init__(self):
        self.pisos = Pisos(0, 0, "")
