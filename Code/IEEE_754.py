# addition
# Align binary points
# Add significands
# Normalize result
import math


def iee_addition(input_num_x, input_num_y):
    # to ieee_754 encoding:

    if not isinstance(input_num_x, float) or not isinstance(input_num_y, float): #or max(input_num_y, input_num_x) > 128:
        print("INPUT INT! ERROR")
        return None
    from BinaryCalcFunc import binary_format

    x_sign_bit = False
    y_sign_bit = False
    if input_num_x < 0:
        x_sign_bit = True
    if input_num_y < 0:
        y_sign_bit = True
    input_num_x = abs(input_num_x)
    input_num_y = abs(input_num_y)
    binary_len_set = 16

    # print(math.floor(input_num_x))
    # print(math.floor(input_num_y))
    binary_x_exponent = binary_format(math.floor(input_num_x),binary_len_set).lstrip('0')#[::-1]
    binary_y_exponent = binary_format(math.floor(input_num_y),binary_len_set).lstrip('0')#[::-1]

    print(f"binary exponent from the start y= {binary_y_exponent},x= {binary_x_exponent} ")
    dot_number_x = binary_x_exponent[0]
    dot_number_y = binary_y_exponent[0]

    binary_x_exponent = binary_x_exponent[1:len(binary_x_exponent)]
    binary_y_exponent = binary_y_exponent[1:len(binary_y_exponent)]

    mantissa_x_binary = binary_x_exponent
    mantissa_y_binary = binary_y_exponent
    # print(f"mantissa_x_part = {mantissa_x_binary}")
    print(f"mantissa_y_part = {mantissa_y_binary}")

    one_hundred_twenty_seven_binary = binary_format(127, 8)

    binary_x_exponent = binary_format(len(binary_x_exponent),8)
    binary_y_exponent = binary_format(len(binary_y_exponent),8)

    from BinaryCalcFunc import binary_array_sum


    if x_sign_bit == 0 or x_sign_bit == 1:
        binary_x_exponent = binary_array_sum([binary_x_exponent, one_hundred_twenty_seven_binary], True, True)
    #else:
    #    binary_x_exponent = binary_subtraction(one_hundred_twenty_seven_binary, binary_x_exponent)
    if y_sign_bit == 0 or y_sign_bit == 1:
        binary_y_exponent = binary_array_sum([binary_y_exponent, one_hundred_twenty_seven_binary], True, True)
    #else:
    #    binary_y_exponent = binary_subtraction(one_hundred_twenty_seven_binary, binary_y_exponent)

    float_len_x = str(input_num_x)
    float_len_x = float_len_x.split('.')
    float_len_y = str(input_num_y)
    float_len_y = float_len_y.split('.')

    mantissa_x = input_num_x - math.floor(input_num_x)
    mantissa_y = input_num_y - math.floor(input_num_y)


    round_arrange = (max(len(float_len_x[1]),len(float_len_y[1])))
    #print(round(mantissa_x,round_arrange))
    # fraction bits, mantissa
    for i in range(1,24 - len(mantissa_x_binary)):
        #print(i)
        x_mn_calc = round((mantissa_x * 2), round_arrange)
        #print(f"x-mn_calc = {x_mn_calc}, y-mn_calc = {y_mn_calc}")
        mantissa_x_binary += str(x_mn_calc)[0]
        mantissa_x = float("0." + str(x_mn_calc).split('.')[1])


    for i in range(1, 24 - len(mantissa_y_binary)):
        y_mn_calc = round((mantissa_y * 2), round_arrange)
        mantissa_y_binary += str(y_mn_calc)[0]
        mantissa_y = float("0." + str(y_mn_calc).split('.')[1])

    # one_hundred_twenty_seven_binary = binary_format(127, 8)
    # print(f"input_num_x = {input_num_x}")
    # print(f"input_num_Y = {input_num_y}")
    # print(f"binary_x_exponent = {binary_x_exponent}, mantissa x = {mantissa_x_binary}")
    # print(f"binary_y_exponent = {binary_y_exponent}, mantissa y = {mantissa_y_binary}")
    status_x = ''
    status_y = ''
    if x_sign_bit == 1:
        status_x = '-'
    if y_sign_bit == 1:
        status_y = '-'

    print(f"full (x) {status_x}{input_num_x} representation: {int(x_sign_bit)}.{binary_x_exponent}.{mantissa_x_binary}")
    print(f"full (y) {status_y}{input_num_y} representation: {int(y_sign_bit)}.{binary_y_exponent}.{mantissa_y_binary}")

    # actual addition
    #if binary_x_exponent == binary_y_exponent:
    from BinaryCalcFunc import binary_subtraction
    from BinaryCalcFunc import binary_to_decimal

    Exponent_x = binary_to_decimal(binary_x_exponent)
    Exponent_y = binary_to_decimal(binary_y_exponent)


    if input_num_x >= input_num_y:
        number_1 = input_num_x
        number_2 = min(input_num_x,input_num_y)
        # binary_summ_number_exponent = binary_x_exponent
        # Exponent_x > Exponent_y
        Exponent_number_1 = Exponent_x - 127
        Exponent_number_2 = Exponent_y - 127
        # exponent_difference = binary_subtraction(binary_x_exponent, binary_y_exponent).lstrip('0')
    else:
        number_1 = max(input_num_x, input_num_y)
        number_2 = min(input_num_x, input_num_y)
        # binary_summ_number_exponent = binary_y_exponent
        # exponent_difference = binary_subtraction(binary_y_exponent, binary_x_exponent).lstrip('0')
        # Exponent_x < Exponent_y
        Exponent_number_2 = Exponent_x - 127
        Exponent_number_1 = Exponent_y - 127
    # print(mantissa_x_binary)
    # print(exponent_difference)
    # print(number_1, number_2)
    # print(Exponent_number_1, Exponent_number_2)
    if Exponent_number_1 != Exponent_number_2:
        # choose smaller exponent
        check = min(Exponent_number_1, Exponent_number_2)
        max_check = max(Exponent_number_2, Exponent_number_1)
        if check == Exponent_number_1:
            # x is smaller (have smaller exponent check)
            bigger_mantissa = mantissa_y_binary[0:max_check]
            bigger_exponent = binary_y_exponent
            bigger_num_sing = y_sign_bit
            bigger_mantissa_start = dot_number_y
            if Exponent_number_2 > Exponent_number_1:
                prolongue_smaller_mantissa_part = bigger_mantissa_start + mantissa_x_binary[0:Exponent_number_1 + 2]
            else:
                prolongue_smaller_mantissa_part = mantissa_x_binary[0:Exponent_number_1 + 2]
        if check == Exponent_number_2:
            # y is smaller (have smaller exponent check)
            bigger_mantissa = mantissa_x_binary[0:max_check + 2]
            bigger_num_sing = x_sign_bit
            bigger_exponent = binary_x_exponent

            bigger_mantissa_start = dot_number_x
            if Exponent_number_2 < Exponent_number_1:
                prolongue_smaller_mantissa_part = bigger_mantissa_start + mantissa_y_binary[0:Exponent_number_2 + 2]
            else:
                prolongue_smaller_mantissa_part =  mantissa_y_binary[0:Exponent_number_2 + 2]

        # print(prolongue_smaller_mantissa_part)
        prolongue_smaller_mantissa_part = prolongue_smaller_mantissa_part.zfill(max_check)
        # print(prolongue_smaller_mantissa_part)
        # adding mantissas

        number_from_mantissas_sum = binary_array_sum([prolongue_smaller_mantissa_part, bigger_mantissa], True, True)
        print(f"prolonged smaller exponent mantissa = {prolongue_smaller_mantissa_part}, bigger exponent mantissa part = {bigger_mantissa}, their summ = {number_from_mantissas_sum}")
        # print(number_from_mantissas_sum)
        # bigger exponent is addition of mantissa exponent elements

        # bigger_exponent = from mantissas len?

        new_sum_exponent = binary_array_sum([bigger_exponent, one_hundred_twenty_seven_binary], True, True)
        # print(bigger_exponent)

        new_ieee_754_number = str(int(bigger_num_sing)) + "." + bigger_exponent + "." + number_from_mantissas_sum[::-1].zfill(23)[::-1] # 01000010110100110000000000000000
        print(f"sum = {new_ieee_754_number}")

iee_addition(35.75,20.5) # 54.4, 12.125 I received 13.25 not 66.525 - error somewhere in mantissa migration (notes) 12.125,54.4,

#iee_addition(54.4, 12.125)
# 54.4
# 0 10000100    10110011001100110011010
# 0 10000100    10110011001100110011010


