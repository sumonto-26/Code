#include <iostream>
using namespace std;

int main(){

    int ans = 0;

    for (int i = 0; i < 5; i++){
        int n ;
        cin >> n;
        if (n%2 == 0){
            ans++;
        }
    }
    cout << ans << " valores pares" << endl;

    return 0;
}