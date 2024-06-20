//Youtube video link == https:
//www.youtube.com/watch?v=xiXMmOSDX3U&list=PLauivoElc3gh3RCiQA82MDI-gJfXQQVnn&index=5&ab_channel=Luv

// Topic ==  Iterators Code in Short in C++ STL 
// Learn "auto" in c++ STL. it is very crusial.

#include <bits/stdc++.h>
using namespace std;

int main(){
    vector <int> v = {2,3,5,6,7};
    
    for(int i=0; i< v.size(); ++i){  // rule number 1;
        cout << v[i] << " "; 
    }
    cout << endl;

    vector<int> :: iterator it;
    for(it = v.begin(); it != v.end(); ++it){ // rule number 2;
        cout << (*it) << " "; 
    }
    cout << endl;


    for(auto it = v.begin(); it != v.end(); ++it){ // rule number 2;
        cout << (*it) << " "; 
    }
    cout << endl;
    
    /*for(int value : v){ // rule number 3
        cout << value << " ";
    }
    // for (int value : v){ // Copy verdion;
    for (int &value : v){ //Real value;
        value ++; // We chnage our real value;
        cout << value << " ";
    }
    cout << endl;

    for (int value : v){
        cout << value << " ";
    }
    cout << endl;*/
    vector<pair<int,int>> v_p = {{1,2},{2,3},{3,4},{4,5}};
    for (pair<int,int> &value : v_p){
        cout << value.first << " " << value.second<< endl;
    }


    auto a = 1.0;
    cout << a << endl;

    return 0;
}