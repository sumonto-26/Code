// DATE ==> 9 June 2024
// AUTHOR ==> SUMONTO

#include <bits/stdc++.h>
using namespace std;

void solve(string m[]){
    for (int i=1; i<7; i++){
        for (int j=1; j<7; j++){
            if(m[i][j] == '#'){
                if (m[i-1][j-1] == '#' &&
                    m[i-1][j+1] == '#' &&
                    m[i+1][j-1] == '#' &&
                    m[i+1][j+1] == '#'
                    ){
                    cout << i+1 << " "<< j+1 << endl;
                } 
            }
        }
    }
}
int main(){
    int tt;
    cin >> tt;
    while(tt--){
        string m[8];
        for(int a=0; a<8; a++){
            cin >> m[a];
        }
        solve(m);
    }
    
    return 0;
}