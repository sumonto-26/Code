// DATE ==> 22 April 2024
// AUTHOR ==> SUMONTO.

#include <bits/stdc++.h>
using namespace std;
int main(){
    string a,b;
    cin >> a >> b;
    vector <string> v;
    for (int i=0; i<a.size(); i++){
        if (a[i] == b[i]){
            v.push_back("0");
        }
        else{
            v.push_back("1");
        }
    }
    for(auto it = v.begin() ; it != v.end(); it++){
        cout << (*it);
    }


    return 0;
}