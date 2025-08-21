from dosificacion import dosificacion
from elemento import Elemento3D, Areas, Medidas3D
from utilidades import Calcular

cal = Calcular()


def run():
    nombre = "columnas"
    cantidad = 20
    medidas = Medidas3D(10.2, 11.5, 5.4)
    areas = cal.calcular_3d(medidas, cantidad)
    concreto = dosificacion.concreto(areas.area_all, "122")
    elemento_3d = Elemento3D(nombre, cantidad, areas, medidas, concreto)

    print(elemento_3d.json())


if __name__ == '__main__':
    run()
