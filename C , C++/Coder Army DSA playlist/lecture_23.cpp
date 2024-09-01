// 29 AUGUST 2024
// TOPIC ==>  Binary Search Different Problem || Search Insert Position || Sqrt(x) || Count occurrence.

#include <bits/stdc++.h>
using namespace std;

int find_first_target(int arr[], int n, int target){
    int start = 0, end = n-1;
    int ans = -1;
    while(start <= end){
        int mid = start+(end-start)/2;
        if(arr[mid] == target){
            ans = mid;
            end = mid - 1;
        }
        else if (arr[mid] > target)
            end = mid - 1;
        else start = mid + 1;
    }
    return ans;
}

int find_last_target(int arr[], int n, int target){
    int start = 0, end = n-1;
    int ans = -1;
    while(start <= end){
        int mid = start+(end-start)/2;
        if(arr[mid] == target){
            ans = mid;
            start = mid + 1;
        }
        else if (arr[mid] > target)
            end = mid - 1;
        else start = mid + 1;
    }
    return ans;
}

int searchInsert(vector<int>& nums, int target) {
    int answer = nums.size(), start = 0, end = nums.size()-1;
    while(start <= end){
        int mid = start + (end-start)/2;
        if(nums[mid] == target) return mid;
        else if (nums[mid] < target)  start = mid + 1;
        else{
            answer = mid;
            end = mid - 1;
        }
    }
    return answer;
}

int mySqrt(int x){
    if(x < 2) return x;

    int start=0, end=x, ans;
    while(start <= end){
        int mid = start+(end-start)/2;
        if (mid == x/mid) return mid;
        else if (mid < x/mid){
            ans = mid;
            start = mid+1;
        }
        else end = mid-1;
    }
    return ans;
}


int main(){
/*
    int n; cin >> n;
    int arr[1000];
    for(int i = 0 ; i < n; i++){
        cin >> arr[i];
    }
    int target; cin >> target;
    cout << find_first_target(arr, n, target) << " " << find_last_target(arr, n, target) << endl;
*/

    int n; cin >> n;
    vector <int> nums(n);
    for(int i = 0; i<n; i++){
        cin >> nums[i];
    }
    int target; cin >> target;
    cout << searchInsert(nums,target);


    return 0;
}