// DATE ==> 2 May 2024
// Author ==> Sumonto.
// Problem name ==> A. Maximuze ?

#include <bits/stdc++.h>
using namespace std;

int main(){
    int N;
    cin >> N;
    while (N--){
        int n,m;
        cin >>n>>m;
        string a,b;
        cin >> a >> b;
        int ans = 0;
        int j = 0;
        for (int i=0; i<m && j<n; ++i){
            if (a[j] == b[i]){
                ans++;
                j++;
            }
        }
        cout << ans << endl;;

    }

    return 0;
}