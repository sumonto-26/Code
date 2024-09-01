// DATE ==> 15. AUGUST. 2024;
// TOPIC ==> Master Arrays By Solving Problems;

#include <iostream>
using namespace std;

int Linear_Search(int arr[], int target){
    for(int i=0; i<10; i++){
        if (arr[i] == target) return i;
    }
    return -1;
}

void Cyclic_Rotate(int arr[], int n) {
    if (n == 0) return;  // Check if the array is empty

    int a = arr[n-1];
    for(int i=n-2; i>=0; i--){
        arr[i+1] = arr[i];
    }
    arr[0] = a;
}

void print_array(int arr[], int size){
    for(int i=0; i<size; i++){
        cout << arr[i] << " ";
    }
    cout << endl;
}

int missingNumber(int nums[], int size) {
    int sum = 0;
    for (int i = 0; i < size; i++) {
        sum += nums[i];
    }
    // The formula for the sum of the first n natural numbers is n*(n+1)/2
    int expected_sum = (size * (size + 1)) / 2;
    return expected_sum - sum;
}

// Function to find the index of the maximum element in the array
int max_index(int arr[], int size) {
    int max_idx = 0;
    for (int i = 1; i < size; i++) {
        if (arr[i] > arr[max_idx]) {
            max_idx = i;
        }
    }
    return max_idx;
}

void function (int arr[], int size){
    // cout << sizeof(arr); // Note: sizeof(arr) inside this function gives the size of the pointer, not the size of the array.
    for(int i=0; i<size; i++){
        cout << arr[i] << " ";
    }
}



int main(){
/*
    int arr[10];
    cout << "Enter an array len 10: ";
    for(int i=0; i<10; i++){
        cin >> arr[i];
    }
    int target;
    cout << "Enter target: ";
    cin >> target;
    cout<<"arr[" << Linear_Search(arr, target)<<"]  == " << target << endl;

*/

 /*
    int array[10];
    for (int i=0; i<10; i++){
        cin >> array[i];
    }

    // Rule: 1;
    int temp[10] = {0};
    int i=10-1, j=0;
    while(i>=0){
        temp[j] = array[i];
        i--;
        j++;
    }
    print_array(temp, 10);    

    // Rule: 2;
    int i=0, j = (sizeof(array)/sizeof(array[0]))-1;
    while(i<j){
        swap(array[i], array[j]);
        i++;
        j--;
    }
    print_array(array,10);
*/


    ///// SECOND MAXIMUM ELEMENT /////
/*
    int arr[] = {50, 54, 12, 69, 31, 64, 37, 75, 82, 82};
    int max_1 = arr[max_index(arr, sizeof(arr)/4)];
    int max_2 = INT32_MIN;  // Initialize to the smallest possible value
    
    for (int i = 0; i < 10; i++) {
        if (arr[i] != max_1 && arr[i] > max_2) {  // Update max_2 if arr[i] is greater
            max_2 = arr[i];
        }
    }
    cout << "Second maximum: " << max_2 << endl;
    cout << "Maximum: " << max_1 << endl;
*/

/*
    int arr[] = {0, 1, 3, 4, 5, 6};
    int size = sizeof(arr) / sizeof(arr[0]);  // Calculate the size of the array
    cout << "Missing Number: " << missingNumber(arr, size) << endl;
*/
    
    //// FIBONACCI SERIES ////
    /*
    int n;
    cout << "Enter the n: "; 
    cin >> n;

    int fibonacci[1000] = {0,1}; // to give array size fixed is a good habit.
    for(int i = 2; i < n; i ++){
        fibonacci[i] = fibonacci[i-1] + fibonacci[i-2];
    }
    
    print_array(fibonacci, n);

    cout << fibonacci[n-1] << " is the nth fibonacci number." << endl;
    */

/*
    int N = 10;

    cout << "Enter 10 Numbers" << endl;
    int arr[10]; 
    for(int i=0; i<N; i++){
        cin >> arr[i];
    }
    Cyclic_Rotate(arr, N);
    print_array(arr, N);
*/

    int size = 10;
    cout << "Enter 10 Numbers"<<endl;
    int array[10];
    for(int i=0; i<size; i++){
        cin >> array[i];
    }
    cout << sizeof(array) << endl;
    function(array, size);



    return 0;
}