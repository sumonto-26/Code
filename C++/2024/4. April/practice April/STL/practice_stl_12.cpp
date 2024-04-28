// DATE ==> 28 April 2024
// Topic ==> STACK_PROBLEM "Next Greater Element using stack."
// Video Link ==> https://www.youtube.com/watch?v=T-E3hWEPWWU&t=371s&ab_channel=Luv

#include <bits/stdc++.h>
using namespace std;

int main(){

    int n;
    cin >> n;
    vector <int> vec;
    for (int i=0; i<n; ++i){
        cin >> vec[i];
    }

    for (auto value : vec){
        cout << value << ' ';
    }

    return 0;
}