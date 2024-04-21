// Youtube Video Link ==>  https://www.youtube.com/watch?v=gUrfXZ0hqoA&list=PLauivoElc3gh3RCiQA82MDI-gJfXQQVnn&index=6&ab_channel=Luv
// Topics ==> STL Maps.

#include<bits/stdc++.h>
using namespace std;

void print_map(map<int,string> &m){
    cout << m.size() << endl;
    for (auto &pr : m){
        cout << pr.first << " " << pr.second << endl;
    }
}

int main(){

    /*
    map <int, string> m; // Making The Map
    
    // __ADD ELEMENTS ON ARRAY__.
    m[5] = "cdc"; // Rule Number 1.
    m[1] = "abc"; // Enter keys and values.
    m[7] = "acd"; // O(log(n)) n == size
    m[6]; // O(log(n)) // empty string
    m[5] = "Five is changed";
    m.insert({4, "afg"}); // Rule Number 2.
    m.insert(make_pair(2, "abc")); // Rule Number 3.
    
    
    auto it = m.find(2); // O(Log(n))
    if (it != m.end()){ 
        m.erase(it);   // O(Log(n))
    }
    print_map(m);
    */

    /*
    if (it == m.end()){ // if not found the value.
        cout << "No value find " << endl;
    }
    else{
        cout << (*it).first << " " << (*it).second << endl; 
    }*/



    // ---PRINT THE MAP---
    
    // Rule Number 1
    /*map <int,string> :: iterator it;
    for (it = m.begin(); it != m.end(); it++){
        cout << (*it).first << " " << (it -> second) << endl;
    }*/

    // Rule Number 2
    /*for (auto pr : m){
        cout << pr.first << " " << pr.second << endl;
    }*/


    // 1 Problem with Easyly solved by MAP in S++ STL
    /*
    Given N strings, print unique strings 
    in lexiographicnal order with their 
    frequency
    N <= 10^5
    S <= 100
    */

    map <string,int> m;
    int n;
    cin >> n;

    for (int i=0; i<n; ++i){
        string s;
        cin >> s;
        // m[s] = m[s]+1
        m[s]++;
    }

    for (auto pr : m){
        cout << pr.first << " " << pr.second << endl;
    }

    return 0;
    

}