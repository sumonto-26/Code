// DATE ==> 7 May 2025
// AUTHOR ==> SUMONTO
// Video ==> https://www.youtube.com/watch?v=ZtSkN2aoCko&list=PLQEaRBV9gAFu4ovJ41PywklqI7IyXwr01&index=33&ab_channel=CoderArmy
// Topic ==> Lecture 33: Rotate Image | Rotate by 90 degree | Rotate Matrix Element Clockwise |Rotate Matrix 180


#include <bits/stdc++.h>
using namespace std;

void print_2D_array(int arr[4][4]){
    for(int i=0; i<4; i++){
        for (int j=0; j<4; j++){
            cout << arr[i][j] << " ";
        } cout << endl;
    } cout << endl;
}


int main(){

    // Rotate Image by 90 degree 
    // Time complexity O(n^2) and Space complexity O(n^2)
    int arr[4][4] = {{1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10, 11, 12}, {13, 14, 15, 16}};
    vector<vector<int> > vec(4, vector<int>(4));
    for(int i=0; i<4; i++)
        for (int j=0; j<4; j++)
            vec[j][3-i] = arr[i][j];
    
    for(int i=0; i<4; i++){
        for (int j=0; j<4; j++){
            cout << vec[i][j] << " ";
        } cout << endl;
    } cout << endl;
    
    // Rotate Image by 90 degree 
    // Time complexity O(n^2) and Space complexity O(1)
    int arr1[4][4] = {{1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10, 11, 12}, {13, 14, 15, 16}};
    for(int i=0; i<4-1; i++)
        for (int j=i+1; j<4; j++)
            swap(arr1[i][j], arr1[j][i]);
    
    for(int i=0; i<4; i++){
        int start = 0, end = 3;
        while(start<end){
            swap(arr1[i][start], arr1[i][end]);
            start++; end--;
        }
    }
    // Print the rotated matrix
    print_2D_array(arr1);


    // Rotate Image by 180 degree
    // Time complexity O(n^2) and Space complexity O(1)
    int arr2[4][4] = {{1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10, 11, 12}, {13, 14, 15, 16}};
    int n = 4;
        for(int i=0; i<n; i++){
            for (int j=i; j<n; j++)
                if (!(i==j && i >= n/2)) 
                    swap(arr2[i][j], arr2[n-i-1][n-j-1]);
        }

    // Print the rotated matrix
    // Time complexity O(n^2) and Space complexity O(1)
    print_2D_array(arr2);

    int arr3[4][4] = {{1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10, 11, 12}, {13, 14, 15, 16}};
    /*
    for(int i=0; i<4/2; i++){
        for(int j=0; j<4; j++){
            swap(arr3[i][j], arr3[3-i][j]);
        } 
    }
    */
    for(int j=0; j<4; j++){
        int start = 0, end = 3;
        while(start<end){
            swap(arr3[start][j], arr3[end][j]);
            start++; end--;
        }
    }

    // Reverse the rows of the matrix
    for(int i=0; i<4; i++){
        int start = 0, end = 3;
        while(start<end){
            swap(arr3[i][start], arr3[i][end]);
            start++; end--;
        }
    }
    print_2D_array(arr3);

    // Rotate Image by 270 degree or 90 degree anticlockwise
    // Time complexity O(n^2) and Space complexity O(1)
    int arr4[4][4] = {{1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10, 11, 12}, {13, 14, 15, 16}};
    for(int i=0; i<4-1; i++)
        for (int j=i+1; j<4; j++)
            swap(arr4[i][j], arr4[j][i]);

    for(int j=0; j<4; j++){
        int start = 0, end = 4-1;
        while(start<end){
            swap(arr4[start][j], arr4[end][j]);
            start++; end--;
        }
    }
    print_2D_array(arr4);

    // Rotate Image by k times   
    // Time complexity O(n^2) and Space complexity O(1)
    
    // int a = times%4; 
    // if(a == 0) cout << "No rotation" << endl;
    // else if (a == 1) cout << "Rotate by 90 degree" << endl;
    // else if (a == 2) cout << "Rotate by 180 degree" << endl;
    // else if (a == 3) cout << "Rotate by 270 degree" << endl;
    // else cout << "Invalid rotation" << endl;

    return 0;
}