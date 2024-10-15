// DATE ==> 6 September 2024 (Friday)
// AUTHOR ==> SUMONTO
// PROBLEM NAME ==> B. Books
// CONTEST NAME ==> Codeforces Round 171 (Div. 2)
// Link ==> https://codeforces.com/problemset/problem/279/B
// PROBLEM RATING ==> 1400
// PROBLEM TAGS ==> Binary Search, Brute Force, Implementation, Two pointers.
// Time Limit Per Test ==> 2 Second.
// Memory Limit Per Test ==> 256 MegaBytes.

/*
When Valera has got some free time, he goes to the library to read some books.
Today he's got t free minutes to read. That's why Valera took n books in the library
and for each book he estimated the time he is going to need to read it.
Let's number the books by integers from 1 to n. Valera needs ai minutes to read the i-th book.
Valera decided to choose an arbitrary book with number i and read the books one by one,
starting from this book. In other words, he will first read book number i,
then book number i + 1, then book number i + 2 and so on. He continues the process until
he either runs out of the free time or finishes reading the n-th book.
Valera reads each book up to the end, that is, he doesn't start reading the book
if he doesn't have enough free time to finish reading it.

Print the maximum number of books Valera can read.
*/

#include <bits/stdc++.h>
using namespace std;

int Sum_mid_to_n(vector<int> a, int n, int t, int mid){
    int sum = 0;
    for(int i=mid; i<n; i++)
        sum += a[i];
    return sum;
}

int main(){
    int n,t;
    cin >> n >> t;
    vector<int> a(n);
    for(int i=0; i<n; i++) cin >> a[i];
    sort(a.begin(), a.end());

    int start = 0, end = n, ans = 0;
    while(start <= end){
        int mid = start + (end-start)/2;

        if(Sum_mid_to_n(a,n,t,mid ) <= t){
            ans = mid;
            end = mid-1;
        }
        else start = mid+1;
    }

    cout << n-ans << endl;

}