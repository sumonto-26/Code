# DATE ==> 28 February 2024
# RATING ==> 1100
# TIME COMPLEXITY ==> 733ms
# MY LOGIC.
for _ in range(int(input())):
    n = list(map(int,input().split()))
    if n[1]**2 <= n[0] and n[0] % 2 == n[1] % 2:
        print("YES")
    else:
        print("NO")     
        
# OTHER'S LOGIC
# TIME COMPLEXITY ==> 202ms
""" 
import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
print = lambda x: sys.stdout.write(str(x) + "\n")
    
II = lambda: int(input())
MII = lambda: map(int, input().split())
LMII = lambda: list(MII())
SLMII = lambda: sorted(LMII())

for _ in range(II()):
    n, k = MII()
    print('YES' if n >= k*k and n%2 == k%2 else 'NO')"""   