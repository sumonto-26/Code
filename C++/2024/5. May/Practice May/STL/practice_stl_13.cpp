// DATE ==> 29 April 2024.
// Topic ==> Build in Sort in C++ STL.
// Youtube Video Link ==> https://www.youtube.com/watch?v=zI9wlhwMZpk&t=336s&ab_channel=Luv

#include <bits/stdc++.h>
using namespace std;

int main(){
    int n;
    cin >> n;
    vector<int> a(n);
    for(int i=0; i<n; ++i){
        cin >> a[i];
    }
    // sort(a, a+n);
    sort(a.begin(), a.end());
    for(int j=0; j<n; ++j){
        cout << a[j] << " ";
    }

    return 0;
}