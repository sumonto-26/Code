// DATE ==> 23 DECEMBER 2024
// TOPIC ==> Lecture 28: Two Pointer in C++ | TWO SUM | Pair Sum | Pair Difference | Move 0 to end
// LINK ==> https://www.youtube.com/watch?v=KKPjlsLSs5w&list=PLQEaRBV9gAFu4ovJ41PywklqI7IyXwr01&index=29&t=28s&ab_channel=CoderArmy
#include <bits/stdc++.h>
using namespace std;


// 1: Segregate 0s and 1s
void Segregate_0s_and_1s_1(vector<int> vec){
    sort(vec.begin(), vec.end());
    for(int value: vec){
        cout << value << " ";
    } cout << endl;
}
void Segregate_0s_and_1s_2(vector<int> vec){
    int count_1 = 0, count_0 = 0;
    vector<int> answer;
    for(int i=0; i<vec.size(); i++){
        if(vec[i] == 1) count_1++;
        else count_0++;
    }
    for(int i = 0; i<count_0; i++) answer.push_back(0);
    for(int i = 0; i<count_1; i++) answer.push_back(1);
    
    for(auto value : answer) cout << value << " ";
    cout << endl;
}
void Segregate_0s_and_1s_3(vector<int> vec){
    int start = 0, end = vec.size()-1;
    while(start <= end){
        if(vec[start] == 1 && vec[end] == 0) swap(vec[start], vec[end]);
        else if(vec[start] == 1 && vec[end] == 1) end--;
        else if(vec[start] == 0 && vec[end] == 0) start++;
        else{
            start++;
            end--;
        }
    }
    for(int i = 0; i<vec.size(); i++){
        cout<< vec[i] << " ";
    }cout << endl;
}
void Segregate_0s_and_1s_4(vector<int> vec){
    int start = 0, end = vec.size()-1;
    while(start <= end){
        if(vec[start] == 0 ) start++;
        else{
            if(vec[end] == 0) swap(vec[start], vec[end]);
            else end--;
        } 
    }
    for(auto value: vec){
        cout << value << " "; 
    }cout << endl;
}

// 2: TWO SUM
int two_sum_1(vector<int> arr, int target){
    for(int i=0; i<arr.size()-1; i++){
        for(int j=i+1; j<arr.size(); j++){
            if(arr[i]+arr[j] == target){
                cout<< i+1 << " " << j+1 << endl;
                return 0; 
            }
        }
    }
    cout<< "NOT FOUND" << endl;
}
int two_sum_2(vector<int> arr, int target){
    for(int i=0; i<arr.size()-1; i++){
        int start = i+1, end = arr.size()-1, mid;
        while(start <= end){
            int mid = start+(end-start)/2;
            if(arr[mid] == target-arr[i]){
                cout << i+1 << " " <<  mid+1 << endl;
                return 0;
            } 
            else if(arr[mid] < target-arr[i]) start = mid+1;
            else end = mid-1;
        }
    }
    cout << "NOT FOUND" << endl;
    return 0;
}
int two_sum_3(vector<int> arr, int target){
    int start = 0, end = arr.size()-1;
    while(start < end){
        if(arr[start] + arr[end] == target) {
            cout << start+1 << " " << end+1 << endl;
            return 0;
        }
        else if(arr[start] + arr[end] < target) start++;
        else end--;
    }
    cout << "NOT FOUND" << endl;
    return 0;
}

// 3: Pair With Given Difference
int Pair_with_given_difference_1(vector<int> vec, int target){
    for(int i=0; i<vec.size()-1; i++){
        for(int j=i+1; j<vec.size(); j++){
            if(vec[i]-vec[j] == target || vec[j]-vec[i] == target){
                cout << i+1 << " " << j+1 << endl;
                return 0;
            }
        }
    }
    cout << "NOT FOUND!!!" << endl;
}
int Pair_with_given_difference_2(vector<int> vec, int target){
    sort(vec.begin(), vec.end()); 
    if(target < 0) target = target*-1; 
    int start = 0, end = 1;
    while(end<vec.size()){
        if(vec[end]-vec[start] == target){
            cout << vec[end] << "-" << vec[start] << " == " << target << endl; 
            return 1;
        }
        else if(vec[end] - vec[start] < target ) end++;
        else start++;
        if(start == end) end ++;
    }
    cout << "NOT FOUND!!!" << endl;
    return 0;
}


int main(){
/*
    int n; cin >> n;
    vector<int> vec(n);
    for(int i=0; i<n; i++){
        cin >> vec[i];
    }
    Segregate_0s_and_1s_1(vec);
    Segregate_0s_and_1s_2(vec);
    Segregate_0s_and_1s_3(vec);
    Segregate_0s_and_1s_4(vec);
*/
/*
    cout << "Enter the N ---> ";
    int n; cin >> n;

    cout << "Enter the Sorted Vector ---> ";
    vector<int> vec(n);
    for(int i=0; i<n; i++){
        cin >> vec[i];
    }
    cout << "Enter the Target ---> " ;
    int target; cin >> target;

    two_sum_1(vec, target);
    two_sum_2(vec, target);
    two_sum_3(vec, target);
*/
    cout << "Enter n : ";
    int n; cin >> n;
    
    cout << "Enter the vector ---> ";
    vector<int> vec(n);
    for(int i=0; i<n; i++){
        cin >> vec[i];
    }

    cout << "Enter the target ----> ";
    int target; cin >> target;

    Pair_with_given_difference_1(vec, target);
    Pair_with_given_difference_2(vec, target);



    return 0;
}