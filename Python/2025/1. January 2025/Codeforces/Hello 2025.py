# DATE ==> 4 JANUARY 2025
# CONTEST ==> Hello 2025
# Problem A
for _ in range(int(input())):
    arr = list(map(int,input().split()))
    print(max(arr)+1)

# Problem B
for _ in range(int(input())):
    n,k = map(int,input().split())
    arr = list(map(int,input().split()))
    if(n == k): print(1)
    else:
        tem = []
        for i in set(arr):
            tem.append(arr.count(i))
        tem = sorted(tem)
        
        for i in range(len(tem)):
            k -= tem[i]
            if(k < 0): 
                print(len(tem)-i)
                break

