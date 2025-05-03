// DATE -----> 3 May 2025
// AUTHOR -----> SUMONTO
// PROBLEM ==> https://codeforces.com/problemset/problem/1985/D

#include <bits/stdc++.h>
using namespace std;
int main(){
    int tt; cin >> tt;
    while(tt--){
        int n,m; cin >> n >> m;
        vector<vector<char>> arr(n,vector<char>(m));
        vector<int> counter;
        int ans1 = 0, ans2 = 0;
        for(int i=0; i<n; i++){
            int a = 0;
            for(int j=0; j<m; j++){
                char x; cin >> x;
                arr[i][j] = x; 
                if (x == '#') a++;
            }
            counter.push_back(a);
            a = 0;
        }

        int max_ = 0; 
        for(int i=0; i<counter.size(); i++) {
            if(counter[i]>=max_){
                max_ = counter[i];
                ans1 = i;
            }
        }

        while(ans2<m && arr[ans1][ans2] != '#'){
            ans2++;
        }
        
        ans2+= floor(max_/2);
        cout << ans1+1 << " " << ans2+1 << endl;
        
    }


    return 0;
}