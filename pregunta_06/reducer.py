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

        curkey = None
        total1 = 0
        total2 = 0

        for line in lista:

            key, val = line.split(",")
            val = float(val)

            if key == curkey:
                if val > total1:
                    total1 = val

            else:
                if curkey is not None:
                    sys.stdout.write("{},{},{}\n".format(curkey, total1 , total2))
                curkey = key
                total1 = val
                total2 = val
        sys.stdout.write("{},{},{}\n".format(curkey, total1 , total2))
