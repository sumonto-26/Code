# DATE ==> 3 September 2024
# AUTHOR ==> SUMONTO
# PROBLEM NAME ==> A. Case of the Zeros and Ones
# CONTEST NAME ==> Codeforces Round 310 (Div. 2)
# PROBLEM RATING ==> 900
# PROBLEM TAGS ==> Greedy
# Time Limit Per Test ==> 1 Second.
# Memory Limit Per Test ==> 256 MegaBytes.

'''
Andrewid the Android is a galaxy-famous detective. In his free time he likes to think about strings containing zeros and ones.
Once he thought about a string of length n consisting of zeroes and ones. Consider the following operation:
we choose any two adjacent positions in the string, and if one them contains 0, and the other contains 1,
then we are allowed to remove these two digits from the string, obtaining a string of length n - 2 as a result.
Now Andreid thinks about what is the minimum length of the string that can remain after applying the described operation several times
(possibly, zero)? Help him to calculate this number.
Output the minimum length of the string that may remain after applying the described operations several times.
'''

n = int(input())
b = input()
while(len(set(b)) == 2):
    b = b.replace("10","")
    b = b.replace("01", "")
print(len(b))

#time error
#time error
#time error
#time error
#time error
#time error
#time error