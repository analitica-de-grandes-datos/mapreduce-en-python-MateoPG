#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

if __name__ == "__main__":
    for line in sys.stdin:
        date_separated = line.split()[1].split("-")

        sys.stdout.write("{}\t1\n".format(
            date_separated[1]))
