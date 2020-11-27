from time import time
import string
import random
from matplotlib import pyplot as plt

def random_protein_sequence_generator(size=200, chars=string.ascii_uppercase):

    return ''.join(random.choice(chars) for _ in range(size))

string1 = random_protein_sequence_generator(11)

string2 = random_protein_sequence_generator(11)


def branch_and_bound_edit_distance(string1, string2, cost=0, bound=0):

    #plt.plot(x, y, linestyle='dashed')
    #plt.title('Branch and Bound')

    #plt.xlabel('sequence size', color='b')
    #plt.ylabel('time (sec)', color='b')
    #plt.show()

    #if string 1 is empty
    if len(string1) == 0:
        return len(string2), ["#" for i in range(len(string2))], [string2[i] for i in range(len(string2))]

    #if string 2 is empty
    if len(string2) == 0:
        return len(string1), [string1[i] for i in range(len(string1))], ["#" for i in range(len(string1))]


    cost_of_a = abs((len(string1) - 1) - len(string2))
    cost_of_b = cost_of_a + cost
    cost_of_c = abs(len(string1) - (len(string2) - 1))
    cost_of_d = cost_of_c + cost

   # if values.index(minval) == 0:
   #     ad1 = ad1 + [string1[-1]]
   #     ad2 = ad2 + ["#"]
   #     return minval, ad1, ad2

    #compare the cost of string1[len(string1) - 1] and string2[len(string2) - 1]
    cost_of_e = abs((len(string1) - 1) - (len(string2) - 1))
    if string1[-1] == string2[-1]:
        cost_of_f = cost_of_e + cost - 1
    else:
        cost_of_f = cost_of_e + cost
    ad1, ad2, ai1, ai2, ac1, ac2 = [], [], [], [], [], []

    #if upper bound ===> deletion
    if bound >= cost_of_b:
      #  insertion,ai1,ai2 = branch_and_bound_edit_distance(string1, string2[:-1], cost + 1, bound)  # Insertion
      #  insertion += 1
        remove,ad1,ad2  = branch_and_bound_edit_distance(string1[:-1], string2, cost + 1, bound)  # Deletion
        remove += 1
    else:
        remove = 1000000

    if bound >= cost_of_d:
        #Insertion branch for algo
        add,ai1,ai2 = branch_and_bound_edit_distance(string1, string2[:-1], cost + 1, bound)  # Insertion
        add += 1
    else:
        add = 1000000
    if bound >= cost_of_e:
        #3 branch compare the last two protein strings
        if (string1[-1] != string2[-1]):
            replace,ac1,ac2 = branch_and_bound_edit_distance(string1[:-1], string2[:-1], cost + 1, bound)
            replace += 1
        else:
            replace,ac1,ac2 = branch_and_bound_edit_distance(string1[:-1], string2[:-1], cost, bound)
    else:
        replace = 1000000


    #store the value of the operations: deletion, insertion and substitution in an array
    amount = [remove, add, replace]
    minimum = min(remove, add, replace)
    if amount.index(minimum) == 0:
        ad1 = ad1 + [string1[-1]]
        ad2 = ad2 + ["#"]
        return minimum, ad1, ad2
    elif amount.index(minimum) == 1:
        ai1 = ai1 + ["#"]
        ai2 = ai2 +[string2[-1]]
        return minimum, ai1, ai2
    else:
        ac1 = ac1 + [string1[-1]]
        ac2 = ac2 + [string2[-1]]
        return minimum, ac1, ac2

#the needed steps taken to compute the Edit distance is described here

starting_time=time()
result, a1, a2  = branch_and_bound_edit_distance(string1,string2,0,max(len(string1),len(string2)))
ending_time=time()
print('alignment             : ', a2)
print('final alignment       : ', a1)
print('minimum edit distance : ', result)
print('run time              :  %3f seconds'%(ending_time-starting_time))
print("_____________________________________________________________________________________________________________")
print("plotting...")
x = []
y = []

for i in range(12):
    str1 = random_protein_sequence_generator(i)
    str2 = random_protein_sequence_generator(i)
    start = time()
    branch_and_bound_edit_distance(str1, str2, 0, max(len(str1),len(str2)))
    end = time()
    x.append(i)
    y.append(end-start)


plt.plot(x, y, linestyle='dashed')
plt.title('Branch and Bound')
plt.xlabel('sequence size', color='b')
plt.ylabel('time (sec)', color='b')
plt.show()