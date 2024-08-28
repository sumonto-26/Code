// DATE ==> 28 AUGUST 2024
// PROBLEM NAME ==>  B. Different Divisors
// PROBLEM RATING ==> 1000
// PROBLEM TAGS ==> Binary search, Constructive algorithms, Greedy, Math, Number Theory.
// AUTHOR ==> SUMONTO

#include <iostream>
#include <vector>
using namespace std;

bool isPrime(int num){
    if (num < 2) return false;
    for(int i = 2; i*i<=num; i++){
        if (num%i == 0) return false;
    }
    return true;
}

int main(){
    int test_case;
    cin >> test_case;
    while(test_case){
        int d;
        cin >> d;
        
        int a,b;
        for(int i = d+1; i <= d+100; i++){
            if (isPrime(i)){
                a = i;
                break;
            }
        }
        for(int i = a+d; i <= a+d+100; i++){
            if (isPrime(i)){
                b = i;
                break;
            }
        }
        cout << a*b << endl;

        test_case--;
    }

    return 0;
}