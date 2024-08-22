// DATE ==> 21 AUGUST 2024
// PROBLEM NAME ==> A. Password Check
// PROBLEM RATING ==> 800
// PROBLEM TAGS ==> *special problem,  implementation
// AUTHOR ==> SUMONTO

#include <bits/stdc++.h>
using namespace std;


void solve(string password){
    if(password.size()<5){
        cout << "Too weak";
        return;
    }
    else{
        bool is_large = 0, is_small = 0, is_digit=0; 
        for(int i=0; i<=password.size(); i++){
            if (isupper(password[i])) is_large = 1;
            if (islower(password[i])) is_small = 1;
            if (isdigit(password[i])) is_digit = 1;
        }
        if(is_large && is_small && is_digit)
            cout << "Correct";
        else cout << "Too weak";
    }
}

int main(){
    string password;
    cin >> password;
    solve(password);
    cout << endl;

    return 0;
}