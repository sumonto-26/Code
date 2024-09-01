// DATE ==> 28 JULY 2024
// Topic ==> Solve Any Pattern Problem with Simple Trick Part-2

#include <iostream>
using namespace std;

int main(){

/*
    int x;
    cout << "Enter a Number between 1-50 : ";
    cin >> x;

    for(int row=1; row <= x; row++){
        for(int col=1; col <= row; col++){
            cout << "* ";
        }
        cout << endl;
    }
*/

/*
    for(int row = 1; row <= 5; row++){
        for(int col=1; col <= row; col++){
            cout << col << " ";
        }
        cout << endl;
    }
*/

/*
    for(int row = 1; row <= 5; row++){
        for(int col = 1; col <= row; col++){
            cout << row << " ";
        }
        cout << endl;
    }
*/

/*
    for(int row=1; row <=5; row++){
        for(int col = row; col >= 1; col--){
            cout << col << ' ';
        }
        cout << endl;
    }
*/

/*
    for (char row = 1; row <= 26; row ++){
        char ch = 'a'+(row-1);
        for(int col = 1; col<=row; col++){
            cout << ch << "  "; 
        }
        cout << endl;
    }
*/

/*
    for (int row = 1; row <= 5; row ++){
        for (int col = row; col <= 5; col ++){
            cout << "* ";
        }
        cout << endl;
    }
*/

/*
    for (int row = 1; row <= 5; row++){
        for (int col = 1; col <= 6-row; col++){
            cout << col << ' ';
        }
        cout << endl; 
    }
*/

    for(int row = 1; row <= 5; row++){
        for(int col = 5; col >= 6-row; col--){
            cout << col << ' ';
        }
        cout << endl;
    }




    return 0;
};