#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
if __name__ == '__main__':
    curkey = None
    total1 = 0
    total2 = 0

    for line in sys.stdin:

        key, val = line.split("\t")
        val = float(val)

        if key == curkey:
             if val > total1:
                 total1 = val
                 if key == curkey:
                    if val < total1:
                        total2 = val
        else:
            if curkey is not None:
                sys.stdout.write("{}\t{}\t{}\n".format(curkey, total1 , total2))
            curkey = key
            total1 = val
            total2 = val
    sys.stdout.write("{}\t{}\t{}\n".format(curkey, total1 , total2))
