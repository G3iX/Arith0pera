# - d) Booth's algorithm
# from calc import binary_array_column_sum
def binary_refacor(input_array):
    for i in range(len(input_array)):
        if input_array[i] == 'b':
            input_array[i] = '1'
    #result = ''
    #for i in input_array:
    #    result += i
    return input_array

def binary_array_sum(input_array):
    # Find the maximum length of the binary strings in the array
    max_len = max(len(x) for x in input_array)
    print("max_len =",max_len)
    # Pad each binary string with leading zeroes to make them the same length
    input_array = [x.zfill(max_len) for x in input_array]
    print("input_array =", input_array )
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
    # Convert the result to a binary string and return it
    result = "".join(str(x) for x in result).lstrip("0")
    print("result =", result)
    return result

def binary_reverse(input_array):
    for i in range(len(input_array)-1):
        print(input_array)
        print(i)
        if input_array[i] == '-':
            input_array.pop(i)
            input_array.reverse()  # # # # # # # # # # # test!
            temp = ''
            negative_input_array = []
            for i in input_array:
                temp += i
            try:
                negative_input_array = binary_array_sum([temp, "1"])
            except:
                print("aboba error")
    return negative_input_array

def booth_algo(m, negative_m ,r):
    n = max(len(m), len(r))
    toll = n * 2 + 1

    A = m.ljust(toll, '0')
    S = negative_m.ljust(toll, '0')
    P = r.zfill(toll - 1)
    P += '0'
    print(' '+ A,'\n', S, '\n', P)
    temp = list(P)
    i = 0
    for i in range(len(temp),0,-2):
        print(temp[i-1], temp[i-2])
        # print(temp[i], temp[i-1])
    while True:
        try:
            took_last = temp.pop(len(temp))
            pre_last = temp[len(temp)]
            if took_last+pre_last=="00":
                if temp[0] == '0':
                    temp.insert(0,'0')
                else:
                    temp.insert(0,'1')
            elif took_last+pre_last=="01":
                print("idk")
            elif took_last + pre_last == "10":
                print("'10' chance probe:")
                P = binary_array_sum([P, S])
                print("P == ", P) # 1110 1001 1
                temp.pop(len(temp)) # Arithmetical - to right
                if temp[0] == '0':
                    temp.insert(0, '0')
                else:
                    temp.insert(0, '1')
            elif took_last + pre_last == "11":
                temp.pop(len(temp))  # Arithmetical - to right
                if temp[0] == '0':
                    temp.insert(0, '0')
                else:
                    temp.insert(0, '1')
                break;
            result = ''
            for i in temp:
                result += i
            print(result)
            return result
        except:
            print("break datebajo")
            break;
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
    print("zfill:\nx =", x, "\n" + "y =", y)

    arr_x = [] # split string to arr and if arr contains '-' .reverse and if 'b' remake 'b' in '1'
    arr_y = []

    for i in range(n):
        arr_x.append(str(x[i]))
        arr_y.append(str(y[i]))
    print("arrays:\n", arr_x,arr_y)
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
    arr_x.insert(0, '-')

    arr_x_negative_binary_number = binary_reverse(arr_x)


    print("new nums (from arrays):\n", "x =",arr_x_binary_number, "y =",arr_y_binary_number)
    print(f"from x - negative x = {arr_x_negative_binary_number}")
    x_binary_str = ''
    y_binary_str = ''
    for i in range(max(len(arr_x_binary_number), len(arr_y_binary_number))):
        x_binary_str += arr_x_binary_number[i]
        y_binary_str += arr_y_binary_number[i]
    print(x_binary_str, arr_x_negative_binary_number, y_binary_str)
    booth_algo(x_binary_str, arr_x_negative_binary_number, y_binary_str)
    # if


booth_multiplication(3,-4)
