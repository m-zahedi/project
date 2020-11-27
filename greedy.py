from time import time
import string
import random
import math
from matplotlib import pyplot as plt

def swap(str1, str2):
    return string2, string1

def random_protein_sequence_generator(size=200, chars=string.ascii_uppercase):
    return ''.join(random.choice(chars) for _ in range(size))
print("_____________________________________________________________________________________________________________")
def greedy_edit_distance(string1, string2):

    minimum_edit_distance = math.inf
    #if both strings are empty
    if len(string1) == 0 and len(string2) == 0:
        return 0
    #if string1 is empty
    if len(string1) == 0:
        return string2

    #if string2 is empty
    if len(string2) == 0:
        return string1

    if len(string1) > len(string2):
        string1, string2 = swap(string1, string2)

    # 1: shift string2 on string1 to find maximum of overlapped characters
    # first len(string1)/2 chars of string 2 shifts on last len(string1)/2 chars of string 1
    str1_last_chars = int(len(string1) / 2)

    for i in range(str1_last_chars, -1, -1):
        str2 = i * "#" + string2
        difference = len(str2) - len(string1)
        str1 = string1 + difference * "#"
        n = 0
        for a, b in zip(str1, str2):
            if a != b: n += 1
        if n < minimum_edit_distance:
            minimum_edit_distance = n
            string1_alignment = str1
            string2_alignment = str2
    # 2: shift string1 on string2 to find maximum of overlapped characters
    #first len(string1)/2 chars  of string1 shifts on  last len(string1)/2 chars of string 2
    str2_last_chars = int(len(string2) - len(string1) / 2) + 1
    for j in range(1, str2_last_chars):

        maximum = max(len(str1), len(string2))
        str2 = string2 + "#" * (maximum - len(string2))
        str1 = j * "#" + string1
        str1 = str1 + "#" * (maximum - len(str1))

        m = 0
        for a, b in zip(str1, str2):
            if a != b: m += 1
        if m < minimum_edit_distance:
            minimum_edit_distance = m
            string1_alignment = str1
            string2_alignment = str2
  #  print("_____________________________________________________________________________________________________________")
  #  print("\nstring1              : " + string1)
  #  print("string1 alignment      : " + string1_alignment)
  #  print("final   alignment      : " + string2_alignment)
  #  print("_____________________________________________________________________________________________________________")
    return string1, string1_alignment, string2_alignment, minimum_edit_distance


############length of string#############
###########################################
string1 = random_protein_sequence_generator(200)
string2 = random_protein_sequence_generator(200)
###########################################
starting_time = time()
a1, a2, a3, result = greedy_edit_distance(string1, string2)
print("string1              : ", a1)
print("string1 alignment    : ", a2)
print("final alignment      : ", a3)
print("minimum edit distance: ",result)
ending_time = time()

print('run time             : %3f seconds'%(ending_time-starting_time))
print("_____________________________________________________________________________________________________________")
print("plotting...")


x = []
y = []

for i in range(201):
    string1 = random_protein_sequence_generator(i)
    string2 = random_protein_sequence_generator(i)
    start = time()
    greedy_edit_distance(string1, string2)
    end = time()
    x.append(i)
    y.append(end-start)


plt.plot(x, y, linestyle='dashed')
plt.title('Greedy')
plt.xlabel('protein sequence size', color='b')
plt.ylabel('time (sec)', color='b')
plt.show()