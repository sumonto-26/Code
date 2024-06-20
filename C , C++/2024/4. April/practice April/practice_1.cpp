// DATE ==> 26 April 2024

#include <bits/stdc++.h>
using namespace std;
int main(){

    string real_string;
    cin >> real_string;

    int n = real_string.size();

    stack <char> sta;
    for(int i=0; i<n ; ++i){
        sta.push(real_string[i]);
    } 

    while (!sta.empty())
    {
        cout << sta.top();
        sta.pop();
    }
    cout << endl;
    


    return 0;
}