// DATE ==> 29 December 2024;
// AUTHOR ==> SUMONTO
// Problem name ===> A. Everyone Loves to Sleep
// Problem Rating ==> 900
// time limit per test2 seconds
// memory limit per test256 megabytes

#include <bits/stdc++.h>
using namespace std;

int turn_minute(int h, int m){
    return h*60 + m;
}

int main(){
    int t; cin >> t;
    while(t--){
        int n; cin >> n;
        int H, M;
        cin >> H >> M;
        int distance = 1500;
        for(int i=0; i<n; i++){
            int h,m; 
            cin >> h >> m;
            if(turn_minute(H,M) > turn_minute(h,m)) distance = min(distance, (1440 - turn_minute(H,M)) + turn_minute(h,m));
            else distance = min(distance, turn_minute(h,m)-turn_minute(H,M));
            
        }
        int distance_m = distance%60, distance_h = distance/60;
        cout << distance_h <<" "<< distance_m << endl;
    }

    return 0;
}