#! /usr/bin/python
#!encoding: UTF-8

import moduloprct07

def error (n, t, umbral):
    solucion = 0.0
    warn = 0.0
    ref = moduloprct07.f(n)
    for j in range (t):
        pi = moduloprct07.f(n)
        if (abs(pi - ref) > umbral):
            warn += 1
    return (warn/t) * 100

if (__name__ == "__main__"):
    import sys
    if ((len(sys.argv) == 1) or (len(sys.argv) == 2) or (len(sys.argv[3]) == 3)):
        print "\nSe requiere la presencia de tres argumentos: \n\n\t- Número de intervalos.\n\t- Número de iteraciones.\n\t- Umbral de tolerancia.\n"
        n = int(raw_input("Introduzca el número de intervalos utilizados para aproximar pi: "))
        t = int(raw_input("Introduzca el número de ejecuciones del algoritmo: "))
        umbral = float(raw_input("Introduzca el umbral de tolerancia para comprobación de errores: "))
    else:
        n = int(sys.argv[1])
        t = int(sys.argv[2])
        umbral = float(sys.argv[3])
    answer = error(n, t, umbral)
    print "\nEl porcentaje de errores detectados ha sido del %.4f %%.\n" %answer
