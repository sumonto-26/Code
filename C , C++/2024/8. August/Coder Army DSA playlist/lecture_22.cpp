// DATE ==> 18 AUGUST 2024
// TOPIC ==> Binary Search with Theory and Code.

#include <iostream>
using namespace std;

void Binary_Search_increasing(int arr[], int n, int target){
    int start = 0, end = n-1;
    while(start <= end){
        int mid = start+(end-start)/2; 
        if (arr[mid] == target){
            cout << target << " is found in index " << mid << endl; 
            return ;
        } 
        else if (arr[mid] > target) end = mid-1;
        else if(arr[mid] <  target) start = mid+1;
    }
    cout << "Not Found" << endl;
}


void Binary_Search_decreasing(int arr[], int n, int target){
    int start = 0, end = n-1;
    while(start <= end){
        int mid = start+(end-start)/2; 
        if (arr[mid] == target){
            cout << target << " is found in index " << mid << endl; 
            return ;
        } 
        else if (arr[mid] < target) end = mid-1;
        else if(arr[mid] >  target) start = mid+1;
    }
    cout << "Not Found" << endl;
}


int main(){
    int n;
    cout << "Enter the length of array: ";
    cin >> n;

    int arr[1000];
    for(int i=0; i<=n-1; i++){
        cin >> arr[i];
    }
    int target;
    cout << "Enter The Target: ";
    cin >> target;

    // Binary_Search_decreasing(arr, n, target);
    // Binary_Search_increasing(arr, n, target);
    

    return 0;
}