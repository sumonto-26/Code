// DATE ==> 29 December 2024
// Problem name ==> A. Juicer
// AUTHOR ==> SUMONTO
// time limit per test ==> 1 second
// memory limit per test ==> 256 megabytes

#include <bits/stdc++.h>
using namespace std;
int main(){
    int n,b,d;
    cin >> n >> b >> d ;
    int ans = 0,box = 0;
    for(int i = 0; i<n; i++){
        int orange; cin >> orange;
        box += orange;
        if(box > d) {
            box = 0;
            ans ++;
        }
    }
    cout << ans << endl;
    return 0;
}

// NOT SOLVED ERROR BUG
// NOT SOLVED ERROR BUG
// NOT SOLVED ERROR BUG
// NOT SOLVED ERROR BUG
// NOT SOLVED ERROR BUG