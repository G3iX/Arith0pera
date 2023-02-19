# done multiplication in a column (but then received another task, Booth's algorithm)
# Ver 3 - Working
def binary_array_column_sum(input_array):
    # Find the maximum length of the binary strings in the array
    max_len = max(len(x) for x in input_array)
    print("max_len =",max_len)
    # Pad each binary string with leading zeroes to make them the same length
    input_array = [x.zfill(max_len) for x in input_array]
    print("input_array =", input_array )
    # Initialize the result as a list of zeroes
    result = [0] * (max_len + 1)
    print("result =", result)
    # Add up the binary numbers as done in columns
    for i in range(max_len - 1, -1, -1):
        column_sum = sum(int(x[i]) for x in input_array) + result[i + 1]
        # print("column_sum = ", result)
        result[i + 1] = column_sum % 2
        result[i] += column_sum // 2
        # print("result num = ", result)
    # Convert the result to a binary string and return it
    result = "".join(str(x) for x in result).lstrip("0")
    return result

# Ver 1 - NOT Working
def binary_addition(input_array):
    if len(input_array) < 2:
        return input_array[0]
    result = ""
    for i in range(0, len(input_array),1): # [::-1]
        temp = ""
        try:
            print("i = ", input_array[i])  # bin(int(i,2))[2:])
            x_1 = input_array[i][::-1]
            y_1 = input_array[i+1][::-1]
            # print()
            for j in x_1:
                temp = j
            # CRINGE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        except:
            return None

# Ver 2 - Working
def binary_array_sum(arr):
    total = sum(int(x, 2) for x in arr)
    return bin(total)[2:]
def binary_multiplication(x, y):
    # convert x and y to binary strings if they are not already binary strings
    if isinstance(x, int):
        x = bin(x)[2:]
    if isinstance(y, int):
        y = bin(y)[2:]
    print("x start = ", x, "; y start = ", y)
    # pad x and y with leading zeroes to make them the same length
    n = max(len(x), len(y))
    print("n = ", n)
    # make same strings length
    x = x.zfill(n)
    y = y.zfill(n)
    print("x = ", x, "; y = ", y)
    # perform multiplication as done in columns
    temp_arr = []
    index = 1
    for i in y:
        if i == "1":
            temp = x + (n-index)*"0"
            temp_arr.append(temp)
        index += 1
    temp_arr.reverse()
    return temp_arr

print(binary_array_column_sum(binary_multiplication("1100", "1111")))