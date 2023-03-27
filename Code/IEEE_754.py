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


    binary_x_exponent = binary_x_exponent[1:len(binary_x_exponent)]
    binary_y_exponent = binary_y_exponent[1:len(binary_y_exponent)]

    mantissa_x_binary = binary_x_exponent
    mantissa_y_binary = binary_y_exponent
    # print(f"mantissa_x_part = {mantissa_x_binary}")
    # print(f"mantissa_y_part = {mantissa_y_binary}")

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

    print(f"full {status_x}{input_num_x} representation: {int(x_sign_bit)}.{binary_x_exponent}.{mantissa_x_binary}")
    print(f"full {status_y}{input_num_y} representation: {int(y_sign_bit)}.{binary_y_exponent}.{mantissa_y_binary}")

    # actual addition
    #if binary_x_exponent == binary_y_exponent:
    from BinaryCalcFunc import binary_subtraction
    if input_num_x > input_num_y:
        number_1 = input_num_x
        number_2 = min(input_num_x,input_num_y)
        binary_summ_number_exponent = binary_x_exponent
        exponent_difference = binary_subtraction(binary_x_exponent, binary_y_exponent).lstrip('0')
    else:
        number_1 = max(input_num_x, input_num_y)
        number_2 = min(input_num_x, input_num_y)
        binary_summ_number_exponent = binary_y_exponent
        exponent_difference = binary_subtraction(binary_y_exponent, binary_x_exponent).lstrip('0')



    print(exponent_difference)
    print(number_1, number_2)


iee_addition(-54.4,85.125) #54.4 85.125

# 54.4
# 0 10000100    10110011001100110011010
# 0 10000100    10110011001100110011010


