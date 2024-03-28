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
