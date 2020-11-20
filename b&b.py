import math
from time import time

def branch_and_bound_edit_distance(string1, string2, cost=0, bound=0):

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

    #compare the cost of string1[len(string1) - 1] and string2[len(string2) - 1]
    cost_of_e = abs((len(string1) - 1) - (len(string2) - 1))
    if string1[-1] == string2[-1]:
        cost_of_f = cost_of_e + cost - 1
    else:
        cost_of_f = cost_of_e + cost
    ad1, ad2, ai1, ai2, ac1, ac2 = [], [], [], [], [], []

    #if upper bound ===> deletion
    if bound >= cost_of_b:

        deletion,ad1,ad2  = branch_and_bound_edit_distance(string1[:-1], string2, cost + 1, bound)  # Deletion
        deletion += 1
    else:
        deletion = 1000000

    if bound >= cost_of_d:
        #Insertion branch for algo
        insertion,ai1,ai2 = branch_and_bound_edit_distance(string1, string2[:-1], cost + 1, bound)  # Insertion
        insertion += 1
    else:
        insertion = 1000000
    if bound >= cost_of_e:
        #3 branch compare the last two protein strings
        if (string1[-1] != string2[-1]):
            substitution,ac1,ac2 = branch_and_bound_edit_distance(string1[:-1], string2[:-1], cost + 1, bound)
            substitution += 1
        else:
            substitution,ac1,ac2 = branch_and_bound_edit_distance(string1[:-1], string2[:-1], cost, bound)
    else:
        substitution = 1000000

    #store the value of the operations: deletion, insertion and substitution in an array
    values = [deletion, insertion, substitution]
    minval = min(deletion, insertion, substitution)
    if values.index(minval) == 0:
        ad1 = ad1 + [string1[-1]]
        ad2 = ad2 + ["#"]
        return minval, ad1, ad2
    elif values.index(minval) == 1:
        ai1 = ai1 + ["#"]
        ai2 = ai2 +[string2[-1]]
        return minval, ai1, ai2
    else:
        ac1 = ac1 + [string1[-1]]
        ac2 = ac2 + [string2[-1]]
        return minval, ac1, ac2

#the needed steps taken to compute the Edit distance is described here
string1 = "ASDADDF"
string2 = "SDFFF"
starting_time=time()
result, a1, a2  = branch_and_bound_edit_distance(string1,string2,0,max(len(string1),len(string2)))
ending_time=time()
print('alignment         : ', a2)
print('final alignment   : ', a1)
print('minimum operations: ', result)
print('run time          :  %3f seconds'%(ending_time-starting_time))