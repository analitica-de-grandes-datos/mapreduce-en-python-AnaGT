#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

#
# Esta funcion reduce los elementos que tienen la misma clave
#
if __name__ == '__main__':

    lista = []
    #
    # cada linea de texto recibida se adiciona a la lista1
    #
    for line in sys.stdin:
        line1 = line.replace('\n','').split(',')
        line1[2] = int(line1[2])
        lista.append(line1)
       
    lista2 = sorted(lista, key=lambda x:x[2])
    lista2 = sorted(lista2, key=lambda x:x[0])

    for item in lista2:
        sys.stdout.write("{}   {}   {}\n".format(item[0],item[1],item[2]))
