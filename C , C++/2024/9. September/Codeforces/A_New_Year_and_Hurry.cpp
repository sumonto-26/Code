// DATE ==> 4 September 2024
// AUTHOR ==> SUMONTO
// PROBLEM NAME ==> A. New Year and Hurry
// CONTEST NAME ==>  Good Bye 2016
// Link ==> https://codeforces.com/problemset/problem/750/A
// PROBLEM RATING ==> 800
// PROBLEM TAGS ==> Binary Search, Math, Brute Force, Implementation .
// Time Limit Per Test ==> 1 Second.
// Memory Limit Per Test ==> 256 MegaBytes.
/*
Limak is going to participate in a contest on the last day of the 2016. The contest will start at 20:00 and will last four hours,
exactly until midnight. There will be n problems, sorted by difficulty,
i.e. problem 1 is the easiest and problem n is the hardest. Limak knows it will take him 5·i minutes to solve the i-th problem.
Limak's friends organize a New Year's Eve party and Limak wants to be there at midnight or earlier.
He needs k minutes to get there from his house, where he will participate in the contest first.
How many problems can Limak solve if he wants to make it to the party?
*/
#include <bits/stdc++.h>
using namespace std;
int main(){
    int problems, party_time;
    cin >> problems >> party_time;
    if(party_time > 235) cout << 0 << endl;
    
    // binary Search in 1-10 for improved implementation of binary search;
    else{
        int start = 1, end = problems, mid, ans;
        int contest_time = 240-party_time; 
        while(start <= end){
            mid = start + (end-start)/2;
            int solving_time = 0;
            for(int i=1; i<=mid; i++) solving_time+= i*5;
            if(solving_time == contest_time){
                ans =  mid;
                break;
                }
            else if( solving_time < contest_time){
                ans = mid;
                start = mid+1;
            }
            else end = mid-1;
        }
        cout << ans << endl;
    }

    return 0;
}