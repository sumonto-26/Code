// DATE ==> 6 January 2025
// AUTHOR ==> SUMONTO
#include<bits/stdc++.h>
#include <set>
using namespace std;

void print_set(set<int> s){
/*  
    // RULE 1 //
    for(auto i: s) {
        cout << i << " ";
    }
*/
    // RULE 2 //
    for (set<int>::iterator it = s.begin(); it != s.end(); ++it) {
        cout << *it << " ";  
    }
    cout << endl;
}

void print_set1(set<int, greater<int> > s){
    for(set<int,greater<int>>::iterator it = s.begin(); it != s.end(); ++it){
        cout << *it << " ";
    }
    cout << endl;
}

int main(){
    set<int> s0;
    set<int> s1 = {10, 20, 30, 40};
    set<int> s2 = {20, 10, 20, 30};  // Results in {10, 20, 30}
    vector<int> v0 = {10, 20, 30, 40};
    set<int> s3(v0.begin(), v0.end());
    
    set<int> s4 = {10, 20, 30};
    set<int> s5(s4);  // s5 = {10, 20, 30}

    set<int> s6 = {10, 20, 30};
    set<int> s7(move(s6));  // s6 becomes empty, s7 = {10, 20, 30}

    set<int> s8;
    s8.insert(10);
    s8.insert(30);
    s8.insert(20);

    set<int> s9;
    s9.emplace(20);
    s9.emplace(10);
    
    // Sets with descending order
    set<int, greater<int>> sg0;
    set<int, greater<int>> sg1 = {10, 20, 30, 40};
    set<int, greater<int>> sg2 = {20, 10, 20, 30};  // Results in {10, 20, 30}
    vector<int> v1 = {10, 20, 30, 40};
    set<int, greater<int>> sg3(v1.begin(), v1.end());
    
    set<int, greater<int>> sg4 = {10, 20, 30};
    set<int, greater<int>> sg5(sg4);  // sg5 = {10, 20, 30}

    set<int, greater<int>> sg6 = {10, 20, 30};
    set<int, greater<int>> sg7(move(sg6));  // sg6 becomes empty, sg7 = {10, 20, 30}

    set<int, greater<int>> sg8;
    sg8.insert(10);
    sg8.insert(30);
    sg8.insert(20);

    set<int, greater<int>> sg9;
    sg9.emplace(20);
    sg9.emplace(10);

    // PRINT ALL SETS
    cout << "s0 ==> "; print_set(s0);
    cout << "sg0 ==> "; print_set1(sg0);
    cout << "s1 ==> "; print_set(s1);
    cout << "sg1 ==> "; print_set1(sg1);
    cout << "s2 ==> "; print_set(s2);
    cout << "sg2 ==> "; print_set1(sg2);
    cout << "s3 ==> "; print_set(s3);
    cout << "sg3 ==> "; print_set1(sg3);
    cout << "s4 ==> "; print_set(s4);
    cout << "sg4 ==> "; print_set1(sg4);
    cout << "s5 ==> "; print_set(s5);
    cout << "sg5 ==> "; print_set1(sg5);
    cout << "s6 ==> "; print_set(s6);
    cout << "sg6 ==> "; print_set1(sg6);
    cout << "s7 ==> "; print_set(s7);
    cout << "sg7 ==> "; print_set1(sg7);
    cout << "s8 ==> "; print_set(s8);
    cout << "sg8 ==> "; print_set1(sg8);
    cout << "s9 ==> "; print_set(s9);
    cout << "sg9 ==> "; print_set1(sg9);

    // 1. Initialization
    set<int> s = {10, 20, 30, 40, 50};
    cout << "Original set: ";
    print_set(s);

    // 2. Inserting elements
    s.insert(25);  // Insert
    s.emplace(35); // Emplace
    cout << "After insert and emplace: ";
    print_set(s);

    // 3. Erasing elements
    s.erase(30); // Erase
    cout << "After erasing 30: ";
    print_set(s);

    // 4. Find and 5. Count
    if (s.find(40) != s.end()) { // Find
        cout << "40 is present in the set." << endl;
    } else {
        cout << "40 is not in the set." << endl;
    }
    cout << "Count of 25 in the set: " << s.count(25) << endl; // Count

    // 6. Lower Bound and 7. Upper Bound
    auto lb = s.lower_bound(25); // Lower Bound
    auto ub = s.upper_bound(25); // Upper Bound
    if (lb != s.end()) cout << "Lower bound of 25: " << *lb << endl;
    if (ub != s.end()) cout << "Upper bound of 25: " << *ub << endl;

    // 8. Equal Range
    auto range = s.equal_range(25); // Equal Range
    if (range.first != s.end()) cout << "Equal range (lower): " << *range.first << endl;
    if (range.second != s.end()) cout << "Equal range (upper): " << *range.second << endl;

    // 9. Iterators (Reverse Order: rbegin, rend)
    cout << "Set in reverse order: ";
    for (auto it = s.rbegin(); it != s.rend(); ++it) {
        cout << *it << " ";
    }
    cout << endl;

    // 10. Swap
    set<int> another_set = {100, 200, 300};
    s.swap(another_set); // Swap
    cout << "After swapping with another_set: ";
    print_set(s);

    // 11. Size and 12. Empty
    cout << "Set size: " << s.size() << endl; // Size
    cout << "Is set empty? " << (s.empty() ? "Yes" : "No") << endl; // Empty

    // 13. Begin and 14. End
    cout << "First element: " << *s.begin() << endl; // Begin
    cout << "Last element: " << *prev(s.end()) << endl; // End

    // 15. Max Size
    cout << "Max size the set can hold: " << s.max_size() << endl;

    // 16. Emplace Hint
    s.emplace_hint(s.begin(), 150); // Emplace Hint
    cout << "After emplace_hint: ";
    print_set(s);

    // 17. Operator=
    set<int> assigned_set;
    assigned_set = s; // Operator=
    cout << "Assigned set: ";
    print_set(assigned_set);

    // 18. Clear
    s.clear();
    cout << "Set after clear: ";
    print_set(s);
    cout << "Is set empty after clear? " << (s.empty() ? "Yes" : "No") << endl;

    // 19. Get Allocator
    auto alloc = assigned_set.get_allocator(); // Get Allocator
    int* ptr = alloc.allocate(3); // Allocate memory for 3 integers
    ptr[0] = 400;
    ptr[1] = 500;
    ptr[2] = 600;
    cout << "Allocated values: " << ptr[0] << ", " << ptr[1] << ", " << ptr[2] << endl;
    alloc.deallocate(ptr, 3); // Deallocate memory

    return 0;
}