# A Marathon
'''for _ in range(int(input())):
    a = list(map(int,input().split(' ')))
    t = a[0]
    ans = 0
    for i in a:
        if i > t :
            ans += 1
    print(ans)'''
    
    
# B. All Distinct


# C. Where's the Bishop?
"""
import sys

input_lines = sys.stdin.read().strip().split('\n')
input_lines.pop()  # Removing the last empty line

idx = 0
while idx < len(input_lines):
    t = int(input_lines[idx])
    idx += 1

    for _ in range(t):
        arr = []
        rows, cols = 8, 8
        for _ in range(rows):
            arr.append(list(input_lines[idx]))
            idx += 1

        for i in range(1, rows - 1):
            for j in range(1, cols - 1):
                if arr[i][j] == '#' and arr[i-1][j-1] == '#' and arr[i-1][j+1] == '#' and arr[i+1][j-1] == '#' and arr[i+1][j+1] == '#':
                    print(i+1, j+1)
"""
