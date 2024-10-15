// DATE ==> 7 September 2024
// TOPIC ==> Lecture 27: What is STL || Vector in C++
// LINK ==> https://www.youtube.com/watch?v=-tDAAOYFehc&list=PLQEaRBV9gAFu4ovJ41PywklqI7IyXwr01&index=27&ab_channel=CoderArmy
#include <bits/stdc++.h>
#include <vector>
using namespace std;
int main(){
/*
    // create vector // declare
    vector<int> vec;
    vector<int> vec1(10,1);
    // SIZE and CAPACITY and PUSH_BACK.
    cout << "Size of Vector " << vec.size() << endl;
    cout << "Capacity of Vector " << vec.capacity() << endl;
    vec.push_back(2);
    vec1.push_back(10);
    vec.push_back(3);
    vec1[5] = 5;
    cout << "Size of Vector " << vec.size() << endl;
    cout << "Capacity of Vector " << vec.capacity() << endl;
    cout << "Size of Vector " << vec1.size() << endl;
    cout << "Capacity of Vector " << vec1.capacity() << endl;
    vector<int> vec2 = {1,2,3,4,5}; // some case it give error but our compilar does't give error;

    // POP_BACK and ERASE and INSERT and CLEAR
    vector<int> vnew;
    vnew.push_back(1);
    vnew.push_back(2);
    vnew.push_back(3);
    vnew.push_back(4);
    vnew.push_back(5);
    vnew.pop_back();
    vnew.erase(vnew.begin()+0); // erase vnew[0]
    vnew.erase(vnew.begin()+1);
    vnew.insert(vnew.begin()+1, 10);
    vnew.clear();

    cout << "Size of vnew " << vnew.size() << endl;
    cout << "Capacity of vnew " << vnew.capacity() << endl;
*/

    // FRONT and BACK and SORT and BEGIN and END and RBEGIN and REND
    // and BINARY_SEARCH and FIND

    vector<int> vec3;
    vec3.push_back(10);
    vec3.push_back(2);
    vec3.push_back(7);
    vec3.push_back(4);
    vec3.push_back(12);
    cout << vec3[0] << " and " << vec3.front() << " are equal." << endl;
    cout << vec3[vec3.size()-1] << " and " << vec3.back() << " are equal." << endl;
    
    vector<int> copy_vec3;
    // Copy value of 1 vector to another vector.
    copy_vec3 = vec3;
    cout << vec3.size() << endl;

    sort(vec3.begin(), vec3.end()); // Sort a vector in increasing order;

    // Print vector in different ways;
    for(int i=0; i<vec3.size(); i++){
        cout << vec3[i] << " " ;
    } cout << endl;
    

    sort(vec3.begin(), vec3.end(), greater<int>()); // Sort a vector in decreasing order;
    sort(vec3.rbegin(), vec3.rend()); // Sort a vector in decreasing order;

    // for(int it = vec3.begin(); it != vec3.end(); it++){
    //     cout << *it << " ";
    // } cout << endl; ////////////////// error ////////// 

    for(auto it = vec3.begin(); it != vec3.end(); it++){
        cout << *it << " ";
    } cout << endl;

    for(auto i: copy_vec3){
        cout << i << " ";
    } cout << endl;
    
    for(auto i: vec3){
        cout << i << " ";
    } cout << endl;

    // is present 1 else 0
    cout << binary_search(vec3.begin(), vec3.end(), 5 ) << endl;
    // find the element index;
    cout << find(vec3.begin(), vec3.end(), 7) - vec3.begin() << endl;





    return 0;
}