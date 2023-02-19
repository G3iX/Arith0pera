
def booth_algorithm(x, y):
    # convert x and y to binary strings if they are not already binary strings
    if isinstance(x, int):
        x = bin(x)[2:]
    if isinstance(y, int):
        y = bin(y)[2:]
    # same length
    n = max(len(x), len(y))
    result = "0" * n

# example we take 3 * -4 = [0011] * [1100] = [1111 0100]
# we take multiplicand[3] and reverse it  0011 [3] => 1101 [-3] ?
"""
print(bin(-4)[2:])
print("{:b}".format(-4))
print(bin(-4)[2:].replace("b", "1"))
print("--------------")
print(bin(3)[2:])
print("{:b}".format(3))
print(bin(3)[2:].replace("b", "1"))
print("--------------")
print(bin(-3)[2:])
print("{:b}".format(-3))
print(bin(-3)[2:].replace("b", "10"))"""


def decToBinary(n):
    # Size of an integer is
    # assumed to be 32 bits
    res = ""
    for i in range(31, -1, -1):
        k = n >> i
        if k & 1:
            res += "1" # print("1", end="")
        else:
            res += "0" # print("0", end="")
    return  res

# Driver Code
n = -10
result = decToBinary(n)
# print(result[2:]) # show starting from beginning
# print(result[:35]) # show starting from end
#print(str(n))
print(result)
if len(str(n)) <= 2 and '-' in str(n):
    amount = 4
    #print(result[len(result)-amount:])


n2 = 4
result2 = decToBinary(n2)
# print(result[2:]) # show starting from beginning
# print(result[:35]) # show starting from end
#print(str(n2))
# print(result2)
if len(str(n2)) <= 2 or '-' in str(n2) and len(str(n2)) == 2:
    amount = 4
    #print(result2[len(result2)-amount:])

from calc import binary_multiplication
# xol = 1
# varib = binary_multiplication(-3,4)
# print(varib[xol:])
# print(int(varib[xol:],2))

def int_to_binary(n):
    num = n
    if n == 0:
        return [0]
    bits = []
    while n != 0:
        if n < 0:
            bits.append(1)
            # result += str(1)
            n = abs(n) - 1
        else:
            bits.append(n % 2)
            # result += str(n%2)
            n //= 2
    # print(bits)
    if 10 > num > 0:
        bits.append(0)
        bits.append(0)
    elif num >= 10:
        bits.append(0)
    if -10 < num < 0:
        bits.append(1)
    #elif num <= -10:
    #    bits.append(1)
    bits.reverse()


    # print(result)
    # return result[::-1]
    return bits

print(int_to_binary(-3)) # 0, 1, 0, 1, 0 = 1010; [10] 0 1010 = [-10] 10101 + 1 ( 1 0110 )

# need to read negative numbers ? will just do '-' in the beginning of the string, because inversion and etc. -> too long
# if strting