// DATE ==> 17 AUGUST 2024
// TOPIC ==> Bubble Sort with Theory and Code.

#include <iostream>
using namespace std;

void print_array(int arr[], int n){
    for(int i = 0; i < n ; i++){
        cout << arr[i] << " " ;
    }
}

int main(){
    int n;
    cout << "Enter the size of Array: ";
    cin >> n;

/*
    int arr[1000];
    for(int i=0; i<n; i++)
        cin >> arr[i];
*/

/*
    for(int i=n-1; i>0; i--){
        bool is_swap = 0;
        for(int j = 0; j <= i; j++){
            if (arr[j] > arr[j+1]) {
                swap(arr[j], arr[j+1]);
                is_swap =  1;
            }
        }
        if (!is_swap) break; 
    }
    print_array(arr, n);
    cout << endl;
*/

/*
    for(int i=n-1; i>=0; i--){
        bool is_swap = 0;
        for(int j = 0; j < i; j++){
            if (arr[j] < arr[j+1]) {
                swap(arr[j], arr[j+1]);
                is_swap =  1;
            }
        }
        if (!is_swap) break; 
    }
    print_array(arr, n);
    cout << endl;
*/


/*
    for(int i = 0; i < n-1; i++) { 
        bool is_swap = 0;
        for(int j = n-1; j >= 0; j--) {
            if (arr[j] > arr[j+1]) {
                swap(arr[j], arr[j+1]);
                is_swap =  1;
            }
        }
        if (!is_swap) break; 
    }
    print_array(arr, n);
    cout << endl;
*/

    char name[1000];
    for(int i=0; i<n; i++){
        cin >> name[i];
    }

    for(int i = n-1; i>=0; i--){
        bool is_swap = 0;
        for(int j=0; j<=n-1; j++){
            if (name[j] > name[j+1]){
                swap(name[j], name[j+1]);
                is_swap = 1;
            }
        }
        if (!is_swap) break;
    }
    for(int i=0; i<n; i++){
        cout << name[i] << " ";
    }
    cout << endl;

    return 0;
}