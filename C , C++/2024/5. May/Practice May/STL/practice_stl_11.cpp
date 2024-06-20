// DATE ==> 26 April 2024
// YOUTUBE VIDEO LINK ==> https://www.youtube.com/watch?v=q-JB0hYyouo&list=PLauivoElc3gh3RCiQA82MDI-gJfXQQVnn&index=12&ab_channel=Luv
// TOPIC ==> STACK Problem.
// problem link ==> https://www.hackerrank.com/challenges/balanced-brackets/problem


#include <bits/stdc++.h>
using namespace std;

unordered_map<char,int> symbols = {{'[',-1}, {'{',-2}, {'(',-3}, {']',1}, {'}',2}, {')',3}};

string is_balanced(string s){
    stack<char> st;
    for(char brackets : s){
        if (symbols[brackets] < 0){
            st.push(brackets);
        }
        else{
            if (st.empty()) return "NO";
            char top = st.top();
            st.pop();
            if (symbols[top] + symbols[brackets] != 0){
                return "NO";
            }
        }
    }
    if (st.empty()) return "YES";
    return "NO";
}

int main(){
    int N;
    cin >> N;
    while (N--){
        string s;
        cin >> s;
        cout << is_balanced(s) << endl;
    }

    return 0;
}
