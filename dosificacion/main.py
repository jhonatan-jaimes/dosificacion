from dosificacion import Dosificacion
from elemento import Elemento3D, Areas, Medidas3D

dosifi = Dosificacion()


def run():
    nombre = "columnas"
    cantidad = 20
    medidas = Medidas3D(10.2, 11.5, 5.4)
    area_one = medidas.largo * medidas.ancho * medidas.alto
    area_all = area_one * cantidad
    concreto = dosifi.concreto(area_all, "121")
    areas = Areas(area_one, area_all)
    elemento_3d = Elemento3D(nombre, cantidad, areas, medidas)

    print(concreto.json())

    print(elemento_3d.json())


if __name__ == '__main__':
    run()
