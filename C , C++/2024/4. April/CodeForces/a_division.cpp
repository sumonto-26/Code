// Date ==> 21 April 2024
// Author ==> SUMONTO

#include <bits/stdc++.h>
using namespace std;

int main (){
    int N;
    cin >> N;
    for (int i=0; i<N; i++){
        int s;
        cin >> s;
        
        if (s< 1400){
            cout << "Division 4" << endl; 
        }
        else if (s>= 1400 && s<1600){
            cout << "Division 3" << endl; 
        }
        else if (s>= 1600 && s<1900){
            cout << "Division 2" << endl; 
        }
        else
            cout << "Division 1" << endl; 
        }

    return 0;
}