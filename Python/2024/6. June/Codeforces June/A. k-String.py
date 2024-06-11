# DATE ==> 11 JUNE 2024
# AUTHOR ==> SUMONTO

k = int(input())
s = input()
if len(s)%k == 0:
    characters = list(set(s))
    counts = []
    for i in characters:
        counts.append(s.count(i)) 
    ans = ""
    for j in range(len(characters)):
        ans += characters[j]*int(counts[j]/k)
    print(ans*k if len(s) == len(ans)*k else -1)

else:
    print(-1)