# (Division as it is (into a column))
# first make def for to convert num into binary
from BinaryCalcFunc import binary_format
from BinaryCalcFunc import negative_binary_to_decimal
from BinaryCalcFunc import binary_to_decimal
from BinaryCalcFunc import binary_array_sum
def binary_division(input_num_x, input_num_y):
    print(f"~~~~~~~~~~~~~~~binary_division({input_num_x},{input_num_y})~~~~~~~~~~~~~~~~~~~~~~")
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

    sequence_count = max(len(Divisor), len(Dividend)) # N
    # x \ y = b (+ remainder)
    #Dividend = list(Dividend) # x
    #Divisor = list(Divisor) # y
    #print('', Dividend, '\n', Divisor)
    quotient = []
    remainder = '0'
    Divisor = Divisor.lstrip("0")
    Dividend = Dividend.lstrip("0")
    print(Dividend, Divisor, )


    # берем к-во элементов раных длинне делителя и сам делитель (делитель меньше делимого)

    # print(len(Divisor)) = 3
    Answear = ''
    for i in range(sequence_count):
        # if len(Dividend) > len(Divisor):
        #    Answear += '0' * (len(Dividend)-len(Divisor)-1)
        # print(Answear) # 00
        # print(took_dividend)
        Temp = ''
        Temp += Dividend[len(Temp)]
        if len(Temp) < len(Dividend):
            if int(Divisor) > int(Temp):
                Answear += '0'
                continue
            else:
                Answear += '1'
                continue
        else:
            print(Answear)
            return Answear
        took_dividend = Dividend[i:len(Divisor)+1+i]  # x   i:len(Divisor)+1+i


        if len(took_dividend) > len(Divisor): # 0
            dividend_shift_to_right = int(took_dividend)

        divisor_shift_to_right = int(Divisor)
        print(f"divisor_shift_to_right  = {Divisor}, [{divisor_shift_to_right}]")
        print(f"dividend_shift_to_right = {took_dividend}, [{dividend_shift_to_right}]")

        # print(f"i = {i}, dividend_shift_to_right = {dividend_shift_to_right}, divisor_shift_to_right = {divisor_shift_to_right}")
        # HOW CAN I GET REMAINDER?
        #if dividend_shift_to_right >= 1:
        #    remainder += '1'

        # print(f"dividend = {dividend}")
        if divisor_shift_to_right > dividend_shift_to_right:
            # Dividend.pop(len(Dividend) - 1)
            # Divisor.pop(len(Divisor) - 1)
            quotient.insert(0, '1')
            print('insert')
            print(f"-------------------")
            continue
        else:
            # Dividend.pop(len(Dividend) - 1)
            # Divisor.pop(len(Divisor) - 1)
            quotient.insert(0, '0')
            #if dividend_shift_to_right > 0:
            #    remainder += '1'
            print(f"-------------------")
            continue


    result = ''
    for j in quotient:
        result += str(j)
    # remainder = '1'
    print(f"remainder = {remainder}")
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

binary_division(22,3)