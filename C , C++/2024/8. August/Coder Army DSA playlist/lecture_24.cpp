// DATE ==> 31 AUGUST 2024
// TOPIC ==> Search in a Rotated Array | Peak index in a Mountain Array | Kth Missing Positive Number
#include <bits/stdc++.h>
using namespace std;

int peakIndexInMountainArray(vector<int>& arr) {
    int start = 1, end = arr.size()-2;
    while(start <= end){
        int mid = start + (end-start)/2;
        if (arr[mid] >= arr[mid-1] && arr[mid] >= arr[mid+1]) return mid;
        else if (arr[mid] >= arr[mid-1])
            end = mid-1;
        else start = mid+1;
    }
    return 0;
}

int Find_Min_In_Rotated_Sorted_Array(vector<int>& nums) {
    int start = 0, end = nums.size()-1, ans = nums[0];
    while(start <= end){
        int mid = start+(end-start)/2;
        if(nums[mid] < nums[0]){
            ans = nums[mid];
            end = mid-1;
        }
        else start = mid+1;
    }
    return ans;
}

int Search_In_Rotated_Array(vector<int>& arr, int target){
    int start = 0, end = arr.size()-1, mid;
    while(start <= end){
        mid = start+(end-start)/2;
        if(arr[mid] == target) return mid;
        else if (arr[mid] >= arr[0]){
            if(arr[start] <= target && arr[mid] > target)
                end = mid - 1;
            else start = mid + 1;
        }
        else{
            if(arr[mid] < target && arr[end] >= target)
                start = mid + 1;
            else end = mid-1;
        }
    }
    return -1;
}

int findKthPositive(vector<int>& arr, int k) {
    int start = 0, end = arr.size()-1, mid, ans = arr.size();
    while(start <= end){
        mid = start+(end-start)/2;
        if(arr[mid]-mid-1 >= k){
            ans = mid;
            end = mid-1;
        }
        else start = mid+1;
    }
    return ans+k;

}

int main(){

    return 0;
}