# (Division as it is (into a column))
# first make def for to convert num into binary
from BinaryCalcFunc import binary_format
def binary_division(input_num_x, input_num_y):
    print(f"~~~~~~~~~~~~~~~binary_division({input_num_x},{input_num_y})~~~~~~~~~~~~~~~~~~~~~~")
    # exeption
    if not isinstance(input_num_x, int) or not isinstance(input_num_y, int):
        print("INPUT INT! ERROR")
        return None

    minus_flag_x = False
    minus_flag_y = False
    if input_num_x < 0:
        minus_flag_x = True
    if input_num_y < 0:
        minus_flag_y = True
    if minus_flag_x and minus_flag_y or not minus_flag_x and not minus_flag_y:
        status = "not negative"
    if minus_flag_x and not minus_flag_y or not minus_flag_x and minus_flag_y:
        status = "negative"

    binary_len_set = 8

    if minus_flag_x or minus_flag_y:
        negative_minimum = min(input_num_x, input_num_y)
        x = bin(negative_minimum)[2:]
        if 'b' in x:
            binary_len_set = (len(x) - 1) * 2
        else:
            binary_len_set = len(x) * 2

    try:
        Quotient  = binary_format(input_num_x, binary_len_set)    # input_num_x_string = Multiplicand
    except:
        print(f"error in formatting {input_num_x} to string in 'booth_algorithm' function")
    try:
        Divisor  = binary_format(input_num_y, binary_len_set)        # input_num_y_string = Quotient
    except:
        print(f"error in formatting {input_num_y} to string in 'booth_algorithm' function")

    if len(Quotient) > len(Divisor):
        print(f"error because {Quotient} is bigger then {Divisor}")
        return None


    dividend = []
    sequence_count = max(len(Divisor), len(Quotient))

    # total_length = sequence_count * 2 + 1
    # negative_multiplicand = binary_format(-input_num_x, binary_len_set)
    # A = Multiplicand.ljust(total_length, '0')
    # S = negative_multiplicand.ljust(total_length, '0')
    # Product = Quotient.zfill(total_length - 1)
    # Product += '0'
    Quotient = list(Quotient)
    # print(f"input_num_x is {input_num_x}, in binary {Quotient}")
    Divisor = list(Divisor)
    for i in range(sequence_count):
        pre_last_quotient = Quotient[i]  #
        took_last_quotient = Quotient[i]  # quotient Arithmetical - to right

        pre_last_divisor = Quotient[i]  #
        took_last_divisor = Quotient[i]  # divisor Arithmetical - to right

        quotient_shift_to_right = int(pre_last_quotient + took_last_quotient)
        divisor_shift_to_right = int(pre_last_divisor + took_last_divisor)

        if quotient_shift_to_right > divisor_shift_to_right:
            temp.pop(len(temp) - 1)
            if temp[0] == '0':
                temp.insert(0,'0')
            else:
                temp.insert(0,'1')
            continue

        else:
            if_10 = "".join(str(x) for x in temp)
            temp = binary_array_sum([if_10, A], False, True)
            temp.pop(len(temp) - 1)
            if temp[0] == '0':
                temp.insert(0, '0')

            else:
                temp.insert(0, '1')

            continue

    temp.pop(len(temp) - 1)
    result = ''
    for j in temp:
        result += str(j)


    pretty_res = result
    if 4 < sequence_count < 8:
        pretty_res = result[len(result)-8:len(result)] # -sequence_count
    else:
        pretty_res = result[len(result) - sequence_count:len(result)]  # -sequence_count
    print(f"result:{pretty_res} and its {status}")
    status_symbol = ''
    if not "not" in status:
        status_symbol = '-'
    print(f"decimal: {status_symbol}{negative_binary_to_decimal(pretty_res)}")
    return result


binary_division(8,2)