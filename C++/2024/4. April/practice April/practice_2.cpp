// Topic Name ==> Blanced bracket.

#include <bits/stdc++.h>
using namespace std;

string is_balanced(string s){
    unordered_map <char,int> symbol_list = {{'(',-1}, {'{',-2}, {'[',-3},{')',1}, {'}',2}, {']',3}};
    stack <char> st;
    for (auto &value : s){
        if(symbol_list[value] < 0){
            st.push(value);
        }
        else{
            if (st.empty() || symbol_list[st.top()] + symbol_list[value] != 0){
                return "Not Balanced";
            }
            st.pop();
        }
    }
    if (st.empty()){
        return "Balanced";
    }
    else{
        return "Not Balanced";
    }
}

int main(){
    int n;
    cin >> n;
    while(--n){
        string s;
        cin >> s;
        cout << is_balanced(s) << endl;
    }

    return 0;
}