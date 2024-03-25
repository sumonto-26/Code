#include <iostream>
using namespace std;

int main(){
    int I = 1, J = 60;
    int n = J/5;
    for (int i=0; i<n+1; i++){
        cout <<"I="<<I<<" "<<"J="<<J<<endl;
        I += 3;
        J -= 5; 
    }

    return 0;
}