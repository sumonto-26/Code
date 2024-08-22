// DATE ==> 21 AUGUST 2024
// PROBLEM NAME ==> M. Minimum LCM 
// PROBLEM RATING ==> 1000
// PROBLEM TAGS ==> math, number theory
// AUTHOR ==> SUMONTO

#include <iostream>
#include <cmath>
using namespace std;

int main(){
    short test_case;
    cin >> test_case;
    while (test_case)
    {
        long long num;
        cin >> num;
        long long n = 1;
        for(long long index = 2; index <= sqrt(num); index ++){
            if (num % index == 0){
                n = max(index, num/index);
                break;
            }
        }
        cout << n << " " << num - n << endl;
        
        test_case --;
    }
    
    return 0;
}