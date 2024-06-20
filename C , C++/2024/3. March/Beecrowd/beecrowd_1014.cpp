#include <iostream>
#include <iomanip>
using namespace std;

int main(){
    
    double distance, fuel;
    cin >> distance;
    cin >> fuel;

    cout << fixed << setprecision(3) << distance/fuel << " km/l" << endl;

    return 0;
}