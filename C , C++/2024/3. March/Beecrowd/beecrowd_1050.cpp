
#include <iostream>
using namespace std;

int main (){
    int ddd;
    cin >> ddd;

    int DDD[8] = {61, 71, 11, 21, 32, 19, 27, 31};
    string Destination[8] = {
        "Brasilia",
        "Salvador",
        "Sao Paulo",
        "Rio de Janeiro",
        "Juiz de Fora",
        "Campinas",
        "Vitoria",
        "Belo Horizonte",
        }; 

    for (int i = 0; i < 8; i++){
        if (ddd == DDD[i]){
            cout << Destination[i] << endl;
            break;
        }
        if (i == 7){
            cout << "DDD nao cadastrado" << endl;
        }
    }

    return 0;
}