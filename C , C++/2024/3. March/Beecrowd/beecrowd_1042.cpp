#include <iostream>
using namespace std;

void bubbleSort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                // Swap arr[j] and arr[j+1]
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}

// Function declaration
std::string print_ans(const int arr[], int n) {
    // Example: Concatenate all elements of the array into a string
    std::string result;
    for (int i = 0; i < n; ++i) {
        result += std::to_string(arr[i]) + "\n";
    }
    return result;


}
int main(){

    int n = 3;
    int* arr = new int[n];
    for (int i = 0;  i<n; i++){
        cin >> arr[i];
    }

    string ans = print_ans(arr, n);
    bubbleSort(arr, n);
    cout << print_ans(arr, n);
    cout << endl;
    cout << ans;    


    return 0;
}