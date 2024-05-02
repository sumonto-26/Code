// DATE ==> 2 May 2024
// Problem Name ==> B. I Hate 1111.
// Problme Rating ==> 1400.
// AUTHOR ==> SUMONTO.

#include <bits/stdc++.h>
using namespace std;

bool solve(int amount) {
    for (int i = 0; i <= amount / 111; ++i) {
        // for (int j = 0; j <= amount / 111; ++j) {
        if ((amount-(111 * i)) % 11 == 0) {
            return true;
            // }
        }
    }
    return false;
}

int main() {
    int N;
    cin >> N;
    for (int i = 0; i < N; ++i) {
        int x;
        cin >> x;
        if (solve(x)) cout << "YES" << endl;
        else cout << "NO" << endl;
    }
    return 0;
}
