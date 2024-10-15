// DATE ==> 6 September 2024 (Friday)
// AUTHOR ==> SUMONTO
// PROBLEM NAME ==>  B. DMCA
// CONTEST NAME ==>  April Fools Day Contest 2021
// Link ==>  https://codeforces.com/problemset/problem/1505/B
// PROBLEM RATING ==> 1600 
// PROBLEM TAGS ==>  *Special Problem, Implementation, Number Theory.
// Time Limit Per Test ==> 1 Second.
// Memory Limit Per Test ==> 256 MegaBytes.

/*
Many people are aware of DMCA – Digital Millennium Copyright Act.
But another recently proposed DMCA – Digital Millennium Calculation Act – is much less known.
In this problem you need to find a root of a number according to this new DMCA law.
*/
#include <bits/stdc++.h>
using namespace std;
int main(){
    int a; cin >> a;
    while(a>=10){
        int sum = 0;
        while(a){
            sum += a%10;
            a /= 10;
        }
        a = sum;
    }
    cout << a << endl;

    return 0;
}