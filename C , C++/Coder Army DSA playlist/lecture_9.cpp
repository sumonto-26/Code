// DATE ==> 29 JULY 2024
// Topic ==> Top 5 Advance Pattern Print Problems

#include <iostream>
using namespace std;

int main(){

/*
    int n;
    cout<< "Enter a Number: ";
    cin >> n;

    for(int row=1; row<= n; row ++){
        for (int s = 1; s <= n-row; s++)
            cout << "  ";
        for(int col = 1; col<= (row*2)-1; col++)
            cout << "* ";
        cout << endl;
    }
*/

/*
    int n;
    cout << "Enter a Number: ";
    cin >> n;

    for(int row=1; row<=n; row++){
        // print space
        for(int col=1; col<=n-row; col++)
            cout << "  ";
        // print 1 to row
        for(int col=1; col<=row; col++)
            cout << col << " ";
        // print row-1 to 1
        for(int col=row-1; col >=1; col--)
            cout << col << " ";
        cout << endl;
    }
*/

/*
    int n;
    cout << "Enter a Number: ";
    cin >> n;

    for(int row=n; row>=1; row--){
        for(int col=1; col<= n-row; col++)
            cout << "  ";
        for (int col=1; col<=(row*2)-1; col++)
            cout << "* ";
        cout << endl;
    } 
*/

/*
    int n;
    cout << "Enter a Number: ";
    cin >> n;

    for(int row=n; row>=1; row--){ // Upper Part
        //Star
        for(int col=1; col<= row; col++)
            cout << "* ";

        // Space
        for(int col=1; col <= (n-row)*2; col++)
            cout << "  ";

        // Star
        for(int col=1; col<=row; col++)
            cout << "* ";
        cout << endl;
    }

    for(int row=1; row<=n; row++){ // Lower Part

        for(int col=1; col<=row; col++)
            cout << "* ";
    
        for(int col=1; col<=(n-row)*2; col++)
            cout << "  ";
    
        for(int col=1; col<=row; col++)
            cout << "* ";

        cout << endl;
    }
*/


/*
    int n;
    cout << "Enter a Number: ";
    cin >> n;

    for(int row=1; row<=n; row++){ // Upper part
        for(int col=1; col<=row; col++)
            cout << "* ";
        for(int col=1; col<=(n-row)*2; col++)
            cout << "  ";
        for(int col=1; col<=row; col++)
            cout << "* ";
        cout << endl;
    }
    for (int row=n-1; row>=1; row--){ // Lower part
        for(int col=1; col<=row; col++)
            cout << "* ";
        for(int col=1; col<=(n-row)*2; col++)
            cout << "  ";
        for(int col=1; col<=row; col++)
            cout << "* ";
        cout << endl;
    }
*/

    int n;
    cout << "Enter A Number: ";
    cin >> n;

    for(int row=1; row<=n; row++){
        for(int col=1; col<=(n-row); col++)
            cout << " ";
        for(int col=1; col<=row; col++)
            cout << "* ";
        cout<<endl;
    }
    for(int row=n; row>=1; row--){
        for(int col=1; col<=(n-row); col++)
            cout << " ";
        for(int col=1; col<=row; col++)
            cout << "* ";
        cout << endl;
    }


}