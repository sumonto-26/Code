#include <bits/stdc++.h>
using namespace std;
int main(){
    int da, db;
    cin >> da >> db;
    if (da == 9 && db == 1) cout << 9 << " " << 10 << endl;
    else if (db<da || db > da+1)  cout << "-1" << endl;
    else if (da == db) cout << (da*100)+1 << " " << (db*100)+2 << endl;
    else if(db = da+1) cout << (da*100)+99 << " " << (db*100) << endl; 
    else cout << "-1" << endl;
    return 0;
}