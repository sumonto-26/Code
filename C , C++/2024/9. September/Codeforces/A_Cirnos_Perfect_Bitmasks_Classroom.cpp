// DATE ==> 6 September 2024 (Friday)
// AUTHOR ==> SUMONTO
// PROBLEM NAME ==> A. Cirno's Perfect Bitmasks Classroom
// CONTEST NAME ==> Codeforces Round 796 (Div. 2)
// Link ==> https://codeforces.com/problemset/problem/1688/A
// PROBLEM RATING ==> 800
// PROBLEM TAGS ==> Bitmasks, Brute Force.
// Time Limit Per Test ==> 1 Second.
// Memory Limit Per Test ==> 256 MegaBytes.

/*
Cirno's perfect bitmasks classroom has just started!
Cirno gave her students a positive integer x. As an assignment,
her students need to find the minimum positive integer y,
which satisfies the following two conditions:
x and y>0 x xor y>0
Where and is the bitwise AND operation, and xor is the bitwise XOR operation.
Among the students was Mystia, who was truly baffled by all these new operators. Please help her!
*/

#include <bits/stdc++.h>
using namespace std;
int main(){
    int tt; cin >> tt;
    while(tt--){
        long long x, y=0; cin >> x;
        long long v1 = x&y, v2 = x^y;
        while(v1<=0 || v2<=0){
            y++;
            v1 = x&y;
            v2 = x^y;
        } 
        cout << y << endl;
    }

    return 0;
}