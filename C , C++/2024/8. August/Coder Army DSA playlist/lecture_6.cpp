// DATE ==> 28 JULY 2024
// Topic ==> Solve Any Pattern Problem With Simple Trick Part-1

#include <iostream>
using namespace std;

int main(){

/*
    for(int i = 1; i<=5; i++){ // Row
        for(int j=1; j<=5; j++){ // Column
            cout << "* " ;
        }
        cout << endl;
    }
*/

/*
    int col, row;
    for (row=1; row<=5; row ++){
        for(col=1; col<=5; col ++){
            cout << "10 ";
        }
        cout << endl;
    }
*/

/*
    int col,row;
    for(row=1; row<=5; row ++){
        for (col=1; col<=5; col ++){
            cout << row << " ";
        }
        cout << endl;
    }
*/

/*
    int col,row;
    for(row=1; row<=5; row ++){
        for (col=1; col<=5; col ++){
            cout << col << " ";
        }
        cout << endl;
    }
*/

/*
    int i,j;
    for (i=5; i>=1; i--){
        for (j=5; j>=1; j--){
            cout << j << ' ';
        }
        cout << endl;
    }
*/

/*
    for (int i=1; i<=5; i++){
        for (int j=1; j<=5; j++){
            cout << j*j << " ";
        }
        cout << endl;
    }
*/

/*
    for(char c='a'; c<='e'; c++){
        for (int i=1; i<=5; i++){
            cout << c << ' ';
        }
        cout << endl;
    }
*/

/*
    for (int i=1; i<=5; i++){
        char c = 'a'+(i-1);
        for(int j=1; j<=5; j++){
            cout << c << " ";
        }
        cout << endl;
    }
*/

/*
    for (int i=1; i<=5; i++){
        for (char c = 'a'; c <= 'e'; c++){
            cout << c << ' ';
        }
        cout << endl;
    }
*/

    for (int row=1; row<=5; row++){
        for (int col=1; col<=5; col++){
            cout << col + ((row-1)*5) << ' ';
        }
        cout << endl;
    }
    cout << endl;


    int counter = 1;
    for (int row=1; row<=5; row++){
        for (int col=1; col<=5; col++){
            cout << counter << ' ';
            counter ++;
        }
        cout << endl;
    }


    return 0;
};