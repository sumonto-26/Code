#include <bits/stdc++.h>
using namespace std;
int main(){
    
    int N;
    cin >> N;
    string a,b;
    cin >> a >> b;
    int ans = 0;

    for(int i = 0; i<N; ++i){
        int d = 0;
        int diff = abs(a[i] - b[i]); 

        if (diff > 5) {
            d = 10 - diff; 
        } else {
            d = diff; 
        }
        ans += d;
        
        // cout << d << endl;
        }
    cout << ans <<endl; 

    return 0;
}