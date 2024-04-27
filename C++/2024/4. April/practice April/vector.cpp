#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    /*
    // create vector, declare.
    vector <int> v;
    vector <int> v1 (5, 1);

    // Size and Capacity.
    cout << "Size of v " << v.size() << endl;
    cout << "Capacity of v " << v.capacity() << endl;
    v.push_back(1);
    v.push_back(2);
    v.push_back(3);
    cout << "\nSize of v " << v.size() << endl;
    cout << "Capacity of v " << v.capacity() << endl;
    
    // the capacity of v1 is equal to the size of v1 because it is fixed in declareation.
    cout << "\nSize of v1 " << v1.size() << endl;
    cout << "Capacity of v1 " << v1.capacity() << endl;
    v1.push_back(100);
    cout << "\nSize of v1 " << v1.size() << endl;
    cout << "Capacity of v1 " << v1.capacity() << endl;

    // Change value
    v[1] = 5;
    */
/*
    // Delete value from vector.
    vector <int> v_new;

    v_new.push_back(2); 
    v_new.push_back(3); 
    v_new.push_back(1); 
    v_new.push_back(4);
    v_new.push_back(8); 
    v_new.pop_back(); // erase last element.
    cout << "\nSize of V_new " << v_new.size() << endl;
    cout << "Capacity of V_new " << v_new.capacity() << endl;
    

    v_new.erase(v_new.begin()+1); // erase v_new[1]
    cout << "\nSize of V_new " << v_new.size() << endl;
    cout << "Capacity of V_new " << v_new.capacity() << endl;
    
    for(int i=0; i<v_new.size(); ++i){
        cout << v_new[i] << " ";
    }
    cout << endl;

    v_new.insert(v_new.begin()+1, 100000); // insert value;

    for(int i=0; i<v_new.size(); ++i){
        cout << v_new[i] << " ";
    }
    cout<<endl;

    v_new[2] = 123456; // replaceing

    for(int i=0; i<v_new.size(); ++i){
        cout << v_new[i] << " ";
    }
    cout << endl;

    v_new.clear(); // Remove all the element.
    cout<<"\nSize of v_new " << v_new.size() << endl;
    cout<<"Capacity of v_new " << v_new.capacity() << endl;  
*/
/*
    vector <int> vec;
    vec.push_back(3);
    vec.push_back(2);
    vec.push_back(5);
    vec.push_back(1);

    // print the first element of vec.
    cout << vec[0] << endl;
    cout << vec.front() << endl;
    
    // print the last element of vec.
    cout << vec[vec.size()-1] << endl;
    cout << vec.back() << endl;

    // print the vec.
    for(auto it = vec.begin(); it!= vec.end(); it++){
        cout << *it << " "; 
    }
    cout << endl;

    for(auto i: vec){
        cout << i << " ";
    }
*/

    vector <int> ans;
    ans.push_back(5);
    ans.push_back(4);
    ans.push_back(6);
    ans.push_back(2);
    ans.push_back(9);

    // sort in increasing order.
    sort(ans.begin(), ans.end());
    for (int i=0; i<ans.size(); ++i){
        cout << ans[i] << " ";
    }
    cout << endl;
    /*
    //sort in decreasing order.
    sort(ans.rbegin(), ans.rend()); 
    sort(ans.begin(), ans.end(), greater<int>());
    for (int i=0; i<ans.size(); ++i){
        cout << ans[i] << " ";
    }
    */ 

    //search in binary search
    cout << binary_search(ans.begin(), ans.end(), 54) << endl; // 0 == No and 1 == yes

    // find the index.
    cout << find(ans.begin(),ans.end(),5)-ans.begin() << endl;

    return 0;
}