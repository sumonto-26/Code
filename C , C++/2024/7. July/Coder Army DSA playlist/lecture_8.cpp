// DATE ==> 29 JULY 2024

#include <iostream>
using namespace std;

int main(){

/*
    int n;
    cout << "Enter a Number: ";
    cin >> n;
    for(int row = 1 ; row <= n ; row++){
        for(int space = 1 ; space <= n-row ; space++)
            cout << "  " ; 
        for (int star = 1 ; star <= row ; star++)
            cout << " *" ;
        
        cout << endl;
    }
*/

/*
    int n = 9;
    for(int row=1; row <=n; row ++){
        // for Spaces
        for(int i=1; i<= n-row; i++)
            cout << "  ";
        // for Numbers
        for (int i=1; i<=row; i++)
            cout << row << " ";
    cout << endl;
    }
*/

/*
    int n;
    cout << "Enter a Number: ";
    cin>>n;
    for(int row = 1; row <= n;  row++){
        // Spaces
        for(int i=1; i<=n-row; i++)
            cout << "  ";
        // Number
        for(int j=1; j<=row; j++)
            cout << j << ' '; 

        cout<<endl;
    }
*/

/*
    int n;
    cout << "Enter a Number: ";
    cin >> n;

    for(int row=1; row <=n; row++){
        // Print space
        for(int s = 1; s <= (n-row); s++)
            cout << "  ";
        // Print Characters
        for (char alpha = 'A'; alpha <= 'A'+(row-1); alpha++)
            cout << alpha << " ";
        cout << endl;
    }
*/

/*
    int n;
    cout<< "Enter A Number: ";
    cin >> n;
    for(int row = 1; row<=n; row++){
        for(int s = 1; s<=(n-row); s++)
            cout << "  ";
        for(int col = row; col>=1; col--)
            cout << col << " ";
        cout << endl;
    }
*/

    int n;
    cout << "Enter A Number: ";
    cin >> n;
    for(int row=1; row<=n; row++){
        for(int s=1; s<=(n-row); s++)
            cout << "  ";
        for(int col=1; col<= (row*2)-1; col ++)
            cout << "* ";
        cout << endl;
    }

};