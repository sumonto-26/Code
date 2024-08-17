// DATE ==> 17 AUGUST 2024 - 18 AUGUST 2024
// TIME ==> 11:50PM - 12:18AM
// AUTHOR ==> SUMONTO

#include <iostream>
using namespace std;
int main(){

    int n;
    // cout << "Enter a Number: ";
    cin >> n;

    int ans=0;
    while(n > 0){
        int power_of_2 = 1;
        while(power_of_2<=n){
            power_of_2 *= 2;
        }
        power_of_2 /= 2;
        // cout << power_of_2 << endl;
        n -= power_of_2;
        ans++;
    }
    cout << ans << endl;

    return 0;
}