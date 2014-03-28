#!/usr/bin/python
#!encoding: UTF-8
def f (n):
    suma = 0.0
    for i in range (1, int(n+1)):
        xi = (i-0.5)/n
        fxi = 4/(1+xi**2)
        suma += fxi
    pi = suma/n
    return pi

if (__name__ == "__main__"):
    import sys
    if (len(sys.argv) == 1):
        print "Se pide  dos argumentos: número de intervalos ."
        n = int(raw_input("Introduzca el número de intervalos utilizados para aproximar pi: "))
        t = int(raw_input("Introduzca el número de ejecuciones del algoritmo: "))
    elif (len(sys.argv) == 2):
        print "detectado un único argumento en la línea de comandos."
        print "Se pide de dos argumentos: número de intervalos ."
        print "sigue las instrucciones"
        n = int(raw_input("Introduzca el número de intervalos utilizados para aproximar pi: "))
        t = int(raw_input("Introduzca el número de ejecuciones del algoritmo: "))
    else:
        n = int(sys.argv[1])
        t = int(sys.argv[2])
    PI = 3.1415926535897931159979634685441852
    print "Intervalos\tValor obtenido\tValor real\tError cometido"
    for j in range (1, t+1):
        pi = f(j*n)
        print "%d\t\t%1.10g\t%1.10g\t%1.10f" %(j, pi, PI, abs(pi-PI)) 