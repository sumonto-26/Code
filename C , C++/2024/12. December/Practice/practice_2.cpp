// DATE ==> 19 becember 2024
#include <bits/stdc++.h>
using namespace std;

void bubble_sort(vector<int> vec, int n){
    for(int i = 1 ; i<n; i++){
        bool swaped = false;
        for(int j=0; j<n-i; j++){
            if(vec[j] > vec[j+1]){
                swaped = true;
                swap(vec[j], vec[j+1]);
            }
        } if (swaped == false) break;
    }
    for(auto value: vec)  cout << value << " ";
    cout << endl;
}

void first_position_of_target(vector<int> vec, int n, int target){
    int start = 0, end = n-1, ans = -1;
    while(start <= end){
        int mid = (end+start)/2;
        if (vec[mid] == target){
            end = mid - 1;
            ans = mid;
        }
        else if (vec[mid] < target) start = mid + 1;
        else end = mid-1;
    }
    cout << ans << " is the first position of " << target << endl;
}

void last_position_of_target(vector<int> vec, int n, int target){
    int start = 0, end = n-1, ans = -1;
    while(start <= end){
        int mid = (end+start)/2;
        if (vec[mid] == target){
            start = mid + 1;
            ans = mid;
        }
        else if (vec[mid] < target) start = mid + 1;
        else end = mid-1;
    }
    cout << ans << " is the last position of " << target << endl;
}

void insertion_sort(vector<int> vec, int n){
    for(int i = 1; i<n; i++){
        for(int j = i; j>0; j--){
            if(vec[j] < vec[j-1]){
                int temp = vec[j];
                vec[j] = vec[j-1];
                vec[j-1] = temp; 
            }
            else break;
        }
    }
    for(int i=0; i<n; i++){
        cout << vec[i] << " ";
    }
    cout << endl;
}

void selection_sort(vector<int> vec, int n){
    for(int i=0; i<n-1; i++){
        int min_ind = i;
        for(int j = i+1; j<n; j++){
            if (vec[min_ind] > vec[j]) min_ind = j;
        }
        swap(vec[i], vec[min_ind]);
    }

    for (auto value: vec){
        cout << value << " ";
    } cout << endl;
}

int main(){
/*
    int n; cin >> n;
    vector<int> vect(n);
    for(int i = 0; i < n; i++){
        cin >> vect[i];
    }
    bubble_sort(vect, n);
*/

/*
    cout << "Enter your vector lenght --> ";
    int n; cin >> n;
    cout << "Enter a sorted vector -----> "; 
    vector<int> vec(n);
    for(int i = 0; i< n; i++){
        cin >> vec[i];
    }

    int target;
    cout << "Enter the target --> ";
    cin >> target;
    first_position_of_target(vec, n, target);
    last_position_of_target(vec, n, target);

    int len; 
    cout << "Enter the len ---> ";
    cin >> len;
    vector<int> vec(len);
    cout << "Enter the unsorted vector ---> ";
    for(int i=0; i<len; i++){
        cin >> vec[i];
    }
    insertion_sort(vec, len);
    selection_sort(vec, len);
*/

/*
    int n;
    cout << "Enter a number ---> ";
    cin >> n;
    for(int i=1; i<=n; i++){
        // Print Spaces;
        for(int j=0; j <= 2; j++) cout << " ";
        for(int k = 1; k<= i; k++) cout << "* ";
        cout << endl;
    }
*/

    


    return 0;
}