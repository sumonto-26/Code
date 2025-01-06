// DATE ==> 5 January 2025
// AUTHOR ==> SUMONTO
#include <bits/stdc++.h>
using namespace std;

int main() {
    int tt; cin >> tt;
    while (tt--){
        int n, k; cin >> n >> k;
        vector<int> a(n);
        unordered_map<int, int> freq;
        for (int i = 0; i < n; i++) {
            cin >> a[i];
            freq[a[i]]++;
        }
        vector<int> emp;
        for (auto& it : freq) {
            emp.push_back(it.second);
        }
        n = emp.size();
        sort(emp.begin(), emp.end());
        for (int i = 0; i < emp.size(); i++) {
            if (k - emp[i] >= 0){
                k -= emp[i];
                n--;
            } 
            else break;   
        }
        cout << max(n, 1) << endl;
    }

    return 0;

    //time error
    //time error
}
