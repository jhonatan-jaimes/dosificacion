from dosificacion import dosificacion
from elemento import Elemento3D, Medidas3D, concreto as con
from utilidades import Calcular

cal = Calcular()


def run():
    nombre = "columnas"
    cantidad = 20
    medidas = Medidas3D(10.2, 11.5, 5.4)
    areas = cal.calcular_3d(medidas, cantidad)
    concreto = dosificacion.concreto(medidas.area(), "123")
    elemento_3d = Elemento3D(nombre, cantidad, areas, medidas, concreto)

    medida_dos = Medidas3D(8888.8, .01, .01)
    area = medida_dos.area()

    print(area)
    print(elemento_3d.json())


if __name__ == '__main__':
    run()
