#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

list_base_key = []
list_base_num = []

ordered_list_key = []
ordered_list_num = []

if __name__ == "__main__":

    for item in sys.stdin:
        key, val = item.split("\t")
        val = int(val)

        list_base_key.append(key)
        list_base_num.append(val)

    while len(list_base_key) != 0:
        lower_value = list_base_num[0]
        pos_to_extract = 0
        for i, curnum in enumerate(list_base_num):
            if curnum < lower_value:
                lower_value = curnum
                pos_to_extract = i

        ordered_list_key.append(list_base_key[pos_to_extract])
        ordered_list_num.append(lower_value)

        list_base_key.remove(list_base_key[pos_to_extract])
        list_base_num.remove(lower_value)

    for n, m in zip(ordered_list_key, ordered_list_num):
        sys.stdout.write("{},{}\n".format(n, m))
