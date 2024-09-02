// DATE ==> 3 September 2024
// AUTHOR ==> SUMONTO
// PROBLEM NAME ==> B. Minimum Product
// PROBLEM RATING ==> 1100
// PROBLEM CONTEST ==> Codeforces Round 667 (Div. 3)

#include <bits/stdc++.h>
using namespace std;
int main(){
    int tt; cin >> tt;
    while(tt--){
        long long a,b,x,y,n;
        cin >> a >> b >> x >> y >> n;
        int copy_n = n;
        long long a1 = a-min(a-x, n);
        if(n <= a-x) n = 0;
        else n -= a-x;
        long long b1 = b-min(b-y,n);

        n = copy_n;
        long long b2 = b-min(b-y, n); 
        if(n <= b-y) n = 0;
        else n-= b-y;
        long long a2 = a-min(a-x,n);


        cout << min(a1*b1, a2*b2) << endl;
    }
    return 0;
}