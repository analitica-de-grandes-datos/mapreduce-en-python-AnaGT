#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
if __name__ == '__main__':
    list1 = []
    list2 = []

    for line in sys.stdin:

        list1.append(line)
    list2= sorted(list1, key= lambda x: x[2])
    for item in list2:
        sys.stdout.write("{}".format(item))