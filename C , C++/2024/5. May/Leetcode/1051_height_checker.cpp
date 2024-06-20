#include <bits/stdc++.h>
using namespace std;


int main(){
    vector <int> heights = {1,1,4,2,1,3};

    vector<int> sorted_heights = heights;
    int ans = 0; 
    sort(sorted_heights.begin(), sorted_heights.end());
    for (int i=0; i<heights.size(); ++i){
        if (sorted_heights[i] != heights[i]){
            ans ++;
        }
    }

    cout << ans <<endl;

    return 0;
}