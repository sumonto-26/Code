#include <iostream>
#include <iomanip>

using namespace std;

int main(){
    int n;
    cin >> n;
    for (int i=0; i<n; i++){
        double a,b,c;
        cin >>a>>b>>c;
        double ans = (((a*2+b*3+c*5)/10));
        cout <<fixed << setprecision(1) << ans <<endl;
    }

    return 0;
}