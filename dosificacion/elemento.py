class Areas:
    def __init__(self, area_one: float, area_all: float):
        self.area_one = area_one
        self.area_all = area_all

    def areas(self):


class Medidas2D:
    def __init__(self, largo: float, ancho: float):
        self.largo = largo
        self.ancho = ancho


class Medidas3D(Medidas2D):
    def __init__(self, largo: float, ancho: float, alto: float):
        super().__init__(largo, ancho)
        self.alto = alto


class ElementoAbs:
    def __init__(self, name: str, units: int, areas: Areas):
        self.name = name
        self.units = units


class Elemento2D(ElementoAbs):
    def __init__(self, name: str, units: int, areas: Areas, medidas_2d: Medidas2D):
        super().__init__(name, units, areas)
        self.medidas_2d = medidas_2d


class Elemento3D(ElementoAbs):
    def __init__(self, name: str, units: int, areas: Areas, medidas_3d: Medidas3D):
        super().__init__(name, units, areas)
        self.medidas_3d = medidas_3d


class Mortero:
    def __init__(self, cemento: float, arena: float, agua: float):
        self.cemento = cemento
        self.arena = arena
        self.agua = agua


class Concreto(Mortero):
    def __init__(self, cemento: float, arena: float, grava: float, agua: float):
        super().__init__(cemento, arena, agua)
        self.grava = grava


class Pisos:
    def __init__(self, baldosas: float, area_baldosas: float, name_baldosa: str):
        self.baldosas = baldosas
        self.area_baldosas = area_baldosas
        self.name_baldosa = name_baldosa


class Elemento:
    def __init__(self):
        self.pisos = Pisos(0, 0, "")
