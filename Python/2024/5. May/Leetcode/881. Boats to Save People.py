people = list(map(int,input().split()))
limit = int(input())
boats = 0
people = sorted(people)
i = 0
j = len(people)-1
while(i <= j):
    if people[i] + people[j] <= limit:
        i += 1
        j -= 1
        boats += 1
    else:
        j -= 1
        boats += 1
        
print(boats)