from time import time
#edit distance in linear time order # O(m*n)
def dynamic_devide_and_conquer_edit_distance(string1, string2):
    #if both strings are empty, return 0
    if len(string1)==0 and len(string2==0):
        return 0
    #if string1 is empty, minimum operation is len(string2)
    if len(string1)==0:
        return len(string2)
    # if string2 is empty, minimum operation is len(string1)
    if len(string2)==0:
        return len(string1)

    dp_dc = [[0 for x in range(2)] for x in range(len(string1) + 1)]
    #print(dp)
    for i in range(len(string1) + 1):
        dp_dc[i][0] = i
    #print(dp)
    for i in range(1, len(string2) + 1):
        for j in range(0, len(string1) + 1):
            if j==0:
                dp_dc[j][i % 2] = i

            elif string1[j - 1] == string2[i - 1]:
                  dp_dc[j][i % 2] = dp_dc[j - 1][(i - 1) % 2]

            else:
                dp_dc[j][i % 2] = 1 + min(dp_dc[j][(i - 1) % 2],
                                       min(dp_dc[j - 1][i % 2],
                                       dp_dc[j - 1][(i - 1) % 2]))
    #print(dp)
    return (dp_dc[len(string1)][len(string2) % 2])
        # AAM63747 cl 6
string1 = "MASSSALALRRLLLDPFTPTRSLSQMLNFMDQVSEIPLVSATRGMGASGVRRGWNVKEKDDALHLRIDMPGLSREDVKLALEQNTLV" \
           "IRGEGETEEGEDVSGDGRRFTSRIELPEKVYKTDEIKAEMKNGVLKVVIPKIKEDERNNIRHINVD"
# AAM67165_cl_2

string2 = "MSAVAINHFFGLPETVEEERTLVIKSNGKRKRDDDESEEGSKYIRLERRLAQNLVKKFRLPEDADMASVTAKYQEGILTVVIKKLPPQPPKPKTVQIAVS"
starting_time = time()
print("minimum operations: ",dynamic_devide_and_conquer_edit_distance(string1, string2))
ending_time = time()
print('run time          : %3f seconds'%(ending_time-starting_time))