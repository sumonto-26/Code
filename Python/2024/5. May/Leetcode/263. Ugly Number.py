n = int(input())
def is_prime(num):
    if num < 2:
        return False
    else:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True
        
ans_list = []
arr = []
for i in range(1, int(n**0.5) + 1):
    if n % i == 0 :
        ans_list.append(i)
        if n // i != i :
            ans_list.append(n // i)
        
for i in ans_list:
    if is_prime(i):
        arr.append(i)    
            
pattern = [[2,3,5],[2],[3],[5],[2,3],[2,5],[3,5]]
for i in pattern:
    if i == sorted(arr):
        print(True)
        break
else:
    print(False)