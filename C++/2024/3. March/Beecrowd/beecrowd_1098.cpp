#include <iostream>
using namespace std;

int main(){
    double i = 0.0;
    double j1 = 1.0;
    double j2 = 2.0;
    double j3 = 3.0;

    for (int n=0; n<=10; n++){
        cout <<"I="<< i << " J=" << j1 <<endl;
        cout <<"I="<< i << " J=" << j2 <<endl;
        cout <<"I="<< i << " J=" << j3 <<endl;

        i+=0.2;
        j1+=0.2;
        j2+=0.2;
        j3+=0.2;
    }

    return 0;
}