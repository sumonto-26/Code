// DATE ==> 17 AUGUST 2024
// TOPIC ==> Insertion Sort with Theory and Code.

#include <iostream>
using namespace std;

void print_array(int array[], int lenght){
    for(int index = 0; index < lenght; index++){
        cout << array[index] << " ";
    }
}

int main(){
    int lenght;
    cout << "Enter the size of Array: ";
    cin >> lenght;

    int array[1000];
    for(int i = 0; i < lenght; i++)
        cin >> array[i];


    for(int i = 1; i <= lenght; i++){
        for(int j = i-1; j > 0; j--){
            if(array[j-1] > array[j])
                swap(array[j], array[j-1]);
            else break;
        }
    }
    print_array(array,lenght);
    cout << endl;



    for(int i = 1; i <= lenght; i++){
        for(int j = i-1; j > 0; j--){
            if(array[j-1] < array[j])
                swap(array[j], array[j-1]);
            else break;
        }
    }
    print_array(array,lenght);
    cout << endl;



    for(int i = 1; i <= lenght; i++){
        for(int j = 0; j <= i-2; j++){
            if(array[j+1] > array[j])
                swap(array[j], array[j+1]);
            else break;
        }
    }
    print_array(array,lenght);
    cout << endl;



    return 0;
}