// DATE ==> 21 April 2024
// Author ==> SUMONTO

# include <bits/stdc++.h>
using namespace std;

int main(){
    int n;
    cin >> n;
    for (int i=0; i<n; ++i){
        string a;
        cin >> a;
        int s = a.size();
        int num = stoi(a);
        int t = (((num)%10)-1)*10;
        int l = (s*(s+1))/2;
        cout << t+l << endl;

    }
    return 0;
}