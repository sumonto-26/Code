// DATE ==> 7 AUGUST 2024
// Topic ==> Binary To Decimal || Decimal To Binary || Decimal To Octal || Binary To Octal Conversion

#include <iostream>
using namespace std;
int main(){

    // DECIMAL TO BINARY
/*
    int num;
    cout << "Enter a Decimal Number: ";
    cin >> num;
    
    int remainder, answer=0, multiplie=1;
    while(num > 0){
        remainder = num&1;
        num >>= 1;
        answer += remainder*multiplie;
        multiplie *= 10;
    }
    cout << "Binary is ==> " << answer << endl;
*/

    // BINARY TO DECIMAL 
/*
    int bin;
    cout << "Enter a Binary Number: ";
    cin >> bin;

    int multi=1, number, decimal=0;
    while (bin != 0){
        number = bin%10;
        bin /= 10;
        decimal += multi*number;
        multi *= 2;
    }
    cout <<"Decimal is "<< decimal << endl;
*/

    // Write a program to convert binary numbers to decimal numbers using a for loop.
    /*
    long long binary_num;
    cout << "Enter a Binary Number: ";
    cin >> binary_num;

    int rem, answer=0, mul=1;
    for(; binary_num>0; binary_num/=10){
        rem = binary_num%10;
        answer += rem*mul;
        mul *= 2;
    }
    cout << "Decimal is "<< answer << endl;
    */


    // Write a program to convert decimal numbers to binary numbers using a for loop.
    /*
    int num;
    cout << "Enter a Decimal Number: ";
    cin >> num;

    int ans=0,rem,mul=1;
    for(;num>0; num/=2){
        rem = num&1;
        ans += rem*mul;
        mul *= 10;
    }
    cout << "Binary Number is: " << ans << endl;
    */

    // Write a program to convert decimal numbers to Octal numbers.
    /*
    int num;
    cout << "Enter a Decimal Number: ";
    cin >> num;

    int rem, ans=0, mul=1;
    for(;num>0; num/=8){
        rem = num%8;
        ans += rem*mul;
        mul *= 10;
    }
    cout << "Octal Number is: " << ans << endl;
    */

    // Write a program to convert Octal numbers to decimal numbers.
    /*
    long long octal_num;
    cout << "Enter a Octal Number: ";
    cin >> octal_num;

    int rem, ans=0, mul=1;
    for(; octal_num>0; octal_num/=10){
        rem = octal_num%10;
        ans += rem*mul;
        mul *= 8;
    }
    cout << "Decimal is "<< ans << endl;
    */

    // Write a program to convert binary to Octal numbers
    /*
    int binary_num;
    cout << "Enter a Binary Number: ";
    cin >> binary_num;

    // binary to decimal
    int rem, decimal_num=0, mul=1;
    while (binary_num > 0){
        rem = binary_num%10; // Last digit
        binary_num /= 10; // remove the last digit
        decimal_num += rem*mul; // decimal += (2 to the power i)*rem
        mul *= 2;
    }
    // decimal to octal
    int remainder, octal_num=0, multiplie=1;
    for(;decimal_num>0; decimal_num/=8){
        remainder = decimal_num%8;
        octal_num += remainder*multiplie;
        multiplie *= 10;
    }
    cout << "Octal Number is: " << octal_num << endl;
    */

    // Write a program to convert Octal numbers to binary numbers
    long long octal_num;
    cout << "Enter a Octal Number: ";
    cin >> octal_num;

    int rem, decimal_num=0, mul=1;
    for(; octal_num>0; octal_num/=10){
        rem = octal_num%10;
        decimal_num += rem*mul;
        mul *= 8;
    }
    cout << "Decimal is "<< decimal_num << endl;

    int remainder, binary_num=0, multiplie=1;
    for (; decimal_num>0; decimal_num/=2){
        remainder = decimal_num&1;
        binary_num += remainder * multiplie;
        multiplie *= 10;
    } 
    cout << "Binary is "<< binary_num << endl;

    return 0;
} 