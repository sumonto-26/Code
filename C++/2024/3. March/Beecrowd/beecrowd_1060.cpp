#include <iostream>
using namespace std;

int main(){

    int ans = 0;

    for (int i = 0; i < 6; i++){
        double n ;
        cin >> n;
        if (n > 0){
            ans++;
        }
    }
    cout << ans << " valores positivos" << endl;

    return 0;
}