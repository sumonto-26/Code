// 1017 //
#include <iostream>
#include <iomanip>
using namespace std;

int main(){

    double time, speed;
    cin >> time;
    cin >> speed;

    double fuel = (time * speed) / 12;
    cout << fixed << setprecision(3) << fuel << endl;

    return 0;
}
