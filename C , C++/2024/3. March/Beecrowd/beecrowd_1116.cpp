#include <iostream>
#include <iomanip>
using namespace std;

int main(){
    int n;
    cin >> n;
    for (int i=0; i<n; i++){
        double x,y;
        cin >> x; 
        cin >> y;
        double ans = x/y;

        if (y == 0){
            cout << "divisao impossivel" << endl;
        }
        else{
            cout << fixed << setprecision(1) << ans <<endl;
        }
    }
    return 0;
}