#include <iostream>
using namespace std;

int main(){

    int a,b,c;
    cin >> a;
    cin >> b;
    cin >> c;

    int ans = 0;

    if (a>b){
        if (a>c){
            ans = a ;
        }
        else{
            ans = c;
        }
    }

    else if (b>a){
        if (b>c){
            ans = b;
        }
        else{
            ans = c;
        }
    }

    else{
        if (b>c){
            ans = b;
        }
        else{
            ans = c;
        }
    }

    cout << ans << " eh o maior" << endl;

    return 0;
}