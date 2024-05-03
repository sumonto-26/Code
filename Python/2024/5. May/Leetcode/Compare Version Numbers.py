# DATE ==> 3  May 2024

version1 = input("Enter version 1: ")
version2 = input("Enter version 2: ")


version1 = version1.split('.')
version2 = version2.split('.')
for i in range(max(len(version1), len(version2))):
    if i >= len(version1): v1 = 0
    else: v1 = int(version1[i])
    
    if i >= len(version2): v2 = 0
    else: v2 = int(version2[i])
    
    if v1 > v2:
        # return 1
        print(1)
        break
        
    if v1 < v2:
        # return -1
        print(-1)
        break
        
else:
    print(0)