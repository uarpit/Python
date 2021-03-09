# -*- coding: utf-8 -*-
"""
Insert M in N given M and N are 32 bit binary number
between indexes j and i
"""

def bit_insrt(M,N,j,i):
    
    
    #Mask N region in M as 0's
    M_len= (len(bin(M)) - 2)
    rpad=2**(i)-1
    lpad=(1<<(M_len-j-i+1))-1 #leftportion to 1's in M
    lmask=lpad<<(j-i+1) #adding 0's for N portion in M
    lrmask=lmask << i 
    lrmask |=rpad        #adding 1's on right portion in M
    M_mask = M & lrmask  #M_mask for clearing bits in N region on M

    #rpad N with 0's
    rshift=N << i
    return bin(M_mask | rshift)
    


long=0b10000000000
short=0b10011
end=2
start=6
print(bit_insrt(long,short,start,end))
