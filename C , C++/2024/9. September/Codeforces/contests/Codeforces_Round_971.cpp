// DATE ==> 3 September 2024
// AUTHOR ==> SUMONTO

// PROBLEM NAME ==> 
// 
// 
#include <bits/stdc++.h>
using namespace std;

int main(){
    int tt; cin >> tt;
    while(tt--){
        int a,b;
        cin >> a >> b;
        int c = b;
        for (int i=a; i<=b; i++){
            if((c-a)+(b-c) > (i-a)+(b-i)){
                c = i;
            }
        }
        cout << (c-a)+(b-c) << endl;
    }


    return 0;
}