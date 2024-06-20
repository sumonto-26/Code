// DATE ==> 1 May 2024
// Problem Name ==> F. 3SUM Codeforces Round 799 (Div. 4)
// Problem Rating ==> 1300
// AUTHOR ==> SUMONTO
#include <bits/stdc++.h>
using namespace std;

int main() {
    int TEST;
    cin >> TEST;
    while(TEST--) {
        int N;
        cin >> N;
        vector<int> vec;
        for(int i = 0; i < N; ++i) {
            int x;
            cin >> x;
            vec.push_back(x%10);
        }

        bool found = false;
        for(int i = 0; i < N; ++i) {
            for(int j = i + 1; j < N; ++j) {
                for(int k = j + 1; k < N; ++k) {
                    int sum = vec[i] + vec[j] + vec[k];
                    if (sum % 10 == 3) {
                        found = true;
                        break; 
                    }
                }
                if (found) break; 
            }
            if (found) break; 
        }

        if (found) {
            cout << "YES" << endl;
        } else {
            cout << "NO" << endl;
        }
    }
    return 0;

    // TIME ERROR TIME ERROR TIME ERROR TIME ERROR TIME ERROR TIME ERROR //
    // TIME ERROR TIME ERROR TIME ERROR TIME ERROR TIME ERROR TIME ERROR //
    // TIME ERROR TIME ERROR TIME ERROR TIME ERROR TIME ERROR TIME ERROR //
    // TIME ERROR TIME ERROR TIME ERROR TIME ERROR TIME ERROR TIME ERROR //
    // TIME ERROR TIME ERROR TIME ERROR TIME ERROR TIME ERROR TIME ERROR //
    // TIME ERROR TIME ERROR TIME ERROR TIME ERROR TIME ERROR TIME ERROR //
    // TIME ERROR TIME ERROR TIME ERROR TIME ERROR TIME ERROR TIME ERROR //
    // TIME ERROR TIME ERROR TIME ERROR TIME ERROR TIME ERROR TIME ERROR //


}