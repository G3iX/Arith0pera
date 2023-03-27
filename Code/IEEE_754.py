# addition
# Align binary points
# Add significands
# Normalize result
import math

from  BinaryCalcFunc import binary_format
from  BinaryCalcFunc import binary_array_sum
def iee_addition(input_num_x, input_num_y):
    if not isinstance(input_num_x, float) or not isinstance(input_num_y, float): #or max(input_num_y, input_num_x) > 128:
        print("INPUT INT! ERROR")
        return None
    x_sign_bit = False
    y_sign_bit = False
    if input_num_x < 0:
        x_sign_bit = True
    if input_num_y < 0:
        y_sign_bit = True

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

    binary_x_exponent = binary_array_sum([binary_x_exponent, one_hundred_twenty_seven_binary], True, True)
    binary_y_exponent = binary_array_sum([binary_y_exponent, one_hundred_twenty_seven_binary], True, True)

    float_len_x = str(input_num_x)
    float_len_x = float_len_x.split('.')
    float_len_y = str(input_num_y)
    float_len_y = float_len_y.split('.')

    mantissa_x = input_num_x - math.floor(input_num_x)
    mantissa_y = input_num_y - math.floor(input_num_y)


    round_arrange = (max(len(float_len_x[1]),len(float_len_y[1])))
    # mantissa_x_binary = mantissa_x_part
    # mantissa_y_binary = mantissa_y_part

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

    print(f"full {input_num_x} representation: {int(x_sign_bit)}.{binary_x_exponent}.{mantissa_x_binary}")
    print(f"full {input_num_y} representation: {int(y_sign_bit)}.{binary_y_exponent}.{mantissa_y_binary}")


iee_addition(54.4,85.125) #54.4

# 54.4
# 0 10000100    10110011001100110011010
# 0 10000100    10110011001100110011010


