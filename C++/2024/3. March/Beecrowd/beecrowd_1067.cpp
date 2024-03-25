#include <iostream>
using namespace std;

int main(){

    int number;
    cin >> number;

    for (int i=1; i < number+1; i += 2){
        cout << i << endl;
    }

    return 0;
}