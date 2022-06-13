#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

letters_dict = {}

if __name__ == "__main__":

    for line in sys.stdin:
        line_num, letters = line.split("\t")
        line_num = int(line_num)
        each_letter = letters.split(",")

        for letter in each_letter:

            letter = letter.strip()
            if letter not in letters_dict.keys():
                letters_dict[letter] = [line_num]

            else:
                letters_dict[letter] += [line_num]

    for key in sorted(letters_dict.keys()):
        str_nums = ",".join([str(i) for i in sorted(letters_dict[key])])
        sys.stdout.write(
            "{}\t{}\n".format(key, str_nums))
