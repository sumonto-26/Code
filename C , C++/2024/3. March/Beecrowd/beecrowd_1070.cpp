#include <iostream>
using namespace std;

int main(){
    int x;
    cin >> x;

    if (x % 2 == 0){
        for (int i = x+1; i < (x + 12); i += 2){
            cout << i<< endl;
        }
    }
    else{
        for (int i = x; i < (x + 11); i += 2){
            cout << i<< endl;
        }
    }

    return 0;
}