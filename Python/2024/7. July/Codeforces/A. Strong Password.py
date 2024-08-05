# DATE ==> 30 7 2024
# AUTHOR ==> SUMONTO

# A. Strong Password
def count_time(s):
    st = s
    for i in range(1,len(st)):
        if st[i-1]==st[i]:
            return False
    return True

    
for i in range(int(input())):
    char = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    n = input("")
    # print(count_time(n))
    if count_time(n):
        for i in char:
            if i != n[-1]:
                print(n+i)
                break
    else:
        pass
        for i in range(1,len(n)):
            if n[i] == n[i-1]:
                n = n[:i]+char[char.index(n[i])+1]+ n[i:]
                print(n)
                break
