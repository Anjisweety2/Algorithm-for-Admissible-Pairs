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
    print("the pair (10,1) is checked and the result is :",len(lst) == m - threshold + 1)

# Ex: (6,5),(7,4),(8,3),(9,2)
# It suffices to check positive integers between 10000 and 2.13*10^6 can be written as sums of at most 5 icosahedral numbers
# and 1 dodecahedral number.

#1st step
all_icosahedrals = set()
for i in range(95):
    all_icosahedrals.add(make_icosahedral(i))

all_dodecahedrals = set()
for i in range(78):
    all_dodecahedrals.add(make_dodecahedral(i))


#2nd step
ico_second_step_combinations = set()
for j in all_icosahedrals:
    for i in all_icosahedrals:
        if ((i+j) <= int(2.13*10**6)):
            ico_second_step_combinations.add(i+j)

#third step
ico_third_step_combinations = set()
for j in ico_second_step_combinations:
    for i in all_icosahedrals:
        if ((i+j) <= int(2.13*10**6)):
            ico_third_step_combinations.add(i+j)

#fourth step
ico_fourth_step_combinations = set()
for j in ico_third_step_combinations:
    for i in all_icosahedrals:
        if ((i+j) <= int(2.13*10**6)):
            ico_fourth_step_combinations.add(i+j)

#fifth step
ico_fifth_step_combinations = set()
for j in ico_fourth_step_combinations:
    for i in all_icosahedrals:
        if ((i+j) <= int(2.13*10**6)):
            ico_fifth_step_combinations.add(i+j)          
#last step
final_list = set()
for j in all_dodecahedrals:
    for i in ico_fifth_step_combinations:
        if (10000 <= (i+j) <= int(2.13*10**6)):
            final_list.add(i+j)

check_counter(10000, int(2.13*10**6), final_list)
