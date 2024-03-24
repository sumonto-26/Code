#include <iostream>

using namespace std;

int greedyCoinChange(int amount, const int* coins, int numCoins) {
    int coinCount = 0;
    for (int i = 0; i < numCoins; ++i) {
        while (amount >= coins[i]) {
            cout << coins[i] << " ";
            amount -= coins[i];
            coinCount++;
        }
    }
    return coinCount;
}

int main() {
    int amount;
    cout << "Enter the amount: ";
    cin >> amount;

    int coins[] = {100, 50, 20, 10, 5, 2, 1}; // denominations of coins
    int numCoins = sizeof(coins) / sizeof(coins[0]);

    cout << "\nCoins used: ";
    int coinCount = greedyCoinChange(amount, coins, numCoins);

    cout << "\nMinimum number of coins required: " << coinCount << endl;

    return 0;
}

// Not compeleit Not compeleit
// Not compeleit Not compeleit
// Not compeleit Not compeleit
// Not compeleit Not compeleit
// Not compeleit Not compeleit
// Not compeleit Not compeleit