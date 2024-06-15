# DATE ==> 15 JUNE 2024
# AUTHOR ==> SUMONTO

def find_divisors(n):
    divisors = []
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if n//i != i:
                divisors.append(n//i)
    return sorted(divisors)

for _ in range(int(input())):
    n = int(input())
    divisors = find_divisors(n)
    found = False
    for i in range(len(divisors)-1):
        for j in range(i,len(divisors)):
            k = n/(divisors[i]*divisors[j])
            if k in divisors and k > 1 and k != divisors[i] and k != divisors[j] and i != j:
                print("YES")
                print(divisors[i], divisors[j], int(k))
                found = True
                break
        if found: break
    if found == False:
        print("NO")
            