// DATE ==> 17 AUGUST 2024
// TOPIC ==> SELECTION SORT Algorithm with Theory and Code.
#include <iostream>
using namespace std;

int main(){
/*
    int arr[1000];
    int n;
    cout << "Enter the Size of Array: ";
    cin >> n;

    for(int i=0; i<n; i++){
        cin >> arr[i];
    }

    // Selcection Sort Code 
    for(int i=0; i<n-1; i++){
        int index = i;

        for(int j=i+1; j<n; j++){
            if (arr[j] < arr[index]){
                index = j;
            }
        }
        swap(arr[i], arr[index]);
    }

    for(int i=0; i<n; i++){
        cout << arr[i]<< " ";
    }
*/

/*
    int arr[1000];
    int n;
    cout << "Enter the Size of Array: ";
    cin >> n;

    for(int i=0; i<n; i++){
        cin >> arr[i];
    }

    // Selcection Sort Code 
    for(int i=n-1; i>=0; i--){
        int index = i;

        for(int j=i-1; j>=0; j--){
            if (arr[j] > arr[index]){
                index = j;
            }
        }
        swap(arr[i], arr[index]);
    }

    for(int i=0; i<n; i++){
        cout << arr[i]<< " ";
    }
*/

    int arr[1000];
    int n;
    cout << "Enter the Size of Array: ";
    cin >> n;

    for(int i=0; i<n; i++){
        cin >> arr[i];
    }

    // Selcection Sort Code 
    for(int i=n-1; i>=0; i--){
        int index = i;

        for(int j=i-1; j>=0; j--){
            if (arr[j] < arr[index]){
                index = j;
            }
        }
        swap(arr[i], arr[index]);
    }

    for(int i=0; i<n; i++){
        cout << arr[i]<< " ";
    }
    return 0;
}