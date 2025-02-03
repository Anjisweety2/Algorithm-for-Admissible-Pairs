from itertools import combinations_with_replacement

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
    n : index of the largest icosahedral number we are using to compute the sums
    limit: the maximum number of icosahedral numbers in the sum

Return value: a list of positive integers less or equal to "m" that can be written
              as a sum of at most "limit" icosahedral numbers
"""
def sum_of_icosahedrals(m, n, limit):
    return_list = []
    for j in combinations_with_replacement(map(make_icosahedral, list(range(n + 1))), limit):
        if (sum(j) not in return_list and sum(j) <= m):
            return_list.extend([sum(j)])
    return return_list

"""
Input values
    m : maximum value of the positive integers that we are checking
    n : index of the largest dodecahedral number we are using to compute the sums
    limit: the maximum number of dodecahedral numbers in the sum

Return value: a list of positive integers less or equal to m that can be written
              as a sum of "limit" dodecahedral numbers
"""
def sum_of_dodecahedrals(m, n, limit):
    return_list = []
    for j in combinations_with_replacement(map(make_dodecahedral, list(range(n + 1))), limit):
        if (sum(j) not in return_list and sum(j) <= m):
            return_list.extend([sum(j)])
    return return_list

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


# sample: (5,6)
icos = sum_of_icosahedrals(80309, 32, 5) # a list of positive integers less than or equal to 80309 that can be written as a sum of at most 5 icosahedral numbers
dodes = sum_of_dodecahedrals(80309, 26, 1) #a list of positive integers less than or equal to 80309 that can be written as a sum of at most 5 dodecahedral numbers
check_counterexample(icos, dodes, 10000, 80309) 
# expected value: "no counterexamples".
