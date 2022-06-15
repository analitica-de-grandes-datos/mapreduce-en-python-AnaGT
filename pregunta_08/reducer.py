#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
if __name__ == '__main__':
    curkey = None
    total1 = 0
    total2 = 0
    letra = 0
    for line in sys.stdin:

        key, val = line.split("\t")
        val = float(val)

        if key == curkey:
            letra += 1
            total1 += val
            total2 = total1 / letra
        else:
            if curkey is not None:
                sys.stdout.write("{}\t{}\t{}\n".format(curkey, total1, total2))
            curkey = key
            letra = 1
            total1 = val
            total2 = total1 / letra
    sys.stdout.write("{}\t{}\t{}\n".format(curkey, total1 , total2))
