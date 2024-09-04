// DATE ==> 4 September 2024
// AUTHOR ==> SUMONTO
// PROBLEM NAME ==> B. Xenia and Ringroad
// CONTEST NAME ==>  Codeforces Round 197 (Div. 2)
// Link ==> https://codeforces.com/problemset/problem/339/B
// PROBLEM RATING ==> 1000
// PROBLEM TAGS ==> Implementation
// Time Limit Per Test ==> 2 Second.
// Memory Limit Per Test ==> 256 MegaBytes.

/*
Xenia lives in a city that has n houses built along the main ringroad. 
The ringroad houses are numbered 1 through n in the clockwise order.
The ringroad traffic is one way and also is clockwise.
Xenia has recently moved into the ringroad house number 1. As a result,
she's got m things to do. In order to complete the i-th task,
she needs to be in the house number ai and complete all tasks with numbers less than i.
Initially, Xenia is in the house number 1, find the minimum time
she needs to complete all her tasks if moving from a house to a 
neighboring one along the ringroad takes one unit of time.
Print a single integer — the time Xenia needs to complete all tasks.
*/

#include <bits/stdc++.h>
using namespace std;
int main(){
    int n, m;
    cin >> n >> m;
    vector<long long > a = {0};
    long long add = 0;
    for(int i=0; i<m; i++){ 
        long long ele; cin >> ele;
        if(a[a.size()-1]-add != ele){
            if(a[a.size()-1]-add > ele)
                add += n;
            a.push_back(ele+add);
        }
    }
    a.erase(a.begin());
    cout << a[a.size()-1]-1 << endl;

    return 0;
}