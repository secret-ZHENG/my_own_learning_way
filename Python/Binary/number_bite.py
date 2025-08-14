'''
count the number of bits that are set to 1 in an integer
'''
# brute-force algorithm
def count_bits_1(x):
    number_bits = 0
    while x :
        number_bits += x & 1#
        x >>= 1
    return number_bits


if __name__ == "__main__":
    x = int(input('Input an integer: '))
    print(bin(x)[2:])
    print(count_bits_1(x))
