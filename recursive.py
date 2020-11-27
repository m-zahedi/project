from time import time
import string
import random
from matplotlib import pyplot as plt

def random_protein_sequence_generator(size=50, chars=string.ascii_uppercase):
    return ''.join(random.choice(chars) for _ in range(size))

#def run_time(function, *args):
#    start_time = time.time()
#    result = function(*args)
#    return time.time() - start_time
#

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
   # list.append(a-b)
    return 1 + min(recursive_edit_distance(str1, str2, m, n - 1),  # Insert
                   recursive_edit_distance(str1, str2, m - 1, n),  # Remove
                   recursive_edit_distance(str1, str2, m - 1, n - 1)  # Replace
                   )

############length of string#############
###########################################
str1 = random_protein_sequence_generator(8)
str2 = random_protein_sequence_generator(7)
###########################################
starting_time = time()
print('minimum edit distance:',recursive_edit_distance(str1, str2, len(str1), len(str2)))
ending_time = time()
#run_time = run_time(recursive_edit_distance, str1, str2,len(str1),len(str2))
#print('run time:             ',run_time,' seconds')
print('run time             : %3f seconds'%(ending_time-starting_time))

x = []
y = []

for i in range(11):
    str1 = random_protein_sequence_generator(i)
    str2 = random_protein_sequence_generator(i)
    start = time()
    recursive_edit_distance(str1, str2, i, i)
    end = time()
    x.append(i)
    y.append(end-start)


plt.plot(x, y, linestyle='dashed')
plt.title('Recursive')
plt.xlabel('sequence size', color='b')
plt.ylabel('time (sec)', color='b')
plt.show()