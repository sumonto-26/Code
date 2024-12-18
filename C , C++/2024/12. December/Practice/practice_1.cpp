// DATE --> 18-19 : December : 2024
#include <bits/stdc++.h>
using namespace std;

// STL

void print_vec(vector<pair<string,int>> vec){
    for (auto value: vec){
        cout << value.first << " " << value.second << endl;
    }
    cout << endl;
}

int main(){
/*
    // PAIR
    pair<int, string> p;
    // p.make_pair(34 , "slkfj");
    p = {10, "tamim"};
    cout<< p.first << " " << p.second << endl;
    p.first = 26;
    p.second = "sumonto";
    cout << p.first << " " << p.second << endl;

    vector<pair<string,int>> vec;
    vec.push_back({"sumonto", 26});
    vec.push_back({"rakib", 34});
    vec.push_back({"ovi", 25});
    vec.push_back({"siam", 16});
    vec.push_back({"niloy", 100});
    vec.push_back({"joy", 6});
    vec[2].first = "Ovi das";
    vec[4].second = 30;

    print_vec(vec);

    vector<int> vec_int;
    int n;
    cin >> n;
    for (int i=0; i<n ; i++){
        int ele; cin >> ele;
        vec_int.push_back(ele);
    }

    for (int i=0; i<vec_int.size(); i++){
        cout << vec_int[i] << " ";
    }
    cout << endl;
*/

    vector<int> vec = {3,2,12,4,5,10};
    vector<pair<int, int>> vec_int = {{1,2}, make_pair(4,3), {1,0} , {4,5}};
    vector<string> bivag = {"Barishal", "Chattogram", "Dhaka", "Khulna", "Rajshahi", "Rangpur", "Mymensingh" , "Sylhet"};
    vector<pair<string, int>> names = {{"Sumonto",26}, make_pair("Saif", 16), {"Nirob", 14}};
    vector<vector<int>> nexted_vec = {{1,2,3}, {4,3,2}, {6,5}, {2,4,3}};

    for (auto value: vec){
        cout << value << " ";
    }
    cout << endl << endl;

    for(auto value: vec_int)  
        cout << value.first << " " << value.second << endl;
    cout << endl;
    
    for(auto value: bivag) cout << value << "  ";
    cout << endl << endl;

    for(auto value: names){
        cout << value.first << " " << value.second << endl;
    }
    cout << endl;

    names.pop_back();
    names[1].first = "Sifat";
    names.push_back(make_pair("Niloy", 17));

    for(auto value: names){
        cout << value.first << " " << value.second << endl;
    }
    cout << endl;

    for(int i=0; i<nexted_vec.size(); i++){
        for(int j=0; j<nexted_vec[i].size(); j++){
            cout << nexted_vec[i][j] << ", ";
        } cout << endl;
    }
    cout << 2*3-4/2 << endl;

    return 0;
}