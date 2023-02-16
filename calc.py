
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
    x = x.zfill(n) # make same str len
    y = y.zfill(n)
    print("x = ", x, "; y = ", y)
    # perform multiplication as done in columns
    # result = "0" * (2 * n)
    result = ""
    #print("result '0'*(2*n) = ", result)
    temp_arr = []
    index = 1
    for i in y:
        if i == "1":
            temp = x + (n-index)*"0"
            temp_arr.append(temp)
        index += 1
    print(temp_arr)
    #for i in range(n): # INCORRECT !
    #    for j in range(n):
    #        if y[n - 1 - j] == "1": # each time we see 1 in y.binary number we do this


                # result += bin(int( (str(int(x, 2)),"0"*j),2 ))

                # temp = str(x) + "0"*j
                # int_temp = int(temp)
                # result = result + bin(int_temp)[2:]

                # temp = int(result[2 * n - i - j - 1], 2) + int(x[n - 1 - i], 2)
                # result = result[:2 * n - i - j - 1] + bin(temp)[2:].zfill(1) + result[2 * n - i - j:]
    #print("result_start = ", result)
    # remove leading zeroes from the result and return it
    print("result = ", result.lstrip("0") ) # or "0"
    return result.lstrip("0") #  or "0"

binary_multiplication("1100", "1111")
print("------------")
binary_multiplication("1010", "101")
# x = binary_multiplication(13, 5) # 01000001 not 001111001
# print(int(x,2))
