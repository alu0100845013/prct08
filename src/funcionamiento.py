#! /usr/bin/python
#!encoding: UTF-8

import error
def save (name, n_inter, umbrales):
    num_iter = 10 
    f = open(name, "w")
    for i in range (len(t_upla_inter)):
        f.write(str(t_upla_inter[i]) + '\n')
        for j in range (len(t_upla_umbrales)):
            sol = error.error(t_upla_inter[i], num_iter, t_upla_umbrales)
            f.write(str(sol) + '\n')
   
if (__name__ == "__main__"):
    import sys 
    t_upla_inter = (1e1, 1e2, 1e3, 1e4, 1e5, 1e6)
    t_upla_umbrales = (1e-1, 1e-2, 1e-3, 1e-4, 1e-5)
    if (len(sys.argv) == 1):
        name = raw_input("\nIntroduzca el nombre del fichero donde se almacenará la información:\n")
    else:
        name = sys.argv[1]
    save(name, t_upla_inter, t_upla_umbrales)