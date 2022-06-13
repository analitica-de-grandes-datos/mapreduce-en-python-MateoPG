#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

curletter = None
minamount = 1000
maxamount = 0

if __name__ == "__main__":

    for purp in sys.stdin:
        letter, amount = purp.split("\t")
        amount = float(amount)

        if curletter == None:
            curletter = letter
            minamount = amount
            maxamount = amount
        else:
            if letter == curletter:
                if amount < minamount:
                    minamount = amount
                if amount > maxamount:
                    maxamount = amount
            else:
                sys.stdout.write("{}\t{}\t{}\n".format(
                    curletter, maxamount, minamount))
                curletter = letter
                minamount = amount
                maxamount = amount
    sys.stdout.write("{}\t{}\t{}\n".format(curletter, maxamount, minamount))
