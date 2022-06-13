#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

curpurpose = None
maxamount = None

if __name__ == "__main__":

    for purp in sys.stdin:
        purpose, amount = purp.split("\t")
        amount = int(amount)

        if curpurpose == None:
            curpurpose = purpose
            maxamount = amount

        else:
            if purpose == curpurpose:
                if amount > maxamount:
                    maxamount = amount
            else:
                sys.stdout.write("{}\t{}\n".format(curpurpose, maxamount))
                curpurpose = purpose
                maxamount = amount
    sys.stdout.write("{}\t{}\n".format(curpurpose, maxamount))
