#include <iostream>
using namespace std;

int main(){
    for(int i=0; i<4000; i++){
        int a,b;
        cin >> a >> b;
        if (a != b){
            if (a > b){
                cout << "Decrescente" << endl;
            }
            else{
                cout << "Crescente" <<endl;
            }
        }
        else{
            break;
        }
    }

    return 0;
}