#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == '__main__':

    lista1 = []
    lista3 = []
   
    for line in sys.stdin:
        line1 = line.replace('\n','').split(',')
        
        lista1.append(line1)
        

        letras=list(set([z[1] for z in lista1]))
        letras.sort()

    for letra in letras:
        lista2=[]
        for element in lista1:
            for i in element[1:]:
                    

                if i == letra:
                    lista2.append(int(element[0]))
        string=','.join(str(e) for e in sorted(lista2))    

        tupla=letra,string
        lista3=lista3+[tupla]

   
    for item in lista3:
        sys.stdout.write("{}\t{}\n".format(item[0],item[1]))
