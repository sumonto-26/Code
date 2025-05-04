// DATE -----> 4 May 2025
// AUTHOR -----> SUMONTO
// Problem -----> http://codeforces.com/problemset/problem/381/A
#include <bits/stdc++.h>
using namespace std;
int main(){
    int n; cin >> n;
    vector<int> arr(n);
    int sereja = 0;
    int dima = 0;
    for (int i=0; i<n; i++) cin >> arr[i];
    int start=0, end = n-1;
    string s = "sereja";
    while(start<=end){
        if(arr[start] > arr[end]){
            if(s == "sereja"){
                sereja += arr[start];
                s = "dima";
            }
            else{
                dima += arr[start];
                s = "sereja";
            }
            start++;
        }
        else{
            if(s == "sereja"){
                sereja += arr[end];
                s = "dima";
            }
            else{
                dima += arr[end];
                s = "sereja"; 
            }
            end--;
        }
    }
    cout << sereja << " " << dima << endl;

    return 0;
} 