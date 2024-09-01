// DATE ==> 1 September 2024
// AUTHOR ==> SUMONTO
#include <bits/stdc++.h>
using namespace std;

int main(){
    int n; cin >> n;
    int ans = 0, one = 0, two = 0, three = 0;
    vector<int> vec(n);
    for(int i = 0; i < n; i++){
        int element; cin >> element;
        if(element == 4) ans ++;
        else if (element == 1) one++;
        else if(element == 2) two++;
        else three++;
    }

    if(one > three){ 
        ans += three;
        one -= three;
        if(two % 2 == 0 ){
            ans += two/2;
            if(one % 4 == 0) ans += one/4;
            else ans += (one/4)+1; 
        }
        else{
            ans += (two-1)/2;
            one += 2;
            if(one % 4 == 0) ans += one/4;
            else ans += (one/4)+1; 
        }
    }

    else{
        ans += three;
        if(two % 2 == 0) ans += two/2;
        else ans += ((two-1)/2)+1;
    }
    
    cout << ans << endl;
    return 0;
}