from decimal import Decimal as dec

from elemento import Mortero, Concreto, Baldosas


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

    def concreto(self, area: float, dosificacion: str):
        objeto_dosificacion = {}
        for i in self.dosificacion_concreto:
            if dosificacion in i:
                objeto_dosificacion = self.dosificacion_concreto[i]

        self.elemento_concreto.cemento = float(round(dec(area) * dec(objeto_dosificacion["cemento"]), 2))
        self.elemento_concreto.arena = float(round(dec(area) * dec(objeto_dosificacion["arena"]), 2))
        self.elemento_concreto.grava = float(round(dec(area) * dec(objeto_dosificacion["grava"]), 2))
        self.elemento_concreto.agua = float(round(dec(area) * dec(objeto_dosificacion["agua"]), 2))

        return self.elemento_concreto

    def mortero(self, area: float, dosificacion: str):
        objeto_dosificacion = {}

        for i in self.dosificacion_mortero:
            if dosificacion in i:
                objeto_dosificacion = self.dosificacion_mortero[i]

        self.elemento_mortero.cemento = float(round(dec(area) * dec(objeto_dosificacion["cemento"]), 2))
        self.elemento_mortero.arena = float(round(dec(area) * dec(objeto_dosificacion["arena"]), 2))
        self.elemento_mortero.agua = float(round(dec(area) * dec(objeto_dosificacion["agua"]), 2))

        return self.elemento_mortero


class Prefabricados:
    def __init__(self):
        self.simetricas_biblioteca = {
            "10": .0100, "15": .0225, "20": .0400, "25": .0625, "30": .0900, "35": .1225,
            "40": .1600, "45": .2025, "50": .2500, "55": .3025, "60": .3600, "65": .4225,
            "70": .4900, "75": .5625, "80": .6400, "85": .7225, "90": .8100, "95": .9025
        }

        self.asimetricas_biblioteca = {

        }

        self.ladrillo_general = {

        }

        self.baldosas_piso = Baldosas()

    def baldosas_simetricas(self, area: float, medida_baldosa: str):
        area_tableta = self.simetricas_biblioteca[medida_baldosa]

        self.baldosas_piso.name_baldosa = medida_baldosa
        self.baldosas_piso.area_baldosas = area_tableta
        self.baldosas_piso.baldosas = float(round(dec(area) / dec(area_tableta), 2))

        return self.baldosas_piso

    def baldosas_asimetricas(self, medida_baldosa: str, area: float):
        area_tableta = self.asimetricas_biblioteca[medida_baldosa]
