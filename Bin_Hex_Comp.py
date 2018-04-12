#Program comparares two given binary and Hexadecimal strings to return True if they are equal
#and False if they are not equal


def string_comp(binry, hex):
    n1 = con_to_base(str(binry), 2)
    n2 = con_to_base(str(hex), 16)
    if n1 < 0 or n2 < 0:
        print('False')
    else:
        if n1 == n2:
            print('True')
        else:
            print('False')


def con_to_base(inpt, base):
    length = len(inpt)
    value = 0
    for i in range(0, length):
        value += int(inpt[length - 1 - i], base) * base ** i
    return value

string_comp(1011,'A')