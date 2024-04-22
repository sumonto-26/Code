// Date ==> 22 April 2024
// Topic ==> SET, UNORDERED SET & MULTISET .

#include <bits/stdc++.h>
using namespace std;

void print(set<string> &s){
    for (string value : s){
        cout << value << endl;
    }
    cout << endl;
    // for (auto it = s.begin(); it != s.end(); ++it){
    //     cout << (*it) << endl;
    // }
}

int main(){
    set <string> s;
    s.insert("abc"); // O(log(n))
    s.insert("zslk");
    s.insert("bcd");
    
    auto it = s.find("lkj"); // O(log(n))
    if(it != s.end()){
        // cout << (*it) << endl;
        s.erase(it);
    }
    s.erase("bcd");
    print(s);


    return 0;
}