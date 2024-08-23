// DATE ==> 23 AUGUST 2024.
// PROBLEM NAME ==> B. Divisor Subtraction.
// PROBLEM RATING ==> 1200.
// PROBLEM TAGS ==> Implementation, Math, Number Theory.
// AUTHOR ==> SUMONTO.

#include <bits/stdc++.h> 
using namespace std;

bool isPrime(long long n){
    if (n<2) return false;
    long long i;
    for(i=2; i<=sqrt(n); i++){
        if (n%i == 0){return false;}
    }
    return true;
}

int main(){
    long long n;
    cin >> n;
    if (isPrime(n)) cout << 1 << endl;
    else{
        if (n%2 == 0) cout << n/2;
        else{
            vector<int> vec;
            int i;
            for(i=2; i<=sqrt(n); i++){
                if (n%i == 0 && isPrime(i)) {
                    vec.push_back(i);
                    break;}
            }
            cout << 1+(n-vec[0])/2; // +1 for vec[0]
        }
    }

    return 0;
}