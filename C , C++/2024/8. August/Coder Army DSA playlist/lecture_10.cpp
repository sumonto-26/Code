// Date ==> 30 JULY 2024

#include <iostream>
using namespace std;

int main(){
/*
    // PRESIDENT     Output the DATE TYPE that size is the Greatest size.
    cout << 105/2 << endl;
    cout << 105.0/2 << endl << endl;
*/

/*
    // BINARY ARITHMETIC OPERATORS
    int a = 2;

    // Addition(+)
    a = a + 2;
    cout << "2+2 = " << a << endl;

    // Subtraction(+)
    a = a - 2;
    cout << "4-2 = " << a << endl;

    // Multiplication(*)
    a = a * 10;
    cout << "2*10 = " << a << endl;

    // Dicision(/)
    a = a / 3;
    cout << "20/3 = " << a << endl; 

    // Modulus(%)
    a = a % 4;
    cout << "6&4 = " << a << endl;
*/


/* // UNARY OPERATORS

    // Post increment
    int n = 10;
    cout << n++ << endl;
    cout << n << endl;

    int a = 5;
    int b = a++;
    cout << a << endl << b << endl << endl;


    // Pre increment
    int n1 = 10;
    cout << ++n1 << endl;
    cout << n1 << endl;  

    int a1 = 5;
    int b1 = ++a1;
    cout << a1 << endl << b1 << endl << endl;


    // Post decrement
    int n = 10;
    cout << n-- << endl;
    cout << n << endl;

    int a = 5;
    int b = a--;
    cout << a << endl << b << endl << endl;


    // Pre decrement
    int n1 = 10;
    cout << --n1 << endl;
    cout << n1 << endl;  

    int a1 = 5;
    int b1 = --a1;
    cout << a1 << endl << b1 << endl << endl;
*/

/*
    // Comparison Operator
    int a,b;
    cout << "Enter the A: ";
    cin >> a;
    cout << "Enter the B: ";
    cin >> b;

    // ==
    if (a==b)
    cout << "A == B" << endl;
    else cout << "A == B is False" << endl;

    // !=
    if (a!=b)
    cout << "A != B" << endl;
    else cout << "A != B is False" << endl;

    // > 
    if (a>b)
    cout << "A > B" << endl;
    else cout << "A > B is False" << endl;

    // <
    if (a<b)
    cout << "A < B" << endl;
    else cout << "A < B is False" << endl;

    // <= 
    if (a<=b)
    cout << "A <= B" << endl;
    else cout << "A <= B is False" << endl;

    // >=
    if (a>=b)
    cout << "A >= B" << endl;
    else cout << "A >= B is False" << endl;
*/

// LOGICAL OPERATORS
/*
// AND (&&)
int a,b,c;
cout << "Enter 3 Numbers: ";
cin >> a >> b >> c;
if (a>b && a>c) cout << "First Number is big" << endl;
else if (b>a && b>c) cout << "Second Number is big" << endl;
else if (c>a && c>b) cout << "Third Number is big" << endl;
else cout << "3 Numbers are Equal" << endl;

// OR (||)
char name;
cout << "Enter a Character: ";
cin >> name;
if (name == 'a' || name == 'e' || name == 'i' || name == 'o' || name == 'u')
    cout << "Lower Vowel." << endl;
else if (name == 'A' || name == 'E' || name == 'I' || name == 'O' || name == 'U')
    cout << "Upper Vowel." << endl;
else cout << "Not a Vowel";

// NOT (!)
cout << !1992389 <<endl; 
cout << !0 <<endl; // 1   because it is 0
cout << !-1324012 <<endl;
*/

// BITWISE OPERATORS 
/*
    int a,b;
    cout << "a = ";
    cin >> a;
    cout << "b = ";
    cin >> b;

    int and_ = a&b;
    cout << "a & b == " << and_ << endl;

    int or_ = a|b;
    cout << "a | b == " << or_ << endl;

    int xor_ = a^b;
    cout << "a ^ b == " << xor_ << endl;
    
    int not_a = ~a;
    cout << "~a == " << not_a << endl;

    int not_b = ~b;
    cout << "~b == " << not_b << endl;

    int left_shift = a<<b;
    cout << "a << b == " << left_shift << endl;

    int right_shift = a>>b;
    cout << "a >> b == " << right_shift << endl;
*/

// ASSIGNMENT OPERATORS

int a = 10; // Simple Assignment Operator
a += 10; // Add and Assign Operator
a -= 10; // Subtract and Assign Operator
a *= 10; // Multiply and Assign Operator
a /= 10; // Divide and Assign Operator
a %= 10; // Modulas and Assign Operator
a <<= 10; // Bitwise LEFT SHIFT and Assign Operator
a >>= 10; // Bitwise RIGHT SHIFT and Assign Operator
a &= 10; // Bitwise AND and Assign Operator
a ^= 10; // Bitwise XOR and Assign Operator
a |= 10; // Bitwise OR and Assign Operator


}