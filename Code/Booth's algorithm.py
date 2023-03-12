# Multiplying two numbers by Booth's algorithm
# first make def for to convert num into binary
from BinaryCalcFunc import binary_format
# second make def for addition if two binary strings
from BinaryCalcFunc import binary_array_sum
def booth_algorithm(input_num_x, input_num_y): # only int !
    print(f"~~~~~~~~~~~~~~~booth_algorithm({input_num_x},{input_num_y})~~~~~~~~~~~~~~~~~~~~~~")
    # exeption
    if not isinstance(input_num_x, int) or not isinstance(input_num_y, int):
        print("INPUNT INT! ERROR")
        return None

    minus_flag_x = False
    minus_flag_y = False
    if input_num_x < 0:
        minus_flag_x = True
    if input_num_y < 0:
        minus_flag_y = True
    if minus_flag_x and minus_flag_y or not minus_flag_x and not  minus_flag_y:
        status = "not negative"
    if minus_flag_x and not minus_flag_y or not minus_flag_x and minus_flag_y:
        status = "negative"

    binary_len_set = 8

    # y = bin(input_num_y)[2:]

    if minus_flag_x or minus_flag_y:
        negative_minimum =min(input_num_x, input_num_y)
        x = bin(negative_minimum)[2:]
        # print(f"x:{x}")
        if 'b' in x:
            binary_len_set = (len(x) - 1) * 2
        else:
            binary_len_set = len(x) * 2


    """if 0 < input_num_x <= 15:
        binary_len_set = 4
    elif input_num_x < 0 or input_num_x > 15:
        binary_len_set = 16 """

    try:
        Multiplicand = binary_format(input_num_x, binary_len_set)    # input_num_x_string = Multiplicand
    except:
        print(f"error in formatting {input_num_x} to string in 'booth_algorithm' function")
    try:
        Quotient = binary_format(input_num_y, binary_len_set)        # input_num_y_string = Quotient
    except:
        print(f"error in formatting {input_num_y} to string in 'booth_algorithm' function")


    sequence_count = max(len(Multiplicand), len(Quotient))
    total_length = sequence_count * 2 + 1
    
    negative_multiplicand = binary_format(-input_num_x, binary_len_set)
    A = Multiplicand.ljust(total_length, '0')
    S = negative_multiplicand.ljust(total_length, '0')
    Product = Quotient.zfill(total_length - 1)
    Product += '0'

    print(f"A:{A}")
    print(f"S:{S}")
    print(f"P:{Product}")
    temp = list(Product)
    print("second input array:", temp)
    print(f"sequence_count:{sequence_count}")
    for i in range(sequence_count):
        # print(i)
    #while True:
        pre_last = temp[len(temp) - 2]  #
        took_last = temp[len(temp) - 1]  # Arithmetical - to right
        # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        # print(f"took pre_last: {pre_last} and last: {took_last}")
        # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        if pre_last+took_last == "00":
            temp.pop(len(temp) - 1)
            if temp[0] == '0':
                temp.insert(0,'0')
            else:
                temp.insert(0,'1')
            # print("'00' chance probe:")
            # print(f"temp after insert :00: {temp}")
            continue
        elif pre_last+took_last == "01":
            if_10 = "".join(str(x) for x in temp)
            temp = binary_array_sum([if_10, A], False, True)
            temp.pop(len(temp) - 1)
            if temp[0] == '0':
                temp.insert(0, '0')
                # print("'01' chance probe:")
                # print(f"'01' probe inserted {temp}:")
            else:
                temp.insert(0, '1')
                # print("'01' chance probe:")
                # print(f"'01' probe inserted {temp}:")
            continue
        elif pre_last+took_last == "10":
            if_10 = "".join(str(x) for x in temp)
            temp = binary_array_sum([if_10, S], False, True)
            temp.pop(len(temp) - 1)
            if temp[0] == '0':
                temp.insert(0, '0')
                # print("'10' chance probe:")
                # print(f"'10' probe inserted {temp}:")
            else:
                temp.insert(0, '1')
                # print("'10' chance probe:")
                # print(f"'10' probe inserted {temp}:")
            continue
        elif took_last + pre_last == "11":
            temp.pop(len(temp) - 1)
            if temp[0] == '0':
                temp.insert(0, '0')
            else:
                temp.insert(0, '1')

    temp.pop(len(temp) - 1)
    result = ''
    for j in temp:
        result += str(j)
            # print("'11' chance probe:")
            # print(f"result = {result}") # and int {int(result[1:len(result)], 2)} and {result[1:len(result)]}")
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


from BinaryCalcFunc import negative_binary_to_decimal
booth_algorithm(3, -4)
# booth_algorithm(-8, 2)
# booth_algorithm(-16, 5)



