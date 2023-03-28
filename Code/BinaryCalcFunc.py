def binary_array_sum(input_array, we_need_string, if_output_array_in_string): # unoptimized option, i'll try to delete it after
    # Find the maximum length of the binary strings in the array
    max_len = max(len(x) for x in input_array)
    # Pad each binary string with leading zeroes to make them the same length
    input_array = [x.zfill(max_len) for x in input_array]
    # Initialize the result as a list of zeroes
    result = [0] * (max_len + 1)
    for i in range(max_len - 1, -1, -1):
        column_sum = sum(int(x[i]) for x in input_array) + result[i + 1]
        result[i + 1] = column_sum % 2
        result[i] += column_sum // 2
    if we_need_string:      # Convert the result to a binary string and return it
        result = "".join(str(x) for x in result).lstrip("0")
        return result
    else:                   # Convert the result to an array and return it
        if if_output_array_in_string:
            string_result = []
            for i in result:
                string_result.append(str(i))
            string_result.pop(0)
            return string_result
        return result

def binary_subtraction(x, y):
    x_int = int(x, 2)
    y_int = int(y, 2)
    result_int = x_int - y_int
    result_str = binary_format(result_int,16)
    max_len = max(len(x), len(y), len(result_str))
    result_str = result_str.zfill(max_len)
    return result_str

def binary_format(number_to_transform, bits_shown):
    try:
        s = bin(number_to_transform & int("1"*bits_shown, 2))[2:]
    except:
        print(f"error in transform {number_to_transform} to binary string in 'binary_format' function")
    return ("{0:0>%s}" % bits_shown).format(s)


def negative_binary_to_decimal(binary):
    binary = binary.replace("0","x")
    binary = binary.replace("1", "0")
    binary = binary.replace("x", "1")
    binary = int(binary) + 1
    decimal, i = 0, 0
    while (binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary // 10
        i += 1
    return decimal

def binary_to_decimal(binary):
    binary = int(binary)
    decimal, i = 0, 0
    while (binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary // 10
        i += 1
    return decimal