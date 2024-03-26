#include <iostream>
using namespace std;

int main(){
    int n;
    cin >> n;
    int ans = 0;
    for (int i=0; i<n; i++){
        ans = 0;
        int a,b;
        cin >> a >> b;
        for (int j = min(a,b)+1; j < max(a,b) ; j++){
            if (j % 2 != 0){
            ans += j;
            }
        }
        cout << ans << endl;
    }

    return 0;
}