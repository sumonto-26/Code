#include <iostream>
using namespace std;

int main(){
    int n;
    cin >> n;
    for (int i=0; i<n; i++){
        int number;
        cin >> number;
        
        if (number == 0){
            cout << "NULL" << endl;
        } 
        else if (number < 0 && number % 2 != 0){
            cout << "ODD NEGATIVE" << endl;
        }
        else if (number < 0 && number % 2 == 0){
            cout << "EVEN NEGATIVE" << endl;
        }
        else if (number > 0 && number % 2 != 0){
            cout << "ODD POSITIVE" << endl;
        }
        else{
            cout << "EVEN POSITIVE" << endl;
        }
    }



    return 0;
}