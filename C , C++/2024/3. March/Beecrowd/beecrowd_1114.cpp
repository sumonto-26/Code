#include <iostream>
using namespace std;

int main(){

    while (true){
        int password;
        cin >> password;
        if (password == 2002){
            cout << "Acesso Permitido" << endl;
            break;
        }
        else{
            cout << "Senha Invalida" << endl;
        }

    }
    
    return 0;
}