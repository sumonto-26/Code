# DATE ==> 27 JULY 2024
# TIME ==> 7:34 PM
# AUTHOR ==> SUMONTO

s = input()
s = list(s)
i,j = 0,len(s)-1

if s == s[::-1] : print(True)
else:
    while(i<j):
        if s[i] != s[j]:
            s1,s2 = s[:i],s[i+1:]
            s3,s4 = s[:j],s[j+1:]
            print(s1+s2 == (s1+s2)[::-1] or s3+s4 == (s3+s4)[::-1])
            break
        i += 1
        j -= 1
    else:
        print(True)
