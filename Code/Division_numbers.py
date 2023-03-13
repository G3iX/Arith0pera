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



    sequence_count = max(len(Divisor), len(Quotient))

    Quotient = list(Quotient)
    Divisor = list(Divisor)
    dividend = []
    remainder = '0'
    for i in range(sequence_count):
        pre_last_quotient = Quotient[len(Quotient) - 2 - i]  #
        took_last_quotient = Quotient[len(Quotient) - 1 - i]  # quotient Arithmetical - to right

        pre_last_divisor = Divisor[len(Divisor) - 2 - i]  #
        took_last_divisor = Divisor[len(Divisor) - 1 - i]  # divisor Arithmetical - to right

        quotient_shift_to_right = int(pre_last_quotient + took_last_quotient)
        divisor_shift_to_right = int(pre_last_divisor + took_last_divisor)
        print(f"i = {i}, quotient_shift_to_right = {quotient_shift_to_right}, divisor_shift_to_right = {divisor_shift_to_right}")
        # HOW CAN I GET REMAINDER?
        if quotient_shift_to_right == 1:
            remainder += '1'

        # print(f"dividend = {dividend}")
        if divisor_shift_to_right > quotient_shift_to_right:
            # Quotient.pop(len(Quotient) - 1)
            # Divisor.pop(len(Divisor) - 1)
            dividend.insert(0, '1')
            continue
        else:
            # Quotient.pop(len(Quotient) - 1)
            # Divisor.pop(len(Divisor) - 1)
            dividend.insert(0, '0')
            continue

    result = ''
    for j in dividend:
        result += str(j)

    result = binary_array_sum([result,remainder], True, False)
    result = result.zfill(sequence_count)
    print(f"result: {result} and its {status}")
    status_symbol = ''
    if not "not" in status:
        status_symbol = '-'
    if status_symbol == '-':
        print(f"decimal: {status_symbol}{negative_binary_to_decimal(result)}")
    else:
        print(f"decimal: {status_symbol}{binary_to_decimal(result)}")
    return result
    print(result)
    return result

from BinaryCalcFunc import negative_binary_to_decimal
from BinaryCalcFunc import binary_to_decimal
from BinaryCalcFunc import binary_array_sum

binary_division(8,8)