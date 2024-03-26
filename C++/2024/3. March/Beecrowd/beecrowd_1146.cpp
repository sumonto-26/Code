#include <iostream>
using namespace std;

int main(){

    while (true){
        int number ;
        cin >> number;
        
        if (number == 0){
            break;
        }
        else{
            for (int i=1; i<=number; i++){
                cout << i << " ";
            }
        cout << endl;
        }
    }

    cout << endl;
    return 0;
}