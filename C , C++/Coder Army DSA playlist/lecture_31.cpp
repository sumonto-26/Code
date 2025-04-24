// Video link --> https://www.youtube.com/watch?v=kP5EoGyTHbA&list=PLQEaRBV9gAFu4ovJ41PywklqI7IyXwr01&index=34&ab_channel=CoderArmy


#include <bits/stdc++.h>
using namespace std;

void print_col_wise(int arr[][4], int row, int col){
    // column wise
    for(int j=0; j<col; j++){
        for(int i=0; i<row; i++){
            cout << arr[i][j] << " ";
        }
        cout << endl;
    }
    cout << endl << endl;
}
void print_row_wise(int arr[][4], int row, int col){
    // row wise
    for(int i=0; i<row; i++){
        for(int j=0; j<col; j++){
            cout << arr[i][j] << " ";
        }
        cout << endl;
    }
    cout << endl << endl;
}

int main(){
/*
    // create 2D array
    int arr[3][4] = {1,2,3,4,5,6,7,8,9,10,11,12};

    // Print all the value in array row wise 
    for(int row=0; row<3; row++){
        for(int col=0; col<4; col++){
            cout<<arr[row][col]<< " ";
        }
        cout << endl;
    }
    cout << endl << endl;
    int rows = sizeof(arr) / sizeof(arr[0]);     // total size / size of one row
    int cols = sizeof(arr[0]) / sizeof(arr[0][0]); // size of one row / size of one element
    cout << rows << " " << cols<< endl << endl;
/*
    cout << endl << endl;
    // Print all the value in array col wise, function call
    print_col_wise(arr,3,4);
*/

/*
    // find and element in our array
    int target = 7;
    for(int i=0; i<3; i++){
        for(int j=0; j<4; j++){
            if(arr[i][j] == target) cout << i << " " << j << endl;
        }
    } 
*/

/*
    int arr1[3][4] = {10,12,11,4,5,6,7,8,9,1,3,2};
    print_row_wise(arr1,3,4);
    
    int arr2[3][4] = {23,11,5,7,19,13,17,31,2,27,29,3};
    print_row_wise(arr2,3,4);
    
    int sum_arr1_arr2[3][4];
    for(int row=0; row<3; row++){
        for(int col=0; col<4; col++){
            sum_arr1_arr2[row][col] = arr1[row][col] + arr2[row][col];
        }
    }
    print_row_wise(sum_arr1_arr2,3,4);

    //Print Row index with Max Sum
    int row = 3;
    int col = 4;
    int sum = -10000, index = 0;
    for(int i=0; i<row; i++){
        int total = 0;
        for(int j=0; j<col; j++){
            total += sum_arr1_arr2[i][j];
            if(sum < total){
                sum = total;
                index = i;
            }
        }
    }
    cout <<"Max Sum in "<< index <<" th row. ---> ";
    for(int i=0; i<col; i++) cout << " + " << sum_arr1_arr2[index][i];
    cout << endl << endl;
*/

    // Print Sum Of Diagonal Element
/*
    int arr[4][4] = {5,8,3,9,6,2,8,4,5,3,2,2,2,8,1,9};
    int first = 0, second = 0;
    for(int i=0; i<4; i++){
        first += arr[i][i];
        second += arr[(4-1)-i][i];
    }
    cout << first << " " << second << endl;
*/
    // Reverse each row of Matrix
    int arr[3][4] = {2,3,4,5,1,2,3,4,2,4,6,8};
    print_row_wise(arr,3,4);

    for (int i=0; i<3; i++){ // 3 == row number
        int start = 0, end = 4-1; // column number-1
        while(start < end){
            swap(arr[i][start], arr[i][end]);
            start++; end--;
        }
    }
    print_row_wise(arr,3,4);

    return 0;
}