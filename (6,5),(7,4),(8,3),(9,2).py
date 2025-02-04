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
    print("the pairs (6,5),(7,4),(8,3) and (9,2) are checked and the result is :",len(lst) == m - threshold + 1)

# Ex: (6,5),(7,4),(8,3),(9,2)
# It suffices to check integers between 10000 and 5.74*10^5 can be written as sums of at most 4 icosahedral numbers
# and 2 dodecahedral numbers.

#1st step
all_icosahedrals = set()
for i in range(61):
    all_icosahedrals.add(make_icosahedral(i))

all_dodecahedrals = set()
for i in range(50):
    all_dodecahedrals.add(make_dodecahedral(i))


#2nd step
ico_second_step_combinations = set()
for j in all_icosahedrals:
    for i in all_icosahedrals:
        if ((i+j) <= int(5.74*10**5)):
            ico_second_step_combinations.add(i+j)

dode_second_step_combinations = set()
for j in all_dodecahedrals:
    for i in all_dodecahedrals:
        if ((i+j) <= int(5.74*10**5)):
            dode_second_step_combinations.add(i+j)


#third step
ico_third_step_combinations = set()
for j in ico_second_step_combinations:
    for i in all_icosahedrals:
        if ((i+j) <= int(5.74*10**5)):
            ico_third_step_combinations.add(i+j)

#fourth step
ico_fourth_step_combinations = set()
for j in ico_third_step_combinations:
    for i in all_icosahedrals:
        if ((i+j) <= int(5.74*10**5)):
            ico_fourth_step_combinations.add(i+j)
            
#last step
final_list = set()
for j in dode_second_step_combinations:
    for i in ico_fourth_step_combinations:
        if (10000 <= (i+j) <= int(5.74*10**5)):
            final_list.add(i+j)

check_counter(10000, int(5.74*10**5), final_list)
