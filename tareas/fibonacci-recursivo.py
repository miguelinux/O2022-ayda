#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# Nombre: Nombre del Estudiante
# No. Control: 123456789
# Calificación: XXX

def fibonacci(num):

    if num <= 0:
        return "indefinida"
    
    if num == 1:
        return 0

    if num == 2:
        return 1

    return fibonacci(num-1) + fibonacci(num-2)


def main():
    numero = eval(input("Escribe un número: "))
    print("La posición", numero, "de fibonacci es", fibonacci(numero))


if __name__ == "__main__":
    main()

