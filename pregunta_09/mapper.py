#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

if __name__ == "__main__":

    for line in sys.stdin:
        result = line.split()
        
        #sys.stdout.write("{}".format(result))
        sys.stdout.write("{},{},{}\n".format(result[0],result[1],result[2]))
