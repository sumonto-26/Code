// DATE ==> 22 April 2024
// AUTHOR ==> SUMONTO.

#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, t;
    cin >> n >> t;
    string s;
    cin >> s;

    for (int i = 0; i < t; ++i) {
        regex pattern("BG");
        s = regex_replace(s, pattern, "GB");
    }

    cout << s << endl;

    return 0;
}
