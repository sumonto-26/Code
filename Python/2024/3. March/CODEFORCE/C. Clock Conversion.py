#my logic
for _ in range(int(input())):
    a = input()
    hour, minute = map(int, a.split(':'))
    if hour == 0:
        print(f"12:{minute:02d} AM")
    elif hour < 12:
        print(f"{hour:02d}:{minute:02d} AM")
    elif hour == 12:
        print(f"{hour:02d}:{minute:02d} PM")
    else:
        print(f"{hour-12:02d}:{minute:02d} PM")

#tourist's logic
'''import sys

for _ in range(int(input())):
    h, m = map(int, input().split(':'))
    s = " AM"
    if h >= 12:
        h -= 12
        s = " PM"
    if h == 0:
        h = 12
    print(f"{h:02d}:{m:02d}{s}")'''
