// Topic ==> LIST IN STL
/*
#include <bits/stdc++.h>
using namespace std;

void print_list(list<int> lis){
    for (auto value: lis){
        cout<< value << " ";
    }
    cout << endl;
}

int main(){
    list <int> l;

    l.push_back(1);
    l.push_back(3);
    l.push_back(2);
    l.push_front(0);

    cout << "Front element of List " << l.front() << endl;
    cout << "Back element of List " << l.back() << endl;
    cout << "Size of the List is " << l.size() <<endl;
    print_list(l);
    
    l.pop_back();
    l.pop_front();

    cout << "Size of the List is " << l.size() <<endl;
    print_list(l);
    
    
    return 0;
}
*/

// TOPIC ==> SET IN STL
/*
#include <bits/stdc++.h>
using namespace std;

// Only Unique value will be stored
// Store value in sorted order (ascending) incresing order
// Insertion, deletion, and search operations have LOGarithmic time
// (O(log n)), making then fast for most use cases.
// Generally Implemented using Red-black Tree
// We can sort it in desending Order also using greater<type> keyword.

int main (){
    // set <int> s; // Ascending Ordered Sorted
    multiset<int, greater<int> > s; // Descending Ordered Sorted
    
    // insert 
    s.insert(10);
    s.insert(10);
    s.insert(20);
    s.insert(400);
    s.insert(49);
    s.insert(491);
    s.insert(192);

    // Search the element
    // find
    
    if (s.find(400) != s.end()){
        cout << "Present the 400 in the set" << endl;
    }
    else{
        cout << "Absent" << endl;
    }
    
    
    // count
    
    if (s.count(400)){
        cout << "Present 400" << endl;
    }
    else{
        cout << "Absent" << endl;
    }
    cout << s.count(291) << endl;
    cout << s.count(491) << endl;
    

    // delete
    s.erase(1);
    s.erase(10);

    // Print the set
    for (auto it = s.begin(); it != s.end(); it ++){
        cout << *it << " ";
    } cout << endl;


    return 0;
}
*/

// TOPIC ==> UNORDERED_SET IN STL
/*
#include <bits/stdc++.h>
using namespace std;

int main(){
    // It store Uniqe elemets.
    // It stored data in Unordered Way
    // Seach , insert , delete in O(1).
    // Implemnted by Hashing.
    unordered_multiset<int> s;
    s.insert(10);
    s.insert(20);
    s.insert(30);
    s.insert(15);
    s.insert(11);
    s.insert(10);

    for(auto it = s.begin(); it != s.end(); it++){
        cout << *it << " ";
    }

// set , multiset, unordered_set, unordered_multiset
// set: Unique elements, sorted
// multiset: sorted
// Unordered_set: Unique
// Unordered_multiset: 


    return 0;
}
*/

// TOPIC ==> MAP
/*
#include <bits/stdc++.h>
using namespace std;

// It store data in key-value pair.
// Key should be Unique but value is not Unique.
// It uses Red-black Tree or AVL Tree for implementation.
// Insertion, deletion, and search operations have O(Log(n)) Time complexity
// Map is sort in key base in Ascending Order.


int main(){
    
    // map create
    map<int,int>m;
    m.insert(make_pair(20,30));
    m.insert(make_pair(30,310));
    m.insert(make_pair(40,230));
    m.insert(make_pair(50,30));
    m.insert(make_pair(20,230)); // this line don't change any thing 
    m[20] = 100; // this line updates m[20]
    m[100] = 60;



    cout << endl;
    // cout << m[200] << endl; // 200 is not in map
    if(m.count(200))
    cout<<m[20]<<" " << endl;

    m.erase(20); // delete operation.

    for (auto it = m.begin(); it != m.end(); it++){
        cout << it->first<<" "<< it->second << endl;
    }

    return 0;
}
*/

// TOPIC ==> MULTI_MAP 
/*
#include <bits/stdc++.h>
using namespace std;

int main(){
    // multimap create
    multimap<int,int>m;
    m.insert(make_pair(20,30));
    m.insert(make_pair(30,310));
    m.insert(make_pair(40,230));
    m.insert(make_pair(50,30));
    m.insert(make_pair(20,230)); 
    // m[20] = 100; // this line don't allow
    // m[100] = 60;

    for (auto it = m.begin(); it != m.end(); it++){
        cout << it->first<<" "<< it->second << endl;
    }

    return 0;
}
*/

// TOPIC ==> UNORDERED_MAP
/*
#include <bits/stdc++.h>
using namespace std;

// Unique keys are present, duplicate keys are not allowed 
// Not neccessary it should be in sorted form 
// Hashing 
// Insert, search, delete O(1) time complexity

int main(){
    // unordered_map create
    unordered_map<int,int>m;
    m.insert(make_pair(20,30));
    m.insert(make_pair(30,310));
    m.insert(make_pair(40,230));
    m.insert(make_pair(50,30));
    m.insert(make_pair(20,230)); // this line don't change anyting
    m[20] = 100;
    m[100] = 60;

    for (auto it = m.begin(); it != m.end(); it++){
        cout << it->first<<" "<< it->second << endl;
    }

    return 0;
} 
*/

// TOPIC ==> Unordered_multimap.
#include <bits/stdc++.h>
using namespace std;

int main(){
    // unordered_multimap create
    unordered_multimap<int,int>m;
    m.insert(make_pair(20,50));
    m.insert(make_pair(20,20));
    m.insert(make_pair(20,30));
    m.insert(make_pair(35,310));
    m.insert(make_pair(40,230));
    m.insert(make_pair(50,30));
    m.insert(make_pair(20,230)); 
    // m[20] = 100; // this line don't allow
    // m[100] = 60;

    for (auto it = m.begin(); it != m.end(); it++){
        cout << it->first << " " << it->second << endl; 
    }


    return 0;
}