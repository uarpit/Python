#Given two strings write a program to check if one is a permutation of the other

#Approach: Create two lists which will store 256 ascii character count
#increment the count at index of each charecter and compare two lists to be the same

def strng_permt(str1, str2):
    ary1 = []
    ary2 = []
    for i in range(0, 256):
        ary1.insert(i, 0)
    for i in range(0, 256):
        ary2.insert(i, 0)

    for c in str1:
        ary1[ord(c) - 1] = ary1[ord(c) - 1] + 1
    for c in str2:
        ary2[ord(c) - 1] += 1

    if ary1 == ary2:
        print('\'{}\' is a permutation of \'{}\''.format(str1, str2))
    else:
        print('\'{}\' is not a permutation of \'{}\''.format(str1, str2))


strng_permt('tic tac toe', 'ttt iao cce')
