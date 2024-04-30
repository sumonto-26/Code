# DATE ==> 30 April 2024
# AUTHOR ==> SUMONTO

n = int(input())
a = list(map(int,input().split()))

one = a.count(1)
two = a.count(2)

def count_contin():
    l = []
    ans = 1
    for i in range(len(a)-1):
        if a[i] == a[i+1]:
            ans+= 1
        elif a[i] != a[i+1]:
            l.append(ans)
            ans = 1
    l.append(ans)
    return l



ans_list = count_contin()
answer = 0
for i in range(len(ans_list)-1):
    if answer < min(ans_list[i], ans_list[i+1]):
        answer = min(ans_list[i], ans_list[i+1])
print(answer*2)