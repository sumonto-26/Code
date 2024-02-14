# time --> 9:46 - 9:55
# TIME COMPLEXITY --> 31ms
lis = ['abc', 'acb','cba', 'bac']
for _ in range(int(input())):
    a = input()
    print("YES" if a in lis else "NO")
    