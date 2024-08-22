// DATE ==> 22 AUGUST 2024
// PROBLEM NAME ==> A. The number of positions.
// PROBLEM RATING ==> 1000.
// PROBLEM TAGS ==> Math 
// AUTHOR ==> SUMONTO

#include <bits/stdc++.h>
using namespace std;

int main(){
    int n, a, b;
    cin >> n >> a >> b;

    n -= a;
    cout << min(n, b+1) << endl;

    return 0;
}