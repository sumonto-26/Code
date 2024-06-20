// Date ==> 20 April 2024
// Author ==> SUMONTO

#include <bits/stdc++.h>
using namespace std;

int main(){

    int ans = 0;
    int N;
    cin >> N;

    for (int i=0; i<N; i++){
        string s;
        cin >> s;
        if (s[1] == '+'){
            ans++;
        }
        else{
            ans--;
        }
    }
    cout << ans<< endl;

    return 0;
}