// DATE ==> 23 April 2024
// AUTHOR ==> SUMONTO.

#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;
    while (N--) {
        string str;
        cin >> str;
        vector<int> v;
        int count = 1; // Start count from 1, because we count the first character as well

        for (int i = 1; i < str.size(); i++) {
            if (str[i] == str[i - 1]) {
                count++;
            } else {
                v.push_back(count); // Store the count in the vector
                count = 1; // Reset count for the next sequence
            }
        }
        v.push_back(count); 
        
        string ans = "YES";

        for (int i=0; i<v.size(); i++){
            if (v[i] < 2){
                ans = "NO";
                break;
            }
        }

        cout << ans << endl;
    }

    return 0;
}
