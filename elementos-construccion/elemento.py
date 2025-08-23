from decimal import Decimal as dec


class Error:
    def __init__(self):
        self.error = None


class Areas:
    def __init__(self, area_one: float = 0.0, area_all: float = 0.0):
        self.area_one = area_one
        self.area_all = area_all

    def json(self):
        areas = {
            "areaUnidad": self.area_one,
            "areaTotal": self.area_all
        }
        return areas


class Medidas2D:
    def __init__(self, largo: float = 0.0, ancho: float = 0.0):
        self.largo = largo
        self.ancho = ancho

    def area(self):
        return float(round(dec(self.largo) * dec(self.ancho), 2))

    def json(self):
        medidas_2d = {
            "largo": self.largo,
            "ancho": self.ancho
        }
        return medidas_2d


class Medidas3D(Medidas2D):
    def __init__(self, largo: float = 0.0, ancho: float = 0.0, alto: float = 0.0):
        super().__init__(largo, ancho)
        self.alto = alto

    def area(self):
        return float(round(dec(super().area()) * dec(self.alto), 2))

    def json(self):
        medidas_3d = {
            "largo": self.largo,
            "ancho": self.ancho,
            "alto": self.alto
        }
        return medidas_3d


class Mortero(Error):
    def __init__(self, cemento: float = 0.0, arena: float = 0.0, agua: float = 0.0):
        super().__init__()
        self.cemento = cemento
        self.arena = arena
        self.agua = agua

    def json(self):
        if self.error is None:
            return {
                "cemento": self.cemento,
                "arena": self.arena,
                "agua": self.agua
            }
        else:
            return {
                "error": self.error
            }


class Concreto(Mortero):
    def __init__(self, cemento: float = 0.0, arena: float = 0.0, grava: float = 0.0,
                 agua: float = 0.0):
        super().__init__(cemento, arena, agua)
        self.grava = grava

    def json(self):
        if self.error is None:
            return {
                "cemento": self.cemento,
                "arena": self.arena,
                "grava": self.grava,
                "agua": self.agua
            }
        else:
            return {
                "error": self.error
            }


class Baldosas:
    def __init__(self, area_piso: float = 0.0, baldosas: float = 0.0, area_baldosas: float = 0.0):
        self.area_piso = area_piso
        self.baldosas = baldosas
        self.area_baldosas = area_baldosas


class Elemento(Error):
    def __init__(self, name: str = "", units: int = 0, areas: Areas = None):
        super().__init__()
        self.name = name
        self.units = units
        self.areas = areas


class Elemento2D(Elemento):
    def __init__(self, name: str = "", units: int = 0,
                 areas: Areas = None, medidas_2d: Medidas2D = None):
        super().__init__(name, units, areas)
        self.medidas_2d = medidas_2d

    def json(self):
        return {
            "nombre": self.name,
            "cantidad": self.units,
            "medidas": self.medidas_2d.json(),
            "areas": self.areas.json()
        }


class Elemento3D(Elemento):
    def __init__(self, name: str = "", units: int = 0,
                 areas: Areas = None, medidas_3d: Medidas3D = None,
                 concreto: Concreto = None, mortero: Mortero = None):
        super().__init__(name, units, areas)
        self.concreto = concreto
        self.mortero = mortero
        self.medidas_3d = medidas_3d

    def json(self):
        return {
            "nombre": self.name,
            "cantidad": self.units,
            "medidas": self.medidas_3d.json(),
            "areas": self.areas.json(),
            "concreto": self.concreto.json()
        }


# Instanciacion de todas las clases de la clase elemento
concreto = Concreto()
