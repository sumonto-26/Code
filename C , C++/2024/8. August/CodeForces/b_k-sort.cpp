// DATE ==> 19 AUGUST 2024
// PROBLEM NAME ==> B. K-Sort
// PROBLEM RATING ==> 1000
// AUTHOR ==> SUMONTO

#include <iostream>
#include <vector>
using namespace std;

long long Solve(vector<long long>& vec) {
    long long answer = 0;  
    long long max_diff = 0;
    for (int i = 1; i < vec.size(); ++i) {
        if (vec[i-1] > vec[i]) {
            long long diff = vec[i-1] - vec[i];
            answer += diff;
            if (max_diff < diff) max_diff = diff;
            vec[i] = vec[i-1]; 
        }
    }
    return answer + max_diff;
}

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        vector<long long> vec(n); // Reserve space for n elements
        for (int i = 0; i < n; i++) {
            cin >> vec[i];
        }
        cout << Solve(vec) << endl;
    }
    return 0;
}
