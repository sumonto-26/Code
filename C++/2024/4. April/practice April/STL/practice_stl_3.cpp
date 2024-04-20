// Youtube Video link == https://www.youtube.com/watch?v=4EDbe3lhHOM&list=PLauivoElc3gh3RCiQA82MDI-gJfXQQVnn&index=4&ab_channel=Luv

#include <bits/stdc++.h>
using namespace std;

int main(){

    vector <int> v = {2,3,5,30,25,4};

    for (int i=0; i < v.size(); ++i){
        cout << v[i]<< " ";
    }
    cout << endl;

    /*vector <int> :: iterator it = v.begin();
    vector <int> :: iterator it2 = v.end();
    // cout << (*(it)) <<endl; // it prints v[0]
    // cout << (*(it2-1)) <<endl; // it prints v[size(v)-1]
    for (it = v.begin(); it != v.end(); ++it ){    // Correct Code .
        cout << (*it) << " ";
    }
    cout << endl;*/
    vector<pair<int,int>> v_p = {{1,2},{2,3},{3,4}};
    vector<pair<int,int>> :: iterator it;
    for (it = v_p.begin(); it != v_p.end(); ++it){
        // cout << (*it).first << " " << (*it).second << endl;
        cout << (it->first) << " " << (it->second) << endl;
    }
    cout << endl;
    for (it = v_p.begin(); it != v_p.end(); ++it){
        cout << (*it).first << " " << (*it).second << endl;    }

    // (*it).first == (it->first) same same but different.


    return 0;
}