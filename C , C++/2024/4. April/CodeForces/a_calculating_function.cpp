// Date ==> 21 April 2024
// Author ==> SUMONTO.

#include <bits/stdc++.h>
using namespace std;

int main (){
    long long a ;
    cin >> a;

    if (a%2 == 0){
        cout << a/2;
    }
    else{
        cout << ((a+1)/2)*-1;
    }
    


    return 0;
}