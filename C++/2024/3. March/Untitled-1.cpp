#include <iostream> // input output stream
#include <cmath> 
#include <iomanip>

using namespace std;

int main() {

    /*cout << "hello world" << endl; // print
    cout <<"cout == character out" << endl;
    
    // VARIABLES
    int variable_name = 100;
    double float_num = 9.9999;
    string strings = "a simple string";
    
    // print all variables
    cout << variable_name << endl;
    cout << float_num << endl;
    cout << strings << endl << endl; // Double endl

    // SWAP 2 VARIABLES
    int a = 5, b = 10;
    cout << "Before swapping: a = " << a << ", b = " << b << endl;

    // Swap like bucket
    int fahrenheitp;
    fahrenheitp = a;
    a = b;
    b = fahrenheitp;
    cout << "After swapping: a = " << a << ", b = " << b << endl;

    // Constants
    const double pi = 3.1415;
    cout << pi << " pi is const constant " << endl;

    // Mathematical Expressions
    // Mathematical Expressions are almost same in python and c++
    
    double a = 10;
    double b = 10;
    double sum = a + b;
    double modulo = a % b;
    
    cout << "a + b == " << sum << endl;
    cout << "a % b == " << modulo << endl; */

    /*
    int x = 10;
    // x  = x + 1; == x++;
    x  = x + 5;
    // int y = x++;
    int y = ++x;
    cout <<"x == "<< x << " y == "<< y << endl;

    // EXERSIZE SOLUTION BY ME //
    double x = 10;
    double y = 5;
    double z = (x + 10) / (3 * y);
    cout << z << endl ; 



    // User Input
    cout << "Enter a 2 integers: ";
    int a;
    int b;
    cin >> a >> b;

    cout << a << " + " << b  << " = " << a + b;
    

    // EXERSIZE SOLUTION BY ME //
    cout << "Fahrenheit: ";
    double fahrenheit;
    cin >> fahrenheit;
    double celsius = (fahrenheit - 32)* 1.8 ;
    cout <<fahrenheit<<" Fahrenheit == "<< celsius<< " Celsius"<< endl;

    cout <<"enter radius: ";
    double radius;
    cin >> radius;
    const double pi = 3.14;
    double area = pi * pow (radius, 2);
    cout << area << endl;


    // IF ELSE_IF ELSE //
    cout <<"Enter a Number: ";
    int number;
    cin >> number;

    if (number > 0){
        cout << "Your Number is Positive.";
    }
    else if (number < 0){
        cout << "Your Number is Nagetive";
    }
    else{
        cout << "Your Number is 0";
    }


    //FOR LOOP//
    cout << "Enter a number: ";
    int n;
    cin >> n;
    
    int sum = 0;

    for (int counter = 1; counter <= n; counter ++){
        sum = sum + counter;
    }
    cout << sum << endl;
    
    
   // WHILE LOOP //
    int n;
    cin >> n;

    while (n>0){
        cout<<n<<endl;
        n--;
    }

    

   // DO WHILE LOOP //
    int n;
    cin >> n;

    do {
        cout << n <<endl;
        n--;
    } while(n>0);
    */

    double x;
    cin >> x;

    double ans = 3.14159 * (x * x);

    // Set precision to 4 decimal places and use fixed-point notation
    cout << "A=" << fixed << setprecision(4) << ans << endl;




    return 0; 
}