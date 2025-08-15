from dosificacion import DosificacionConcreto

dosifi = DosificacionConcreto()


def run():
    concreto = dosifi.dosificacion(86.5, "122")
    print(concreto.cemento)


if __name__ == '__main__':
    run()
