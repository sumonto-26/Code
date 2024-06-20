// Date ==> 29 April 2024
// Topic ==> Upper Bound and Lower Bound in C++ STL
// Youtube Video Link ==> https://www.youtube.com/watch?v=Cg7SI0WtmXY&t=508s&ab_channel=Luv

#include <bits/stdc++.h>
using namespace std;

int main(){

    // FOR ARRAYS
    /*
    int n;
    cin >> n;
    int arr[n];
    for (int i=0; i<n; ++i){
        cin >> arr[i];
    }
    sort(arr, arr+n); // to make the code faster.
    for(int i=0; i<n; ++i){
        cout << arr[i] << " ";
    }
    cout << endl;

    int *pointer_ = lower_bound(arr, arr+n, 5);
    int *pointer_2 = upper_bound(arr, arr+n, 5);
    if (pointer_ == (arr+n)){
        cout << "Not found";
    }
    cout << (*pointer_) << " " << (*pointer_2) << endl; 
    */
    
    // FOR VECTORS
    /*
    int n;
    cin >> n;
    vector <int> vec(n);
    for (int i=0; i<n; ++i){
        cin >> vec[i];
    }
    sort(vec.begin(), vec.end()); // to make the code faster.
    for(int i=0; i<n; ++i){
        cout << vec[i] << " ";
    }
    cout << endl;

    auto it = lower_bound(vec.begin(), vec.end(), 5);
    auto it2 = upper_bound(vec.begin(), vec.end(), 5);
    if (it == (vec.end())){
        cout << "Not found";
    }
    cout << (*it) << " " << (*it2) << endl; 
    */

    // FOR SETS
    /*
    int n;
    cin >> n;
    set <int> s;
    for (int i=0; i<n; ++i){
        int x;
        cin >> x;
        s.insert(x);
    }
    // auto it = lower_bound(s.begin(), s.end(), 5); // O(N)
    auto it = s.lower_bound(5); // O(LOG(N))
    cout << (*it) << endl;
    */

    // FOR MAPS
    int n;
    cin >> n;
    map<int, int> m;
    for (int i = 0; i < n; ++i) {
        int key, value;
        cin >> key >> value;
        m[key] = value;
    }
    cout << endl;

    // Output the map
    for (auto it = m.begin(); it != m.end(); ++it) {
        cout << it->first << " " << it->second << endl;
    }

    // Search for lower and upper bounds
    auto it_lower = m.lower_bound(5); // Returns an iterator to the first element not less than key (>=)
    auto it_upper = m.upper_bound(5); // Returns an iterator to the first element greater than key

    // Check if found
    if (it_lower == m.end()) {
        cout << "Lower bound not found" << endl;
    } else {
        cout << "Lower bound: " << it_lower->first << " " << it_lower->second << endl;
    }

    if (it_upper == m.end()) {
        cout << "Upper bound not found" << endl;
    } else {
        cout << "Upper bound: " << it_upper->first << " " << it_upper->second << endl;
    }



    return 0;
}