# Algorithm-for-Admissible-Pairs

In the main branch, there is a Algorithm I.py file and a folder named "Algorithm II".

The Algorithm I.py file is used to check that Conjecture 1.1 is true for the first 12000 positive integers.

The Algorithm II folder contains four .py files, which are used to finish the proof of Theorem 1.3. The name of each file in this folder corresponds to the relevant pairs being checked. Note that there are in total 12 pairs in Conjecture 1.1, but Algorithm II only contains algorithms for 10 of them. This is because (15,0) and (0,22) are already checked in one of the references.

##### Remark: 
We use two distinct approaches here because of Algorithm I runs much slower than Algorithm II for integers >> 10^5. We are incapable of running Algorithm I with such large integers. 
