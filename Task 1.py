# - d) Booth's algorithm
# from calc import binary_array_column_sum
def binary_refacor(input_array):
    # print(f"input array {input_array}")
    for i in range(len(input_array)):
        if input_array[i] == 'b':
            input_array[i] = '1'
    return input_array

def binary_array_sum(input_array, we_need_string, if_output_array_in_string): # unoptimized option, i'll try to delete it after
    # print("------------------------binary_array_sum-----------------------------")
    # Find the maximum length of the binary strings in the array
    max_len = max(len(x) for x in input_array)
    # print("max_len =",max_len)
    # Pad each binary string with leading zeroes to make them the same length
    input_array = [x.zfill(max_len) for x in input_array]
    # print("input_array =", input_array )
    # Initialize the result as a list of zeroes
    result = [0] * (max_len + 1)
    # print("result =", result)
    # Add up the binary numbers as done in columns
    for i in range(max_len - 1, -1, -1):
        column_sum = sum(int(x[i]) for x in input_array) + result[i + 1] # can't eat '-' numbers
        # тут надо реализация дополнительного кода числа с отрицанием(?)
        # print("column_sum = ", result)
        result[i + 1] = column_sum % 2
        result[i] += column_sum // 2
        # print("result num = ", result)
    #print("binary_array_sum result", result)
    #print('-------------')
    if we_need_string:      # Convert the result to a binary string and return it
        result = "".join(str(x) for x in result).lstrip("0")
        # print("result =", result)
        return result
    else:                   # Convert the result to an array and return it
        if if_output_array_in_string:
            string_result = []
            for i in result:
                string_result.append(str(i))
            string_result.pop(0)
            # print('arr string', string_result)
            # print('-------------')
            return string_result
        # if result[0]=='0' or '1':
        #    result.pop(0)
        # print('before joint(arr int)', result)
        return result

def binary_reverse(input_array):
    print(input_array)
    for i in range(len(input_array)-1):

        # print(i)
        if input_array[i] == '-':
            input_array.pop(i)
            input_array.reverse()  # # # # # # # # # # # test!
            temp = ''
            negative_input_array = []
            for i in input_array:
                temp += i
            try:
                negative_input_array = binary_array_sum([temp, "1"], True, False)
            except:
                print("aboba error")
    return negative_input_array

def booth_algo_def(m, negative_m ,r):
    # print("-----------------------booth_algo_def-------------------------")
    n = max(len(m), len(r))
    toll = n * 2 + 1

    A = m.ljust(toll, '0')
    S = negative_m.ljust(toll, '0')
    P = r.zfill(toll - 1)
    P += '0'

    temp = list(P)
    print('temp start = ', temp)

    while True:
        pre_last = temp[len(temp) - 2]  #
        took_last = temp[len(temp) - 1]  # Arithmetical - to right
        # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        # print(f"took pre_last: {pre_last} and last: {took_last}")
        # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        if pre_last+took_last == "00":
            # print("'00' chance probe:")
            temp.pop(len(temp) - 1)
            if temp[0] == '0':
                temp.insert(0,'0')
            else:
                temp.insert(0,'1')
            # print(f'temp after insert :00: {temp}')
            continue

        elif pre_last+took_last == "01":
            # print("'01' chance probe:")
            if_10 = "".join(str(x) for x in temp)
            temp = binary_array_sum([if_10, A], False, True)
            temp.pop(len(temp) - 1)

            if temp[0] == '0':
                temp.insert(0, '0')
                # print(f"'10' probe inserted {temp}:")
            else:
                temp.insert(0, '1')
                # print(f"'10' probe inserted {temp}:")
            continue

        elif pre_last+took_last == "10":
            # print("'10' chance probe:")
            if_10 = "".join(str(x) for x in temp)
            temp = binary_array_sum([if_10, S], False, True)
            temp.pop(len(temp) - 1)

            if temp[0] == '0':
                temp.insert(0, '0')
                # print(f"'10' probe inserted {temp}:")
            else:
                temp.insert(0, '1')
                # print(f"'10' probe inserted {temp}:")
            continue

        elif took_last + pre_last == "11":
            # print("'11' chance probe:")
            temp.pop(len(temp) - 1)
            if temp[0] == '0':
                temp.insert(0, '0')
            else:
                temp.insert(0, '1')
            result = ''
            temp.pop(len(temp) - 1)
            for j in temp:
                result += str(j)
            # print(f"result = {result}") # and int {int(result[1:len(result)], 2)} and {result[1:len(result)]}") #
            return result

def booth_multiplication(x, y):
    # receive bite string or int
    # convert x and y to binary strings if they are not already binary strings
    if isinstance(x, int):
        x = bin(x)[2:]
    if isinstance(y, int):
        y = bin(y)[2:]
    x_is_negative = False
    y_is_negative = False
    # ("x =", x, "\n"+"y =", y)
    # check if binary number is negative
    if 'b' in x or '0b' in x or '-' in x:
        x_is_negative = True
    if 'b' in y or '0b' in y or '-' in y:
        y_is_negative = True
    # print(x_is_negative, y_is_negative)
    n = max(len(x), len(y))
    x = x.zfill(n)
    y = y.zfill(n)
    # print("zfill:\nx =", x, "\n" + "y =", y)
    # print(x, y)
    arr_x = [] # split string to arr and if arr contains '-' .reverse and if 'b' remake 'b' in '1'
    arr_y = []

    for i in range(n):
        arr_x.append(str(x[i]))
        arr_y.append(str(y[i]))
    # print("arrays:\n", arr_x,arr_y)
    # connect array to number
    arr_x_binary_number = ''
    arr_y_binary_number = ''
    for i in range(n):
        arr_x_binary_number += arr_x[i]
        arr_y_binary_number += arr_y[i]
    #if binary number is negative refactor it
    if x_is_negative:
        # new reverse def function needed (eats array)
        arr_x_binary_number = binary_refacor(arr_x)
    if y_is_negative:
        # new reverse def function needed (eats array): arr_y_binary_number = new_func(arr_y)
        arr_y_binary_number = binary_refacor(arr_y)
    arr_x_negative_binary_number = ''
    print(f" arr_x_binary_number {arr_x_binary_number}")
    arr_x.insert(0, '-')

    arr_x_negative_binary_number = binary_reverse(arr_x)

    # print(arr_x_negative_binary_number)
    # print("new nums (from arrays):\n", "x =",arr_x_binary_number, "y =",arr_y_binary_number)
    # print(f"from x - negative x = {arr_x_negative_binary_number}")
    x_binary_str = ''
    y_binary_str = ''
    for i in range(max(len(arr_x_binary_number), len(arr_y_binary_number))):
        x_binary_str += arr_x_binary_number[i]
        y_binary_str += arr_y_binary_number[i]
    print(f"m = {x_binary_str} -> -m = {arr_x_negative_binary_number} -> r = {y_binary_str}")
    # booth_algo(x_binary_str, arr_x_negative_binary_number, y_binary_str)
    result = booth_algo_def(x_binary_str, arr_x_negative_binary_number, y_binary_str)
    return result
    # if


result = booth_multiplication(3,4) # 3,-4 -8, 2 # 11100000 # 11110100 logic error!
print(result)