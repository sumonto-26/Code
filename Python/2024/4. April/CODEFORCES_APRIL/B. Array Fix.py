for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(len(a)):
        if a == sorted(a):
            print("YES")
            break
        if a[i] > 10:
            sorted_digits = sorted(str(a[i]))
            if str(a[i]) == ''.join(sorted_digits):
                a = a[:i] + [int(digit) for digit in sorted_digits] + a[i+1:]
                if a == sorted(a):
                    print("YES")
                    break
    else:
        print("NO")
        
# Not Compelite # Not Compelite # Not Compelite # Not Compelite
# Not Compelite # Not Compelite # Not Compelite # Not Compelite
# Not Compelite # Not Compelite # Not Compelite # Not Compelite
# Not Compelite # Not Compelite # Not Compelite # Not Compelite
# Not Compelite # Not Compelite # Not Compelite # Not Compelite
# Not Compelite # Not Compelite # Not Compelite # Not Compelite
# Not Compelite # Not Compelite # Not Compelite # Not Compelite