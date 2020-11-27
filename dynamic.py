from time import time
import string
import random
from matplotlib import pyplot as plt

def random_protein_sequence_generator(size=50, chars=string.ascii_uppercase):
    return ''.join(random.choice(chars) for _ in range(size))

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
##########length of string###############
###########################################
string1 = random_protein_sequence_generator(200)
string2 = random_protein_sequence_generator(200)
###########################################
starting_time = time()
print('minimum edit distance:',dynamic_edit_distance(string1, string2))
ending_time = time()
print('run time             : %3f seconds'%(ending_time-starting_time))
print('plotting...')


x = []
y = []

for i in range(201):
    string1 = random_protein_sequence_generator(i)
    string2 = random_protein_sequence_generator(i)
    start = time()
    dynamic_edit_distance(string1, string2)
    end = time()
    x.append(i)
    y.append(end-start)


plt.plot(x, y, linestyle='dashed')
plt.title('Dynamic')
plt.xlabel('sequence size', color='b')
plt.ylabel('time (sec)', color='b')
plt.show()