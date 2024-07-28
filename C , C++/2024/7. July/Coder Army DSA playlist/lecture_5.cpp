// DATE ==> 28 JULY 2024

#include <iostream>
using namespace std;

int main()
{
    /*
    for (int i=100; i<=200; i++){
        cout<< "i ==" << i << endl;
    }
    */

/*
    for(char c = 'a'; c <= 'z'; c++){
        int ascii_value = c;
        cout<< ascii_value-96 << " == ";
        cout << c << endl;
    }

    for (int i = 10; i>= 1; i--){
        cout << i << endl;
    }
*/

/*
    int num, i;
    cout << "Enter a Number: ";
    cin >> num;

    for (i=num; i>= 1; i--){
        cout << i << endl;
    }
*/

/*
    int n;
    cout << "Enter a Number: ";
    cin >> n;
    for(int i=1; i<=n; i+=3){
        cout << i << endl;
    }
*/


/*
    int n;
    cout << "Enter a Number: ";
    cin >> n;
    for(int i=1; i<n; i++){
        cout << i << endl;
    }
*/

/*
    int n;
    cout << "Enter a Number: ";
    cin >> n;
    for (int i=1 ; i<=10; i++){
        cout << n << " * " << i << " = " << n*i << endl;
    }
*/

/*
    int n;
    cout << "Enter a Number: ";
    cin >> n;
    for (int i=n ; i<= n*10; i += n){
        cout << n << " * " << i/n << " = " << i << endl;
    }
*/

/*
    int n,p;
    cout << "Enter First Number: ";
    cin >> n;
    cout << "Enter Second Number: ";
    cin >> p;

    long long x = 1;
    for (int i=1; i<=p; i++){
        x *= n;
    }
    cout << x << endl;
*/

/*
    int n;
    cout << "Enter a Number: ";
    cin >> n;
    long long sum = 0;
    for (int i=1; i<=n; i++){
        sum += i;
    }
    cout << sum << endl;
    cout << ((n*n)+n)/2;
*/
    
/*
    int n;
    cout << "Enter a Number: ";
    cin >> n;
    long long fac = 1;
    for (int i=2; i<=n; i++){
        fac *= i;
    }
    cout << fac;
*/

/*
    int n;
    cout << "Enter a Number: ";
    cin >> n;
    if (n < 2){
        cout << "Not Prime Number" <<endl;
        return 0;
    }    
    else{
        for (int i=2; i<n; i++){
            if (n % i == 0) {
                cout << "Not Prime Number" <<endl;
                return 0;
            }
        }
        cout << "Prime Number" << endl;

    }
*/

    int n;
    cout << "Enter a Number: ";
    cin >> n;
    
    if (n > 1) {
        long long last= 0, prev = 1;
        for (int i = 2; i<n; i++){
            cout << last<< " " << prev << endl;
            long long curr = last+prev;
            last = prev;
            prev = curr;
        }
        cout << prev << endl;
        }
    else cout << n << endl;

};