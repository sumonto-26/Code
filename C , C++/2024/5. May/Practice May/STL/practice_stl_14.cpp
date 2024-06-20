// DATE ==> 29 April 2024.
// Topic ==> Comparator Function in depth Tutorial using C++ Sort.
// Youtube Video Link ==> https://www.youtube.com/watch?v=3pvZhwp0U9w&ab_channel=Luv

#include <bits/stdc++.h>
using namespace std;

bool should_i_swap(pair<int,int> a, pair<int,int> b ){
    if (a.first != b.first){
        // if (a.first > b.first) return false;
        // return true;
        return a.first < b.first;
    }
    // else{
    //     if (a.second < b.second) return false;
    //     return true;
    return a.second > b.second;
    }
// }

int main(){
    int n;
    cin >> n;
    vector<pair<int,int>> a(n);
    for(int i=0; i<n; ++i){
        cin >> a[i].first >> a[i].second;
    }
    for(int i=0; i<n; ++i){
        for (int j=i+1; j<n; ++j){
            if (should_i_swap(a[i], a[j])){
                swap(a[i], a[j]);
            }
        }
    }
    // sort(a.begin(), a.end());
    sort(a.begin(), a.end(), should_i_swap);

    for (int i = 0; i < n; ++i ){
        cout << a[i].first << " " << a[i].second << endl;
    }
    

    return 0;
}