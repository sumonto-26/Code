// DATE ==> 1 May 2024
// Problem rating ==> 1300
// Problem Name ==> A. Equator
// AUTHOR ==> SUMONTO. 

#include <bits/stdc++.h>
using namespace std;

int main(){
    int n;
    cin >> n;
    vector <int> v(n);
    for(int i=0; i<n; ++i){
        cin >> v[i];
    }
    double half_sum = accumulate(v.begin(), v.end(), 0.0) / 2;
    // cout << half_sum << endl;

    int ans = 0;
    for (int i=0; i<n; ++i){
        ans += v[i];
        if (ans >= half_sum){
            cout<< i+1<< endl;
            break;
        }
    }

    return 0;
}