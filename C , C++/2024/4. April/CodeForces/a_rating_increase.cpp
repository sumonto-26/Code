// DATE ==> 22 April 2024
// AUTHOR ==> SUMONTO

#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;
    while (N--) {
        string s;
        cin >> s;
        bool found = false;
        for (int i = 1; i < s.size(); i++) {
            int a = stoi(s.substr(0, i));
            int b = stoi(s.substr(i));
            if (a < b && s[i] != '0') {
                cout << a << " " << b << endl;
                found = true;
                break; // exit inner loop after first valid split
            }
        }
        if (!found) {
            cout << "-1" << endl; // If no valid split found
        }
    }
    return 0;
}
