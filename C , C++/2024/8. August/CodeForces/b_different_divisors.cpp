// DATE ==> 22 AUGUST 2024
// PROBLEM NAME ==>  B. Different Divisors
// PROBLEM RATING ==> 1000
// PROBLEM TAGS ==> Binary search, Constructive algorithms, Greedy, Math, Number Theory.
// AUTHOR ==> SUMONTO

#include <iostream>
using namespace std;

int main(){
    int test_case;
    cin >> test_case;
    while(test_case){
        int d;
        cin >> d;
        int answer = (2*(2+d))*4;
        cout << answer << endl;

        test_case--;
    }

    return 0;
}