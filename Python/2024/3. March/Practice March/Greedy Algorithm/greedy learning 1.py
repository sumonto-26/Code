def make_change(coins, amount):
    coins.sort(reverse=True)  # Sort coins in descending order
    
    num_coins = 0
    change = []

    for coin in coins:
        while amount >= coin:
            amount -= coin
            num_coins += 1
            change.append(coin)

    return num_coins, change

# Example usage:
coins = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000]
amount = int(input())
num_coins, change = make_change(coins, amount)
print("Minimum number of coins:", num_coins)
print("Change given:", change)
