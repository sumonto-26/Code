#include <iostream>
using namespace std;

int main(){
    int even = 0;
    int odd = 0;
    int positive = 0;
    int negative = 0;

    for(int i=0; i<5; i++){
        int number;
        cin >> number;

        if (number % 2 == 0){
            even++;
        }
        if (number % 2 != 0){
            odd++;
        }
        if (number > 0){
            positive++;
        }
        if (number < 0){
            negative++;
        }
    }
    cout << even << " valor(es) par(es)" << endl;
    cout << odd << " valor(es) impar(es)" << endl;
    cout << positive << " valor(es) positivo(s)" << endl;
    cout << negative << " valor(es) negativo(s)" << endl;

    return 0;
}