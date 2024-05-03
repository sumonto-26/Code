strs = list(map(str,input().split()))
min_len = float('inf')
ans_str = ""
for i in strs:
    if min_len > len(i):
        min_len = len(i)
        
for l in range(len(strs)):
    for k in range(min_len):
        if strs[0][k] == strs[l][k]:
            ans_str += strs[0][k]
        else:
            break
    ans_str += " "
    
ans_str = ans_str.split(" ")
ans_str = ans_str[:-1]
ans = "*"*201
for i in ans_str:
    if len(i) < len(ans):
        ans = i
        
print(ans)