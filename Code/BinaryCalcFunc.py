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
        column_sum = sum(int(x[i]) for x in input_array) + result[i + 1]
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

def binary_format(number_to_transform, bits_shown):
    try:
        s = bin(number_to_transform & int("1"*bits_shown, 2))[2:]
    except:
        print(f"error in transform {number_to_transform} to binary string in 'binary_format' function")
    return ("{0:0>%s}" % bits_shown).format(s)


def negative_binary_to_decimal(binary):
    # binary = "".join(lambda x: if x == "1" for x in binary)
    binary = binary.replace("0","x")
    binary = binary.replace("1", "0")
    binary = binary.replace("x", "1")
    # print(f"binary:{binary}")
    binary = int(binary) + 1
    decimal, i = 0, 0
    while (binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary // 10
        i += 1
    return decimal