// DATE ==> 29 December 2024;
// AUTHOR ==> SUMONTO
// Problem name ===> A. Payment Without Change
// Problem Rating ==> 1000
// time limit per test 1 seconds
// memory limit per test 256 megabytes

#include <bits/stdc++.h>
using namespace std;
int main(){
    int t; cin >> t;
    while(t--){
        int a, b, n, S; 
        cin >> a >> b >> n >> S;
        if(n==1){
            if(a+b >= S) cout << "YES" << endl;
            else cout << "NO" << endl;
        }
        if(S <= b || S%n == 0 && S/n <= a && S>=n|| a*n+b == S) cout << "YES" << endl;
        else if(a*n + b < S) cout << "NO" << endl;
        else if(S/n <= a && S%n <= b) cout << "YES" << endl;
        else cout << "NO" << endl;
    }

    return 0;
}
// NOT SOLVED
// NOT SOLVED
// NOT SOLVED
// NOT SOLVED
// NOT SOLVED
// NOT SOLVED
// NOT SOLVED
// NOT SOLVED
// NOT SOLVED