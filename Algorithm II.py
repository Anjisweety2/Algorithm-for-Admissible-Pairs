"""
Input value
n : index of the icosahedral number

Return value: the n-th icosahedral number
"""
def make_icosahedral(n):
    return int(5/2*n**3-5/2*n**2+n)


"""
Input value
n : index of the dodecahedral number

Return value: the n-th dodecahedral number
"""
def make_dodecahedral(n):
    return int(9/2*n**3-9/2*n**2+n)

"""
Input values
    icos_list: a list of numbers that are sums of icosahedral numbers
    dodes_list: a list of numbers that are sums of dodecahedral numbers
    threshold: minimal value of the positive integers that we are checking
    m: maximum value of the positive integers that we are checking

Return value: Return the first integer that is between "threshold" and "m" such that
              it cannot be written as a sum of two numbers from "icos_list" and "dodes_list"
              respectively. If no such integer exists, then return None and print "no
              counterexample".
"""
def check_counterexample(icos_list, dodes_list, threshold, m):
    result = [x + y for x in icos_list for y in dodes_list]
    unique_result = list(set(result))  
    counter = False
    for i in list(range(threshold, m)):
        if i not in unique_result:
            print(i)
            counter = True
            break
    if (not counter):
        print("no counterexamples")

# Ex: (4,7)
# It suffices to check 1.666*10^6 can be written as sums of at most 4 icosahedral numbers
# and 2 dodecahedral numbers.

#1st step
all_icosahedrals = set()
for i in range(87):
    all_icosahedrals.add(make_icosahedral(i))

all_dodecahedrals = set()
for i in range(71):
    all_dodecahedrals.add(make_dodecahedral(i))


#2nd step
ico_second_step_combinations = set()
for j in all_icosahedrals:
    for i in all_icosahedrals:
        if ((i+j) <= int(1.666*10**6)):
            ico_second_step_combinations.add(i+j)

dode_second_step_combinations = set()
for j in all_dodecahedrals:
    for i in all_dodecahedrals:
        if ((i+j) <= int(1.666*10**6)):
            dode_second_step_combinations.add(i+j)

#third step
ico_third_step_combinations = set()
for j in ico_second_step_combinations:
    for i in all_icosahedrals:
        if ((i+j) <= int(1.666*10**6)):
            ico_third_step_combinations.add(i+j)

#fourth step
ico_fourth_step_combinations = set()
for j in ico_third_step_combinations:
    for i in all_icosahedrals:
        if ((i+j) <= int(1.666*10**6)):
            ico_fourth_step_combinations.add(i+j)


check_counterexample(ico_fourth_step_combinations, dode_second_step_combinations, 10000, int(1.666*10**6)) 

