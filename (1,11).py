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
    m : maximum value of the positive integers that we are checking
    threshold: minimal value of the positive integers that we are checking
    lst: complete list of all possible sums after five rounds
Return value: True if all numbers in the given range are in "lst"
              False if there exists any counterexample.
"""
def check_counter(threshold, m, lst):
    print("the pair (1,11) is checked and the result is :",len(lst) == m - threshold + 1)
    for j in range(threshold, m+1):
        if j not in lst:
            print(j)
        
# Ex: (1,11)
# It suffices to check integers between 12000 and 2.1*10^5 can be written as sums of at most 1 icosahedral number
# and 5 dodecahedral numbers.

#1st step
all_icosahedrals = set()
for i in range(44):
    all_icosahedrals.add(make_icosahedral(i))

all_dodecahedrals = set()
for i in range(36):
    all_dodecahedrals.add(make_dodecahedral(i))


#2nd step
dode_second_step_combinations = set()
for j in all_dodecahedrals:
    for i in all_dodecahedrals:
        if ((i+j) <= int(2.1*10**5)):
            dode_second_step_combinations.add(i+j)


#third step
dode_third_step_combinations = set()
for j in dode_second_step_combinations:
    for i in all_dodecahedrals:
        if ((i+j) <= int(2.1*10**5)):
            dode_third_step_combinations.add(i+j)

#fourth step
dode_fourth_step_combinations = set()
for j in dode_third_step_combinations:
    for i in all_dodecahedrals:
        if ((i+j) <= int(2.1*10**5)):
            dode_fourth_step_combinations.add(i+j)

#fifth step
dode_fifth_step_combinations = set()
for j in dode_fourth_step_combinations:
    for i in all_dodecahedrals:
        if ((i+j) <= int(2.1*10**5)):
            dode_fifth_step_combinations.add(i+j)          
#last step
final_list = set()
for j in all_icosahedrals:
    for i in dode_fifth_step_combinations:
        if (12000 <= (i+j) <= int(2.1*10**5)):
            final_list.add(i+j)

check_counter(12000, int(2.1*10**5), final_list)
