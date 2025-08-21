from decimal import Decimal as dec

from elemento import Mortero, Concreto, Baldosas, Medidas3D, Medidas2D


class Dosificacion:
    def __init__(self):
        self.dosificacion_concreto = {
            ("122", "280", "4000", "27"): {"cemento": "420", "arena": "0.67", "grava": "0.67", "agua": "190"},
            ("122.5", "240", "3555", "24"): {"cemento": "380", "arena": "0.60", "grava": "0.76", "agua": "180"},
            ("123", "226", "3224", "22"): {"cemento": "350", "arena": "0.55", "grava": "0.84", "agua": "170"},
            ("123.5", "210", "3000", "20"): {"cemento": "320", "arena": "0.52", "grava": "0.90", "agua": "170"},
            ("124", "200", "2850", "19"): {"cemento": "300", "arena": "0.48", "grava": "0.95", "agua": "158"},
            ("124.5", "189", "2700", "18"): {"cemento": "280", "arena": "0.55", "grava": "0.89", "agua": "158"},
            ("133", "168", "2400", "16"): {"cemento": "300", "arena": "0.72", "grava": "0.72", "agua": "158"},
            ("134", "159", "2275", "15"): {"cemento": "260", "arena": "0.63", "grava": "0.83", "agua": "163"},
            ("135", "140", "2000", "14"): {"cemento": "230", "arena": "0.55", "grava": "0.92", "agua": "148"},
            ("136", "119", "1700", "12"): {"cemento": "210", "arena": "0.50", "grava": "1.00", "agua": "143"},
            ("147", "109", "1560", "11"): {"cemento": "175", "arena": "0.55", "grava": "0.98", "agua": "133"},
            ("148", "99", "1420", "10"): {"cemento": "160", "arena": "0.55", "grava": "1.03", "agua": "125"}
        }

        self.dosificacion_mortero = {
            ("12", "310", "4400", "30"): {"cemento": "525", "arena": "0.97", "agua": "230"},
            ("13", "280", "3980", "27"): {"cemento": "450", "arena": "1.10", "agua": "210"},
            ("14", "240", "3400", "23"): {"cemento": "375", "arena": "1.16", "agua": "200"},
            ("15", "200", "2850", "19"): {"cemento": "300", "arena": "1.18", "agua": "180"},
            ("16", "160", "2275", "16"): {"cemento": "275", "arena": "1.20", "agua": "180"},
        }

        self.elemento_mortero = Mortero()

        self.elemento_concreto = Concreto()

    def concreto(self, area: float, dosificacion_tipo: str):
        if area is None:
            self.elemento_concreto.error = "El area es no puede ser nula"
            return self.elemento_concreto
        elif area <= 0:
            self.elemento_concreto.error = f"El area no puede ser negativo (-1) ni cero (0), {area}"
            return self.elemento_concreto

        objeto_dosificacion = None

        for clave in self.dosificacion_concreto:
            if dosificacion_tipo in clave:
                objeto_dosificacion = self.dosificacion_concreto[clave]
                break

        if objeto_dosificacion is None:
            self.elemento_concreto.error = f"dosificacion no encontrada, {dosificacion_tipo}"
            return self.elemento_concreto

        self.elemento_concreto.cemento = float(round(dec(area) * dec(objeto_dosificacion["cemento"]), 2))
        self.elemento_concreto.arena = float(round(dec(area) * dec(objeto_dosificacion["arena"]), 2))
        self.elemento_concreto.grava = float(round(dec(area) * dec(objeto_dosificacion["grava"]), 2))
        self.elemento_concreto.agua = float(round(dec(area) * dec(objeto_dosificacion["agua"]), 2))

        return self.elemento_concreto

    def mortero(self, area: float, dosificacion_tipo: str):
        if area is None:
            self.elemento_mortero.error = "El area es no puede ser nula"
            return self.elemento_mortero
        elif area <= 0:
            self.elemento_mortero.error = f"El area no puede ser negativo (-1) ni cero (0), {area}"
            return self.elemento_mortero

        objeto_dosificacion = None

        for i in self.dosificacion_mortero:
            if dosificacion_tipo in i:
                objeto_dosificacion = self.dosificacion_mortero[i]

        if objeto_dosificacion is None:
            self.elemento_mortero.error = f"dosificacion no encontrada, {dosificacion_tipo}"
            return self.elemento_mortero

        self.elemento_mortero.cemento = float(round(dec(area) * dec(objeto_dosificacion["cemento"]), 2))
        self.elemento_mortero.arena = float(round(dec(area) * dec(objeto_dosificacion["arena"]), 2))
        self.elemento_mortero.agua = float(round(dec(area) * dec(objeto_dosificacion["agua"]), 2))

        return self.elemento_mortero


