#include <bits/stdc++.h>
using namespace std;

void print_vector(vector<int> vec){
    for (auto value : vec){
        cout << value << " ";
    } cout << endl;
}

void print_array(int arr[], int size){
    for (int i = 0; i < size; ++i){
        cout << arr[i] << " ";
    }
    cout << endl;
}


int main(){
    /*
    int n;
    cin >> n;
    vector<int> v;
    for(int i=0; i<n; ++i){
        int X;
        cin >> X;
        v.push_back(X); 
    }
    print_vector(v);
    

    // 1. Min_element . 
    // It returns address.
    // int min = *min_element(v.begin()+2, v.end());
    int min = *min_element(v.begin(), v.end());
    cout <<"The minimum element is: " << min << endl;
    
    // 2. Max_element. 
    // It returns address.
    int max = *max_element(v.begin(), v.end());
    cout <<"The maximum element is: " << max << endl;

    // 3. Accumulate.
    int sum = accumulate(v.begin(), v.end(), 0); // 0+sum
    cout << "The sum of v is: " << sum << endl;

    // 4. Count.
    // count(start_pos, end_pos, which_element count);
    int count_ = count(v.begin(), v.end(), 54);
    cout <<"Our vector has only " << count_ << " times " <<54 << endl; 

    // 5. Find.
    auto it = find(v.begin(), v.end(), 10);
    if (it != v.end()){
        cout << *it << endl;
    }
    else{
        cout << "10 Not Found." << endl;
    }


    // 6. Reverse.
    reverse(v.begin(), v.end());
    cout << "The reverse vector is ";
    print_vector(v);
    cout << endl;
    */
    
    int n;
    cin >> n;
    int arr[n];
    for(int i=0; i<n; ++i){
        cin >> arr[i];
    }
    print_array(arr,n);
    

    // 1. Min_element . 
    // It returns address.
    // int min = *min_element(v.begin()+2, v.end());
    int min = *min_element(arr, arr+n);
    cout <<"The minimum element is: " << min << endl;
    
    // 2. Max_element. 
    // It returns address.
    int max = *max_element(arr, arr+n);
    cout <<"The maximum element is: " << max << endl;

    // 3. Accumulate.
    int sum = accumulate(arr, arr+n, 0); // 0+sum
    cout << "The sum of v is: " << sum << endl;

    // 4. Count.
    // count(start_pos, end_pos, which_element count);
    int count_ = count(arr, arr+n, 54);
    cout <<"Our vector has only " << count_ << " times " <<54 << endl; 

    // 5. Find.
    auto it = find(arr, arr+n, 10);
    if (it != arr+n){
        cout << *it << endl;
    }
    else{
        cout << "10 Not Found." << endl;
    }


    // 6. Reverse.
    reverse(arr, arr+n);
    cout << "The reverse vector is ";
    print_array(arr, n);
    cout << endl;





    return 0;
}