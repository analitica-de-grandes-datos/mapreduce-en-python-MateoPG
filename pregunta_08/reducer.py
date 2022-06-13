#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

curletter = None
totalsum = 0
totalcount = 0

if __name__ == "__main__":

    for purp in sys.stdin:
        letter, amount = purp.split("\t")
        amount = float(amount)

        if curletter == None:
            curletter = letter
            totalsum = amount
            totalcount = 1
        else:
            if letter == curletter:
                totalsum += amount
                totalcount += 1
            else:
                sys.stdout.write("{}\t{}\t{}\n".format(
                    curletter, totalsum, (totalsum/totalcount)))
                curletter = letter
                totalsum = amount
                totalcount = 1
    sys.stdout.write("{}\t{}\t{}\n".format(
        curletter, totalsum, (totalsum/totalcount)))
