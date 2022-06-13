#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

letters = []
dates = []
values = []

if __name__ == "__main__":

    for line in sys.stdin:
        letter, date, value = line.split("\t")
        value = int(value)

        letters.append(letter)
        dates.append(date)
        values.append(value)

    zipped_lists = zip(letters, dates, values)

    zipped_lists = sorted(zipped_lists, key=lambda x: x[2])

    for l, d, v in zipped_lists[:6]:
        sys.stdout.write("{}   {}   {}\n".format(l, d, v))
