from time import time
def recursive_edit_distance(str1, str2, m, n):
    # if length of both arrays are zero
    if m == 0 and n == 0:
        return 0
    # if length of the first array is zero
    if m == 0:
        return n
    # if length of the second array is zero
    if n == 0:
        return m

    if str1[m - 1] == str2[n - 1]:
        return recursive_edit_distance(str1, str2, m - 1, n - 1)

    return 1 + min(recursive_edit_distance(str1, str2, m, n - 1),  # Insert
                   recursive_edit_distance(str1, str2, m - 1, n),  # Remove
                   recursive_edit_distance(str1, str2, m - 1, n - 1)  # Replace
                   )


#AAM63747 cl 6
str1 =  "MASSSAL"
        #"ALRRLLLDPFTPTRSLSQMLNFMDQVSEIPLVSATRGMGASGVRRGWNVKEKDDALHLRIDMPGLSREDVKLALEQNTLV" \
        #"IRGEGETEEGEDVSGDGRRFTSRIELPEKVYKTDEIKAEMKNGVLKVVIPKIKEDERNNIRHINVD"
#AAM67165_cl_2

str2 = "MSAVA"
        #"INHFFGLPETVEEERTLVIKSNGKRKRDDDESEEGSKYIRLERRLAQNLVKKFRLPEDADMASVTAKYQEGILTVVIKKLPPQPPKPKTVQIAVS"
starting_time = time()
print('minimum operations:',recursive_edit_distance(str1, str2, len(str1), len(str2)))
ending_time = time()
print('run time          : %3f seconds'%(ending_time-starting_time))