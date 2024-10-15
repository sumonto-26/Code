// DATE ==> 6 September 2024
// TOPIC ==> Binary Search Hard Interview Problem || Aggressive Cow || KOKO Eating Banana.
// VIDEO LINK ==> https://www.youtube.com/watch?v=ThCyc5GcuRQ&t=1251s

#include <bits/stdc++.h>
using namespace std;

// Leetcode ==> 1552. Magnetic Force Between Two Balls

// Is possible to assign all magnets;
/*
bool isPossible(vector<int>& position, int m, int mid){
    int basket = position[0], basket_num = 1; 
    for(int i=1; i<position.size(); i++){
        if( position[i] >= mid+basket){
            basket_num++;
            basket = position[i];
        }
    }
    return basket_num >= m;
}
int maxDistance(vector<int>& position, int m) {
    sort(position.begin(), position.end());
    int start = 0, end = position[position.size()-1] - position[0], mid, ans = -1;
    while(start <= end ){
        mid = start + (end-start) / 2;
        if(isPossible(position, m, mid)){
            ans = mid;
            start = mid+1;
        }
        else end = mid-1;
    }
    return ans;
}
*/

// Aggressive Cows
/*
bool isPossible(int mid, vector<int> stalls, int k){
    int count_cows = 1, current_cow = stalls[0];
    for(int i=1; i<stalls.size(); i++){
        if(current_cow+mid <= stalls[i]){
            count_cows++;
            current_cow = stalls[i];
        }
    }
    return count_cows>=k;
}

int solve(int n, int k, vector<int> &stalls) {
    sort(stalls.begin(), stalls.end());
    
    int start = 1, end = stalls[stalls.size()-1]-stalls[0];
    int ans = -1;
    
    while(start <= end){
        int mid = end+(start-end)/2;
        if(isPossible(mid, stalls, k)){
            ans = mid;
            start = mid+1;
        }
        else end = mid-1;
    }
    return ans;
}
*/

// Koko eating bananas
bool Can_Eat_All_Bananas(vector<int> piles, int h, int speed){
    int eating_time = 0;
    for(int i=0; i<piles.size(); i++){
        if (piles[i]%speed == 0) eating_time += piles[i]/speed;
        else  eating_time += (piles[i]/speed)+1;
    }
    return h >= eating_time;
}

int minEatingSpeed(vector<int>& piles, int h) {
    long long start = 1, end = 0, ans;
    for(int i=0; i<piles.size(); i++)  end += piles[i];
    while(start <= end){
        long long  mid = end+(start-end)/2;
        if(Can_Eat_All_Bananas(piles, h, mid)){
            ans = mid;
            end = mid-1;
        }
        else start = mid+1;
    } 
    return ans;
}


int main(){

    return 0;
}