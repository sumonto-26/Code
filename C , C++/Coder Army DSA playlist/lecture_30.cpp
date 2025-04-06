// DATE ---> 6 April 2025
// Lecture 30: Trapping Rain Water || 3 SUM || 4 SUM

#include<bits/stdc++.h>
using namespace std;

int trap_bruteforce(vector<int> height) {
    int n = height.size();
    int leftmax[n], rightmax[n];
    leftmax[0] = 0;
    for(int i=1; i<n; i++){
        leftmax[i] = max(leftmax[i-1], height[i-1]);
    }
    rightmax[n-1] = 0;
    for(int i=n-2; i>=0; i--){
        rightmax[i] = max(rightmax[i+1], height[i+1]);
    }
    int water = 0, min_h;
    for(int i = 0; i<n; i++){
        min_h = min(leftmax[i], rightmax[i]);
        if(min_h-height[i] > 0) water += min_h-height[i];
    }
    return water;
}

int trap_best_way(vector<int> height){
    int maxleft = 0, maxright = 0, water = 0;
    int maxheight = height[0], index = 0;
    for(int i=1; i<height.size(); i++){
        if(height[i] > maxheight){
            maxheight = height[i];
            index = i;
        }
    }
    for(int i=0; i<index; i++){
        if(maxleft>height[i]) water += maxleft-height[i];
        else maxleft = height[i];
    }
    for(int i = height.size()-1; i>index; i--){
        if(maxright>height[i]) water += maxright-height[i];
        else maxright = height[i];
    }
    return water;
}

string three_sum_1(vector<int> arr, int x){
    int n = arr.size(); 
    for(int i=0; i<n-2; i++){
        for(int j=i+1; j<n-1; j++){
            for(int k=j+1; k<n; k++){
                if(arr[i]+arr[j]+arr[k] == x) return "YES";
            }
        }
    }
    return "NO";
}

string three_sum_2(vector<int> arr, int x){
    sort(arr.begin(), arr.end());
    for(int i=0; i<arr.size()-2; i++){
        for(int j=i+1; j<arr.size()-1; j++){
            int start = j+1, end = arr.size()-1, mid;
            while(start <= end){
                mid = start+(end-start)/2;
                if (arr[mid] == x-arr[i]-arr[j]) return "YES";
                else if (arr[mid] > x-arr[i]-arr[j]) end = mid-1;
                else start = mid+1;
            }
        }
    }
    return "NO";
}

string three_sum_3(vector<int> arr, int x){
    sort(arr.begin(), arr.end());
    int ans;
    for(int i=0; i<arr.size()-2; i++){
        ans = x-arr[i];
        int start = i+1, end = arr.size()-1;
        while (start<end){
            if(arr[start]+arr[end] == ans) return "YES";
            else if (arr[start]+arr[end] > ans) end--;
            else start++;
        }
    }
    return "NO";
}

int main(){
    int n; cin >> n;
    vector<int> height(n);
    for(int i=0; i<n; i++) cin >> height[i];
    cout << trap_best_way(height) << endl;
    cout << trap_bruteforce(height) << endl;


    return 0;
}