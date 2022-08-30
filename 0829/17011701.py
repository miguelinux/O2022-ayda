#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
# Nombre: Christopher Daniel Esparza Contreras
# No. Control: 17011701
# Calificación: XXX

def factorial(n):
    if n == 0:
        return 1
    if n < 0:
        return "error"
    for i in range(1,n):
        n = n * i
    return n

numero = eval(input("Escribe un número: "))

print("El factorial de", numero, "es", factorial(numero))
