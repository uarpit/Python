#Program to check if the string has all unique characters given that string only contains alphabets
#without using any additinal datastructures

#Approach: This program creates a list such that each position stores a character from the string
# If a character is already present at an index then it is proves non uniqueness in the string

def unq_c_strng(inpt):
    ary = []
    for i in range(0,52):
        ary.insert(i,'')
    #print(ary)
    for c in inpt:
        if ary[alpha_index(c)] == '':
            ary[alpha_index(c)] = c
        else:
            print('Duplicate charecter \'{0}\' found'.format(c))
            break;

def alpha_index(chr):
    if(chr >= 'A' and chr <= 'Z'):
        return (ord(chr) - 65)
    elif(chr >= 'a' and chr <= 'z'):
        return (ord(chr) - 71)

unq_c_strng('Ramjane')
