#include<iostream>
#include<iomanip>
using namespace std;

int main(){

    const int SIZE = 6;
    float arr[SIZE];

    for (int i = 0; i < SIZE; ++i) {
        cin >> arr[i];
    }

    float answer = (arr[1]*arr[2]) + (arr[4]*arr[5]);

    cout << "VALOR A PAGAR: R$ " << fixed << setprecision(2) << answer << endl;


    return 0;
}