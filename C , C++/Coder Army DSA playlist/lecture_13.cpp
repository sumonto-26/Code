// DATE ==> 9 AUGUST 2024;
// TOPIC ==>  Write Your First Program On LeetCode 

#include <iostream>
using namespace std;
int main(){
    // First Leetcode problem:   258:"Add Digit" 
    /*
    int num;
    cout << "Enter a Number: ";
    cin >> num;
    while(num >= 10){ // while it is not a one digit number
        int sum = 0;
        while(num>0){
            // separate all digit
            short last_digit = num%10;
            num /= 10;
            // make a sum of all digit
            sum += last_digit;
        }
        num = sum;
    }
    cout << "The Answer is:  "<< num << endl;
    */

    // First Geeks For Geeks problem  "Leap Year" .
    // Given a number check the year is Leap Year or not.
    /*
    int year;
    cout << "Enter The Year: ";
    cin >> year; 
    if (year%400==0) cout << year << " is a Leap Year." << endl;
    else if (year%4==0 && year%100!=0) cout << year << " is a Leap Year." << endl;
    else cout << year << " is Not a Leap Year." << endl;
    */

    //Leetcode problem 3; 7.Reverse Integer given a number return the reverse of number.
    /*
    int num;
    cout << "Enter a Number: ";
    cin >> num;
    int ans=0;
    while(num!=0){
        short last_digit = num%10;
        num /= 10; // Remove the last Digit
        if(ans>INT32_MAX/10 || ans<INT32_MIN) return 0;// it will INT_MAX and INT_MIN.
        ans = ans*10+last_digit;
        // cout << " ans ==> " << ans << " " << " last digit ==> " << last_digit << endl;
    }
    cout << "Final Number is " << ans;
    */

    // Leetcode problem 3; "231.Power of Two" Given a number n return is it a power of 2.
    /*
    int n;
    cout << "Enter a Number: ";
    cin >> n;
    if (n<1) cout << "Non-positive number are not power of 2" << endl;
    else{
        while(n!=1){
            if (n%2==1) cout << "Not a Power of 2" << endl;
            n /= 2; 
        }
        cout << "The Number is Power of 2";
    }
    */

   // Leetcode Problem 4; "69.(Sqrt(x))"
/*
    int x;
    cout << "Enter a Number: ";
    cin >> x;
    for(long long i=0; i*i<=x; i++){
        if (i*i <= x && (i+1)*(i+1) > x) cout << i << endl;
    }
*/

    // Leetcode Problem 5; "9. Palindrome Number" Given a Number Return is the number is a Palindrome Number or not.
    /*
    int n;
    cout << "Enter a Number: ";
    cin >> n; 
    int reverse_n = 0, copy_n = n;
    while(copy_n){
        short last_digit = copy_n%10;
        copy_n /= 10;
        reverse_n = reverse_n*10+last_digit;
    } 
    if (n == reverse_n) cout << n << " is a Palindrome Number." << endl;
    else cout << n << " is not a Palindrome Number." << endl;
    */

   // Leetcode Problem 6; "1009. Complement of Base 10 Integer"
    int n;
    cout << "Enter a Number: ";
    cin >> n;
    int ans=0, power_of_10 = 1;
    while(n){
        short rem = n%2;
        rem = rem^1; // swap 0 and 1
        n /= 2;
        ans += rem*power_of_10;
        power_of_10 *= 10; 
    } 
    cout << ans << endl;

    return 0;
}
