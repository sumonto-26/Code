// DATE ==> 10 AUGUST 2024
// TOPIC ==> Functions in C++ || Pass by Value || Pass by Reference

#include <iostream>
using namespace std;

int Sum (int a, int b){        // Function Declare
    int ans = a+b;           // Fuction Define
    return ans;
    }
int  Mul (int a, int b){
    return a*b;
}
// We generally can't use return any value in a Void Function But
// We use return to break the Function 
void function(int n){
    cout << "No parameter and No arguments Function" << endl;
    if (n % 5 == 0){
        cout << n << " is divisible by 5 " << endl;
        return ; // finish or end the function;
    }
    cout << n << " is Not divisible by 5 " << endl;
}

bool isPrime(int n){
    if (n<2) return 0;
    for(int i=2; i<n; i++){
        if (n%i == 0) return 0;
    }
    return 1;
}

long long Factorial(int n){
    long long ans = 1;
    for(int i=1; i<=n; i++){
        ans *= i;
    }
    return ans;
}

// Default Parameter
int default_parameter_example(int a=10, int b=5){ // Multiple Parameter
    return a*b;
}

void swap_pass_by_value(int a, int b){
    int c = a;
    a = b;
    b = c;
}
void swap_pass_by_reference(int &a, int &b){
    int c = a;
    a = b;
    b = c;
}
void swap_pass_by_reference(float &a, float &b){
    float c = a;
    a = b;
    b = c;
}

int main(){
    // Function to return the some of 2 numebrs

/*
    int a,b;
    cout << "Enter 2 Number beetween 1-20: ";
    cin >> a >> b;
    
    // cout << endl << endl;
    cout << isPrime(a) << endl;
    cout << Factorial(a) << endl;
    cout << isPrime(b) << endl;
    cout << Factorial(b) << endl;
    cout << isPrime(b-a) << endl;
    cout << Factorial(b-a) << endl;
*/
/*
    int n;
    cout << "Enter a Number; ";
    cin >> n;
    function(n);
    cout << default_parameter_example() << endl;
*/

    int a,b;
    cout << "Enter 2 Numbers; ";
    cin >> a >> b;

    swap_pass_by_value(a,b);
    cout << "By Pass by Value " << a << "  " << b << endl;

    swap_pass_by_reference(a,b);
    cout << "By Pass by Reference " << a << "  " << b << endl;

    float c,d;
    cout << "Enter 2 Float Numbers; ";
    cin >> c >> d;

    swap_pass_by_reference(c,d); // Function overloading 
    cout << c << " " << d << endl;

    swap(c,d); // There is a build-in method swap
    cout << c << " " << d << endl;

    return 0;
}