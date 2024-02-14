# DATE 15 12 2023

# a = input()
# p = ''

# for i in a:
#     if i not in p: p = p+i

# ans = len(p)
# print("CHAT WITH HER!" if ans % 2 == 0 else "IGNORE HIM!")


a = set(input())
ans = len(a)
print("CHAT WITH HER!" if ans % 2 == 0 else "IGNORE HIM!")
