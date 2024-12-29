#include <bits/stdc++.h>
using namespace std;

bool is_possible_to_allocate(int mid, vector<int> arr, int m){
    int page = 0, counter = 1; // first student has 0 pages;
    for (int i =0; i<arr.size(); i++){
        page += arr[i];
        if(page > mid){
            page = arr[i];
            counter++;
        }
    }
    return (counter <= m); 
}

int main(){
/*
    cout << "Enter the size of arr ---> ";
    int n; cin >> n;
    cout << endl;
    
    cout << "Enter the people quantity ---> ";
    int m; cin >> m;
    cout << endl;

    vector<int> arr(n);
    cout << "Enter the arr ----> ";
    for(int i=0; i<n; i++){
        cin >> arr[i];
    }
    int min = arr[0];
    int max = 0;
    for(int i = 0; i<n; i++){
        max += arr[i];
        if(min < arr[i]) min = arr[i];
    }


    int ans = -1, mid;
    while (min<=max){
        mid = min+(max-min)/2;
        if(is_possible_to_allocate(mid, arr, m) == true){
            ans = mid;
            max = mid-1;
        }
        else min = mid+1;
    }
    cout << "---->  " << ans << endl;
*/


}