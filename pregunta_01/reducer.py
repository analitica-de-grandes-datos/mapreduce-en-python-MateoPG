#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

curkey = None
total = 0

if __name__ == "__main__":

    for word in sys.stdin:
        key, val = word.split("\t")
        val = int(val)

        if key == curkey:
            total += val
        else:
            if curkey == None:
                curkey = key
                total = val
            else:
                sys.stdout.write("{}\t{}\n".format(curkey, total))
                curkey = key
                total = val
    sys.stdout.write("{}\t{}\n".format(curkey, total))
