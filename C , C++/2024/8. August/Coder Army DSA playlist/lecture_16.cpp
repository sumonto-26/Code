// DATE ==> 14 AUGUST 2024;
// TOPIC ==> Introduction To Arrays in C++

#include <iostream>
using namespace std;

void print_array(int arr[], int len) {
    for(int i = 0; i < len; i++) {
        cout << arr[i] << " ";
    }
    cout << endl << endl;
}


int main(){

    int arr[5]; // array declare
    cout << "Garbage Value "<< " ";
    print_array(arr, 5);
    
    int a[5] = {4,3,2,5,6};
    print_array(a, 5);

    int b[] = {4,2,1,45,67,4,3,22,5,6,3};
    print_array(b,11);

    int c[10];
    cout << "Enter 10 numbers ";
    for(int i=0; i<10; i++){
        cin >> c[i];
    }
    print_array(c,10);

    int d[10] = {3,2,4,1,5};
    cout << "5 Garbage Value "<< " ";
    print_array(d, 10);

    int e[10] = {0};
    cout << "9 Garbage Value "<< " ";
    print_array(e, 10);

    int f[10] = {4};
    cout << "4 Garbage Value "<< " ";
    print_array(f, 10);

    int size;
    cout << "Enter The size of your array ==> ";
    cin >> size;
    // int array[size]; // Bad Habit
    int array[1000]; // Good Habit
    for(int i=0; i<size; i++){
        cin >> array[i];
    }
    print_array(array, size);

    // SIZE_OF
    int n = 1000;
    cout << sizeof(n) << " it is a sizeof an int which is 4 bytes or 16 bits " << endl;
    // length of an array is sizeof(arr_name)/sizeof(element_type);

    // Minimum Element of an array;
    int minimum[10] = {5,2,8,56,65,4,545,2,213,20};
    int ans = INT32_MAX;

    for(int i=0; i<sizeof(minimum)/sizeof(minimum[0]); i++){
        if(minimum[i] < ans) 
        ans = minimum[i];
    }
    
    print_array(minimum, 10);
    cout << "Minimum ==> " << ans << endl;

    int maximum[10] = {50,25,8,5,605,24,545,2,213,20};
    int ans2 = 0;
    for(int i=0; i<sizeof(maximum)/sizeof(maximum[0]); i++){
        if(maximum[i] > ans2) 
        ans2 = maximum[i];
    }

    print_array(maximum, 10);
    cout << "Maximum ==> " << ans2 << endl;

    return 0;
}