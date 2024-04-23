# DATE ==> 23 April 2024
# AUTHOR ==> SUMONTO

N = int(input())
presents = list(map(int,input().split()))
sort = sorted(presents)
ans = []
for i in range(N):
    a = presents.index(sort[i]) + 1
    ans.append(str(a))

ans = " ".join(ans)
print(ans)