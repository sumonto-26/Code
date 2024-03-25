#include <iostream>
using namespace std;

int main(){

    int a,b;
    cin >> a;
    cin >> b;
    
    int ans = 0;
    for (int i = a-1; i > b; i--){
        if (i%2 != 0){
            ans += i;
        }
    }

    cout << ans << endl;

    return 0;
}