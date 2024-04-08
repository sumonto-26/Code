#include <iostream>
using namespace std;

int main(){

    //PARTERN 1 // Rectangle Pattern.
    /*
    int rows , cols;
    cin >> rows >> cols;

    for(int i = 1; i <= rows; ++i){
        for (int j = 1; j <= cols; ++j){
            cout<<"* ";
        }
        cout<<endl; // most important.
    }
    */

    //PATTERN 2 // Hollow Rectangle Pattern.
    /*int rows , cols;
    cin >> rows >> cols;

    for(int i = 1; i <= rows; ++i){
        for (int j = 1; j <= cols; ++j){
            if (i == 1 || i == rows || j == 1 || j == cols){
                cout<<"* ";
            }
            else{
                cout <<"  ";
            }

        }

        cout << endl;
    }
    */

    //PATTERN 3 // Inverted Half Pyramid.
    /*
    int n;
    cin >> n;

    for (int i = n; i >= 1; --i){
        for (int j = 1; j<=i; ++j){
            cout << "* ";
        }
        cout << endl;
    }
    */

    //PATTERN 4 // Half Pyramid After 180' Rotation.
    int n;
    cin >> n;

    for (int i = 1; i <= n; i++){
        for (int j = 1; j<=n; j++){
            
            if (j <= n-i){
                cout << "  ";
            }
            else{
                cout << "* ";
            }
        }
        cout << endl;
    }
    

/////////////////// Video complite 14 minutes ////////////

    return 0;
}