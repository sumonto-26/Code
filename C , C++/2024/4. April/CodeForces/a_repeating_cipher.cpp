// DATE ==> 23 April 2024
// AUTHOR ==> SUMONTO.

#include <bits/stdc++.h>
using namespace std;

int main() {
    vector<int> v;
    int N;
    cin >> N;
    string cipher;
    cin >> cipher;

    for (int i = 1; i <= 10; ++i) {
        int index = (i * (i - 1)) / 2;
        if (index < cipher.size()) {
            v.push_back(index);
        } else {
            break;
        }
    }

    for (int j = 0; j < v.size(); ++j) {
        cout << cipher[v[j]];
    }

    return 0;
}
