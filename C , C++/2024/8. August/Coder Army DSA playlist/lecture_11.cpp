// DATE ==> 6 August 2024

#include <iostream>
using namespace std;
int main(){
/*
    int n;
    cout << "Enter a Number: ";
    cin >> n;

    int i = 1; // initialize
    while (i<=n) // break
    {
        cout << i << " "; // code
        i++; // update
    };
*/

/*
    int n;
    cout << "Enter a Number: ";
    cin >> n;
    int i = 1;
    while (i<=10)
    {
        cout << i*n << endl;
        i++;
    }
*/

/*
    int n;
    cout << "Enter a Number: ";
    cin >> n;

    int i=1;
    while(i<=n){
        if (n % i == 0)
            cout << i<< " ";
        i++; 
}
*/

// DO WHILE LOOP

/*
    int n;
    cout << "Enter a Number: ";
    cin >> n;

    int i = 1; // Initialize 
    do{
        cout << i << endl; // code
        i++; // update
    } while (i<=n); // break
    
*/

/*
    int n;
    cout << "Enter a Number: ";
    cin >> n;

    int i = 1; 
    do{
        cout << i*n << endl;
        i++;
    } while (i <= 10);
*/

/*
    int n;
    cout << "Enter a Number: ";
    cin >> n;
    
    int i = 1 ;
    do{
        if(n % i == 0)
        cout << i << "  ";
        i++;
    } while (i<=n) ;
*/
    // Break
    /*
    int i = 1;
    while (i<=10)
    {
        if (i==6) break;
        cout << i << endl;
        i++;
    }
    */
    
    // Continue
    /*
    int n;
    cout << "Enter a Number: ";
    cin >> n;

    int i = 0;
    do
    {
        i++;
        if (i%5 != 0 ) 
        continue;
        cout << i << endl;
    } while (i<=n);
    */

    // Switch Statement
    int day ;
    cout << "Enter a Number: ";
    cin >> day;

    switch (day){
    case 1:
        cout << "Monday" << endl;
        break;
    case 2:
        cout << "Tuesday" << endl;
        break;
    case 3:
        cout << "Wednesday" << endl;
        break;
    case 4:
        cout << "Tuesday" << endl;
        break;
    case 5:
        cout << "Friday" << endl;
        break;
    case 6:
        cout << "Saturday" << endl;
        break;

    default:
        cout << "Sunday"<<endl;
        break;
    }
    


    return 0;
};