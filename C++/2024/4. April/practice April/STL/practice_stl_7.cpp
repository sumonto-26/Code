// Youtube Video Link ==>  https://www.youtube.com/watch?v=7mx2BasNK0w&list=PLauivoElc3gh3RCiQA82MDI-gJfXQQVnn&index=8&ab_channel=Luv
// Date ==> 22 April 2024
// Topic ==> SET, UNORDERED SET & MULTISET .

#include <bits/stdc++.h>
using namespace std;

void print(multiset<string> &s){
    for (string value : s){
        cout << value << endl;
    }
    cout << endl;
    // for (auto it = s.begin(); it != s.end(); ++it){
    //     cout << (*it) << endl;
    // }
}

int main(){
    /*
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
    */

    /*
    Given N strings, print unique strings
    in lexiographical order
    N <= 10^5
    |S| <= 100000
    */
    /*
    set <string> s; // set are already sorted.
    int n;
    cin >> n;
    for (int i=0; i<n; ++i){
        string str;
        cin >> str;
        s.insert (str);
    }
    for (auto value : s){
        cout << value << endl;
    }*/

    /*
    // UNORDERED SET
    unordered_set <string> s;
    s.insert("abc"); // o(1)
    s.insert("sjf");
    s.insert("bcd");
    s.insert("abc");
    auto it = s.find("abc"); // O(1)
    if (it != s.end()){
        s.erase(it);
    }
    s.erase("bcd");
    print(s);
    */

    /*
    given N strings and Q queries.
    In each query you are given a string
    print yes if string is present
    else print no.
    
    n <= 10^6
    |S| <= 100
    Q <= 10^6*/
    /*
    unordered_set <string> s; 
    int n;
    cin >> n;
    for (int i=0; i<n; ++i){
        string str;
        cin >> str;
        s.insert (str);
    }
    int q;
    cin >> q;
    while (q--){
        string str;
        cin >> str;
        if (s.find(str) == s.end()){
            cout << "NO" << endl;
        }
        else{
            cout << "YES" << endl;
        }
    }
    */
    

    // --MULTI SET-- //
    multiset <string> s;
    s.insert("abc"); // o(log(n))
    s.insert("sjf");
    s.insert("bcd");
    s.insert("abc");

    // REMOVE 1 "abc" //
    // auto it = s.find("abc"); // O(log(n)))
    // if (it != s.end()){
    //     s.erase(it);
    // }

    // REMOVE ALL "abc" //
    s.erase("abc");
    print(s);
    

    return 0;
}