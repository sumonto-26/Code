// Date ==> 3 September 2024
// Problem Name ==> A. Benches
// Time Limit Per Test ==> 1 second
// Memory Limit Per Test ==> 256 megabytes
// Author ==> SUMONTO

#include<bits/stdc++.h>
using namespace std;
// My Solution 
int main() {
    int n; cin >> n;
    int m; cin >> m;

    vector<int> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];
    int maximum = *max_element(a.begin(), a.end()) + m;

    while (m) {
        int min_index = 0;
        for(int i=0; i<n; i++)
            if(a[i] < a[min_index]) min_index = i;
        a[min_index]++; 
        m--;
    }

    cout << *max_element(a.begin(), a.end()) << " " << maximum << endl;

    return 0;
}

/*    OTHERS SOLUTIONS
const int N = 100 + 13;

int n, m;
int a[N];

int main() {
    cin >> n >> m;
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    int ans2 = *max_element(a, a + n) + m;
    for (int it = 0; it < m; it++) {
        int pos = -1;
        for (int i = 0; i < n; i++) {
            if (pos == -1 || a[i] < a[pos]) {
                pos = i;
            }
        }
        assert(pos != -1);
        a[pos]++;
    }
    int ans1 = *max_element(a, a + n);
    cout << ans1 << ' ' << ans2 << endl;
}
*/