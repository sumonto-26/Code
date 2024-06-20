// Topic Name ==> Blanced bracket.

#include <bits/stdc++.h>
using namespace std;

string is_balanced(string s){
    unordered_map <char,int> symbols_list = {{'[',1}, {'{', 2}, {'(',3}, {']',-1}, {'}',-2}, {')',-3}};
    stack <char> brackets;
    for(auto value: s){
        if(symbols_list[value] > 0){
            brackets.push(value);
        }
        else{
            if(brackets.empty() || symbols_list[value] + symbols_list[brackets.top()] !=0){
                return "NO";
                break;
            }
            brackets.pop();
        }
    }
    if(brackets.empty()){
        return "YES";
    }
    else{
        return "NO";
    }

}

int main(){
    cout << "Enter a integer the number of test case: "<< endl;
    int n;
    cin >> n;
    while(n--){
        string s;
        cin >> s;
        cout << is_balanced(s) << endl;
    }

    return 0;
}