def area_2d(medidas_2d: Medidas2D):
    return float(round(dec(medidas_2d.largo) * dec(medidas_2d.ancho), 2))


class Prefabricado:
    def __init__(self):
        self.ceramica_simetrica = {
            ("10x10", "10"): .0100, ("15x15", "15"): .0225, ("20x20", "20"): .0400, ("25x25", "25"): .0625,
            ("30x30", "30"): .0900, ("35x35", "35"): .1225, ("40x40", "40"): .1600, ("45x45", "45"): .2025,
            ("50x50", "50"): .2500, ("55x55", "55"): .3025, ("60x60", "60"): .3600, ("65x65", "65"): .4225,
            ("70x70", "70"): .4900, ("75x75", "75"): .5625, ("80x80", "80"): .6400, ("85x85", "85"): .7225,
            ("90x90", "90"): .8100, ("95x95", "95"): .9025, ("100x100", "100"): 1.0
        }

        self.ceramica_asimetrica = {
            ("10x15", "1015"): .0150, ("10x20", "1020"): .0200, ("10x25", "1025"): .0250,
            ("10x30", "1030"): .0300, ("10x35", "1035"): .0350, ("10x40", "1040"): .0400,
            ("20x25", "2025"): .0500, ("20x30", "2030"): .0600, ("20x35", "2035"): .0700,
            ("20x40", "2040"): .0800, ("20x45", "2045"): .0900, ("20x50", "2050"): .1000,
            ("30x35", "3035"): .1050, ("30x40", "3040"): .1200, ("30x45", "3045"): .1350,
            ("30x50", "3050"): .1500, ("30x55", "3055"): .1650, ("30x60", "3060"): .1800,
            ("40x45", "4045"): .1800, ("40x50", "4050"): .2000, ("40x55", "4055"): .2200,
            ("40x60", "4060"): .2400, ("40x65", "4065"): .2600, ("40x70", "4070"): .2800,
            ("50x55", "5055"): .2750, ("50x60", "5060"): .3000, ("50x65", "5065"): .3250,
            ("50x70", "5070"): .3500, ("50x75", "5075"): .3750, ("50x80", "5080"): .4000,
            ("60x65", "6065"): .3900, ("60x70", "6070"): .4200, ("60x75", "6075"): .4500,
            ("60x80", "6080"): .4800, ("60x85", "6085"): .5100, ("60x90", "6090"): .5400,
            ("70x75", "7075"): .5250, ("70x80", "7080"): .5600, ("70x85", "7085"): .5950,
            ("70x90", "7090"): .6300, ("70x95", "7095"): .6650, ("70x100", "70100"): .70,
            ("80x85", "8085"): .6800, ("80x90", "8090"): .7200, ("80x95", "8095"): .7600,
            ("80x100", "80100"): .80, ("90x95", "9095"): .8550, ("90x100", "90100"): .90
        }

        self.ladrillo_general = {

        }

        self.baldosas = Baldosas()

    def baldosas(self, medidas_piso: Medidas2D, medida_baldosa: Medidas2D):
        self.baldosas.area_piso = area_2d(medidas_piso)
        self.baldosas.area_baldosas = area_2d(medida_baldosa)
        self.baldosas.baldosas = float(round(dec(self.baldosas.area_piso) * dec(self.baldosas.area_baldosas), 2))
        return self.baldosas

    def baldosas_asimetricas(self, medida_baldosa: str, area: float):
        area_tableta = self.ceramica_asimetrica[medida_baldosa]

    def ladrillos_muro(self, metros_muro: float, altura_muro: float, espesor_brechas: float, posicion: int):
        return 0


dosificacion = Dosificacion()
prefabricado = Prefabricado()
