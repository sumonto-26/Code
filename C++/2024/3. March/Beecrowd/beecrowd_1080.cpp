#include <iostream>
using namespace std;

int main(){
    int array[100];
    for (int i=0; i<=100; i++){
        cin >> array[i];
    }
    int valueToFind = 0;

    for(int j=0; j<=100; j++){
        if (array[j]>valueToFind){
            valueToFind = array[j];
        }
    }
    int index = -1;

    for (int k=0; k <= 100; ++k) {
        if (array[k] == valueToFind) {
            index = k;
            break;
        }
    }
    cout << valueToFind << endl;
    cout << index+1 << endl;

    return 0;
}