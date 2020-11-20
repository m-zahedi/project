from time import time
def dynamic_edit_distance(str1, str2):
    dynamic_programming_array = [[0 for x in range(len(string2) + 1)] for x in range(len(string1) + 1)]
    for a in range(len(string1) + 1):
        for b in range(len(string2) + 1):

            # if length of the string1 is zero
            # minimum operation is length of string2
            if a == 0:
                dynamic_programming_array[a][b] = b
            # if length of the second array is zero
            # minimum operation is length of string1
            elif b == 0:
                dynamic_programming_array[a][b] = a

            elif str1[a - 1] == str2[b - 1]:
                dynamic_programming_array[a][b] = dynamic_programming_array[a - 1][b - 1]

            else:
                dynamic_programming_array[a][b] = 1 + min(dynamic_programming_array[a][b - 1],
                                   dynamic_programming_array[a - 1][b],
                                   dynamic_programming_array[a - 1][b - 1])
    return dynamic_programming_array[len(string1)][len(string2)]

#AAM63747 cl 6
string1 =  "MASSSALALRRLLLDPFTPTRSLSQMLNFMDQVSEIPLVSATRGMGASGVRRGWNVKEKDDALHLRIDMPGLSREDVKLALEQNTLV" \
        "IRGEGETEEGEDVSGDGRRFTSRIELPEKVYKTDEIKAEMKNGVLKVVIPKIKEDERNNIRHINVD"
#AAM67165_cl_2

string2 = "MSAVAINHFFGLPETVEEERTLVIKSNGKRKRDDDESEEGSKYIRLERRLAQNLVKKFRLPEDADMASVTAKYQEGILTVVIKKLPPQPPKPKTVQIAVS"
starting_time = time()
print('minimum operations:',dynamic_edit_distance(string1, string2))
ending_time = time()
print('run time          : %3f seconds'%(ending_time-starting_time))