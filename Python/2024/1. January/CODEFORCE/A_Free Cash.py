n = []
l = int(input())
for _ in range(l):
    a = input()
    n.append(a)

count_dict = {}
for element in n:
    count_dict[element] = count_dict.get(element, 0) + 1

max_count = max(count_dict.values())
print(max_count)
