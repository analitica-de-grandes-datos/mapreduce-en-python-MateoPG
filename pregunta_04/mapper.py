#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

if __name__ == "__main__":
    for line in sys.stdin:
        column_separated = line.split()

        sys.stdout.write("{}\t1\n".format(
            column_separated[0]))
