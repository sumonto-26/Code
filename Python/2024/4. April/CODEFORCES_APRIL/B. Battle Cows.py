def max_wins(n, k, ratings):
    max_wins = 0
    cow = ratings[k]
    
    for i in range(n//2):
        if n % 2 == 0:
            for j in range(0, n, 2):
                removed_index = ratings.index(min(ratings[j], ratings[j+1]))
                ratings.pop(removed_index)
        else:
            for j in range(0, n-1, 2):
                removed_index = ratings.index(min(ratings[j], ratings[j+1]))
                ratings.pop(removed_index)
        
        if ratings[k] in  :
            max_wins += 1
    
    return max_wins


for _ in range(int(input())):
    n, k = map(int, input().split())
    ratings = list(map(int, input().split()))
    
    print(max_wins(n, k, ratings))
