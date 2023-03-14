# (Division as it is (into a column))
# first make def for to convert num into binary
from BinaryCalcFunc import binary_format
from BinaryCalcFunc import negative_binary_to_decimal
from BinaryCalcFunc import binary_to_decimal
from BinaryCalcFunc import binary_array_sum
from BinaryCalcFunc import binary_subtraction
def binary_division(input_num_x, input_num_y):
    print(f"~~~~~~binary_division({input_num_x},{input_num_y})~~~~~")
    # exeption
    if not isinstance(input_num_x, int) or not isinstance(input_num_y, int):
        print("INPUT INT! ERROR")
        return None
    if input_num_y == 0:
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

    input_num_x, input_num_y = abs(input_num_x), abs(input_num_y)

    try:
        Dividend = binary_format(input_num_x, binary_len_set)    # input_num_x_string = Multiplicand
    except:
        print(f"error in formatting {input_num_x} to string in 'booth_algorithm' function")
    try:
        Divisor = binary_format(input_num_y, binary_len_set)        # input_num_y_string = Dividend
    except:
        print(f"error in formatting {input_num_y} to string in 'booth_algorithm' function")

    if len(Dividend) > len(Divisor):
        print(f"error because {Dividend} is bigger then {Divisor}")
        return None

    remainder = '0'
    Divisor = Divisor.lstrip("0")
    Dividend = Dividend.lstrip("0")

    Answer = ''
    divident_part = ''
    for i in range(len(Dividend)):
        divident_part += Dividend[i]
        # print(f"divident_part = {divident_part}, adding Dividend[i({i}) = {Dividend[i]}]", end=' ')
        if len(divident_part) < len(Dividend):
            if int(Divisor) > int(divident_part):   # if 3 > part of Dividend
                # print('')
                Answer += '0'
            else:                                   # if 3 < part of Dividend

                divident_part = binary_subtraction(divident_part, Divisor).lstrip('0')
                # print(f'update divident_part = {divident_part}')
                Answer += '1'
                continue
        else:
            print(f"Answer = {Answer}")
    if int(divident_part) != 0:
        remainder = str(int(divident_part))
    print(f"Answer = {Answer}")
    print(f"remainder = {remainder}")
    status_symbol = ''
    if not "not" in status:
        status_symbol = '-'
    if status_symbol == '-':
        print(f"Answer in decimal: {status_symbol}{negative_binary_to_decimal(Answer)}")
    else:
        print(f"Answer in decimal: {status_symbol}{binary_to_decimal(Answer)}")
    return Answer

binary_division(16,4)