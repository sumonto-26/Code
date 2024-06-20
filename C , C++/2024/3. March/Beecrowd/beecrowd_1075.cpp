#include <iostream>
using namespace std;

int main(){
    int number;
    cin >> number;

    for(int i=2; i<10001; i+=number){
        cout << i << endl;
    }

    return 0;
}