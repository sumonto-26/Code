// DATE ==> 12/AUGUST/2024
// TOPIC ==> SOLVE SOME PROBLEM.

#include <iostream>
#include <cmath>
using namespace std;


char upper(char name){
    return 'A' + (name -'a');
}

int length(int num){
    int p = 0;
    while(num){
        p++;
        num /= 10;
    }
    return p;
}

int min(int a , int b){
    if (a<b) return a;
    return b;
}

int Bishop_moves(int A, int B) {
    int ans = 0;
    ans += min(A,B)-1;
    ans += min(B-1, 8-A);
    ans += min(8-A, 8-B);
    ans += min(A-1, 8-B);
    return ans;
}

bool is_armstrong_number(int n, int length){
    int num = n, rem;
    float ans = 0;
    while(num){
        rem = num%10;
        num /= 10;
        ans += pow(rem,length); // "pow function return answer in floating point number"
    }
    cout << ans << endl;
    return ans == n;
}

int trailingZeroes(int n) {
    int ans = 0;
    while(n){
        n/=5;
        ans += n;
    }
    return ans;
}

int is_rectangle (int A, int B, int C, int D) {
    if((A == B && C == D) || (A == C && B == D) || (A == D && B == C))
        return 1;
    return 0;
}

bool canWinNim(int n) {
    return n%4!=0;
}

// Problem 1, Given a lowercase char print the uppercase of that char.
int main(){
/*
    char alp;
    cout << "Enter a Lowercase alphabet: ";
    cin >> alp;
    cout << upper(alp) <<endl;
*/
    int n;
    cout << "Enter a Number: ";
    cin >> n;
    cout << is_armstrong_number(n, length(n)) << endl;

    int num;
    cout << "Enter a Number: ";
    cin >> num;
    cout << num << "! has " << trailingZeroes(num) << " zeros. " <<endl;


    return 0;
} 