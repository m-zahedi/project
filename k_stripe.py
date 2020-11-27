import numpy as np
import random
import string
import time
from matplotlib import pyplot as plt
x = []
y = []


#plt.plot(x, y, linestyle='dashed')
#plt.title('Branch and Bound')
#plt.xlabel('sequence size', color='b')
#plt.ylabel('time (sec)', color='b')
#plt.show()

def random_protein_sequence_generator(size=200, chars=string.ascii_uppercase):

    return ''.join(random.choice(chars) for _ in range(size))

for i in range(200):
    str1 = random_protein_sequence_generator(i)
    str2 = random_protein_sequence_generator(i)

def running(function, *args):

    starting_time = time.time()
    result = function(*args)
    return time.time() - starting_time, result

# building a 2d numpy array
#assigning zero to the indexes of the first row and column

def array_2d(string1, string2):

    array_2d = np.empty([len(string1) + 1, len(string2) + 1])

    array_2d[:] = np.inf
    # assigning zero to the indexes of the first row
    array_2d[0] = np.arange(array_2d.shape[1])
    b = 0
    # assigning zero to the indexes of the first column
    for j in array_2d:

        j[0] = b
        b += 1
    return array_2d

def k_strip(string1, string2):

    value = 1
    # if value < 1
    if value > min((len(string1)), (len(string2))) or value < 1:
        return 0

    arr = array_2d(string1, string2)

    index = - (value - 2)

    cap = value + 1 + abs(len(string1) - len(string2))
    # searchin around the diagonal

    for i in range(1, arr.shape[0]):

        for j in range(max(1, index), cap):
            # add
            first = arr[i - 1, j] + 1
            # remove
            second = arr[i, j - 1] + 1
            # replace
            if string1[i - 1] == string2[j - 1]:

                third = arr[i - 1, j - 1]
            else:
                # add
                third = arr[i - 1, j - 1] + 1

            # assign minimum value
            arr[i][j] = min(first, second, third)

        index += 1
        if cap < arr.shape[1]:
            cap += 1
    # zero =0, starting the Alignment
    zero = 0
    mm = np.c_[[zero] * len(arr[:]), arr]
    indx = np.r_[[[zero] * len(mm[1, :])], mm]

    trace_back = [[' ' for y in range(len(string2) + 2)] for x in range(len(string1) + 2)]
    trace_back[1][1] = 0

    for i in range(2, len(string1) + 2):

        trace_back[i][0] = string1[i - 2]

    for j in range(2, len(string2) + 2):

        trace_back[0][j] = string2[j - 2]

    for i in range(2, len(string1) + 2):

        trace_back[i][1] = '|'

    for j in range(2, len(string2) + 2):
        trace_back[1][j] = '_'

    for i in range(2, len(string1) + 2):

        for j in range(2, len(string2) + 2):

            vrt = indx[i - 1][j] + 1            # remove on the vertical

            hrz = indx[i][j - 1] + 1           # add on the horizontal
            if string1[i - 2] == string2[j - 2]:

                dgnl = indx[i - 1][j - 1]
            else:

                dgnl = indx[i - 1][j - 1] + 1             # replace along the dialgonal

            minimum = min(dgnl, vrt, hrz)
            indx[i][j] = minimum

            if minimum == dgnl:
                trace_back[i][j] = 'bn'
            elif minimum == vrt:
                trace_back[i][j] = '|'
            else:
                trace_back[i][j] = '_'
    w = ""
    s = ""
    t = ""

    i = len(string1) + 1
    j = len(string2) + 1
    while not (i == 1 and j == 1):
        c = trace_back[i][j]
        if c == '|':
            w += string1[i - 2] + ' '
            s += '_' + ' '
            t += ' ' + ' '
            i = i - 1
        elif c == 'bn':
            w += string1[i - 2] + ' '
            s += string2[j - 2] + ' '
            if string1[i - 2] == string2[j - 2]:
                t += '|' + ' '
            else:
                t += ' ' + ' '
            i = i - 1
            j = j - 1
        else:
            w += '_' + ' '
            s += string2[j - 2] + ' '
            t += ' ' + ' '
            j = j - 1

    return arr[arr.shape[0] - 1][arr.shape[1] - 1], arr, w[::-1], t[::-1], s[::-1]
##########length of string###############
###########################################
string1 = random_protein_sequence_generator(200)
string2 = random_protein_sequence_generator(200)
###########################################
print('string 1 : ' + string1)
print('string 2 : ' + string2)
final = running(k_strip, string1, string2)
print(final[1][1])
print("_____________________________________________________________________________________________________________")
print("{} {}".format("minimum edit distance :", int(final[1][0])))
print("run time              : %s seconds" % final[0])


run = []
size = [50, 100, 150, 175,200]
s1 = random_protein_sequence_generator(50)
s2 = random_protein_sequence_generator(50)
final0 = running(k_strip, s1, s2)
run.append(final0[0])

s1 = random_protein_sequence_generator(100)
s2 = random_protein_sequence_generator(100)
final0 = running(k_strip, s1, s2)
run.append(final0[0])

s1 = random_protein_sequence_generator(150)
s2 = random_protein_sequence_generator(150)
final0 = running(k_strip, s1, s2)
run.append(final0[0])
s1 = random_protein_sequence_generator(175)
s2 = random_protein_sequence_generator(175)
final0 = running(k_strip, s1, s2)
run.append(final0[0])
s1 = random_protein_sequence_generator(200)
s2 = random_protein_sequence_generator(200)
final0 = running(k_strip, s1, s2)
run.append(final0[0])

plt.plot(size, run, linestyle='dashed')
plt.title('Stripe K')
plt.xlabel('sequence size', color='b')
plt.ylabel('time (sec)', color='b')
plt.show()
