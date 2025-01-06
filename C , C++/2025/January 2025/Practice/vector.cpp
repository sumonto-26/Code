#include <bits/stdc++.h>
#include <vector> // for VECTOR
#include <numeric>  
using namespace std;

int main() {
    // 1. Creating a vector
    vector<int> vec = {1, 2, 3, 4, 5};

    // 2. size() - Returns the number of elements in the vector
    cout << "Size: " << vec.size() << endl;

    // 3. capacity() - Returns the capacity of the vector
    cout << "Capacity: " << vec.capacity() << endl;

    // 4. push_back() - Adds an element to the end
    vec.push_back(6);
    cout << "After push_back(6): ";
    for (int x : vec) cout << x << " ";
    cout << endl;

    // 5. pop_back() - Removes the last element
    vec.pop_back();
    cout << "After pop_back(): ";
    for (int x : vec) cout << x << " ";
    cout << endl;

    // 6. emplace_back() - Adds an element to the end, similar to push_back, but more efficient
    vec.emplace_back(7);
    cout << "After emplace_back(7): ";
    for (int x : vec) cout << x << " ";
    cout << endl;

    // 7. at() - Accesses an element with bounds checking
    cout << "Element at index 2 (using at): " << vec.at(2) << endl;

    // 8. [] - Accesses an element without bounds checking
    cout << "Element at index 2 (using []): " << vec[2] << endl;

    // 9. front() - Returns the first element
    cout << "Front element: " << vec.front() << endl;

    // 10. back() - Returns the last element
    cout << "Back element: " << vec.back() << endl;

    // 11. erase() - Removes an element at a specific position
    vec.erase(vec.begin() + 1);
    cout << "After erase(): ";
    for (int x : vec) cout << x << " ";
    cout << endl;

    // 12. insert() - Inserts an element at a specific position
    vec.insert(vec.begin() + 1, 10);
    cout << "After insert(10): ";
    for (int x : vec) cout << x << " ";
    cout << endl;

    // 13. clear() - Removes all elements from the vector
    vec.clear();
    cout << "After clear(): ";
    cout << (vec.empty() ? "Empty" : "Not Empty") << endl;

    // 14. empty() - Checks if the vector is empty
    cout << "Is vector empty? " << (vec.empty() ? "Yes" : "No") << endl;

    // 15. begin() - Returns an iterator to the first element
    vec = {1, 2, 3, 4, 5};
    cout << "First element using begin: " << *vec.begin() << endl;

    // 16. end() - Returns an iterator to one past the last element
    cout << "Last element using end: " << *(vec.end() - 1) << endl;

    // 17. rbegin() - Returns a reverse iterator to the last element
    cout << "Last element using rbegin: " << *vec.rbegin() << endl;

    // 18. rend() - Returns a reverse iterator to one before the first element
    cout << "First element using rend: " << *(vec.rend() - 1) << endl;

    // 19. swap() - Swaps two vectors
    vector<int> vec2 = {10, 20, 30};
    vec.swap(vec2);
    // swap(vec2[0], vec2[2]);
    cout << "After swap: ";
    for (int x : vec) cout << x << " ";
    cout << endl;

    // 20. emplace() - Inserts an element at a specific position (in-place construction)
    vec.emplace(vec.begin(), 15);
    cout << "After emplace(15) at the beginning: ";
    for (int x : vec) cout << x << " ";
    cout << endl;

    // 21. count() - Counts the occurrences of an element in the vector
    cout << "Occurrences of 15: " << count(vec.begin(), vec.end(), 15) << endl;

    // 22. sort() - Sorts the vector
    sort(vec.begin(), vec.end());
    cout << "After sort: ";
    for (int x : vec) cout << x << " ";
    cout << endl;

    // 23. reverse() - Reverses the vector
    reverse(vec.begin(), vec.end());
    cout << "After reverse: ";
    for (int x : vec) cout << x << " ";
    cout << endl;

    // 24. find() - Finds the first occurrence of a value
    auto it = find(vec.begin(), vec.end(), 15);
    if (it != vec.end()) {
        cout << "Found 15 at position: " << distance(vec.begin(), it) << endl;
    } else {
        cout << "15 not found" << endl;
    }

    // 25. accumulate() - Accumulates the elements (e.g., sum)
    int sum = accumulate(vec.begin(), vec.end(), 0);
    cout << "Sum: " << sum << endl;

    // 26. min_element() - Finds the minimum element
    cout << "Min element: " << *min_element(vec.begin(), vec.end()) << endl;

    // 27. max_element() - Finds the maximum element
    cout << "Max element: " << *max_element(vec.begin(), vec.end()) << endl;

    // 28. resize() - Changes the size of the vector
    vec.resize(7, 0);
    cout << "After resize(7, 0): ";
    for (int x : vec) cout << x << " ";
    cout << endl;

    // 29. assign() - Assigns new values to the vector
    vec.assign(5, 2);
    cout << "After assign(5, 2): ";
    for (int x : vec) cout << x << " ";
    cout << endl;

    // 30. unique() - Removes consecutive duplicate elements
    vec = {1, 1, 2, 2, 3, 3};
    vec.erase(unique(vec.begin(), vec.end()), vec.end());
    cout << "After unique(): ";
    for (int x : vec) cout << x << " ";
    cout << endl;

    // 31. lower_bound() - Finds the first element not less than the given value
    vec = {1, 2, 3, 4, 5, 6};
    auto lb = lower_bound(vec.begin(), vec.end(), 4);
    cout << "Lower bound for 4: " << *lb << endl;

    // 32. upper_bound() - Finds the first element greater than the given value
    auto ub = upper_bound(vec.begin(), vec.end(), 4);
    cout << "Upper bound for 4: " << *ub << endl;

    // 33. is_sorted() - Checks if the vector is sorted
    cout << "Is the vector sorted? " << (is_sorted(vec.begin(), vec.end()) ? "Yes" : "No") << endl;

    // 34. next_permutation() - Generates the next lexicographical permutation
    next_permutation(vec.begin(), vec.end());
    cout << "After next_permutation: ";
    for (int x : vec) cout << x << " ";
    cout << endl;

    // 35. prev_permutation() - Generates the previous lexicographical permutation
    prev_permutation(vec.begin(), vec.end());
    cout << "After prev_permutation: ";
    for (int x : vec) cout << x << " ";
    cout << endl;

    // 36. partial_sum() - Computes the partial sum of elements
    vector<int> partialSum(vec.size());
    partial_sum(vec.begin(), vec.end(), partialSum.begin());
    cout << "Partial sum: ";
    for (int x : partialSum) cout << x << " ";
    cout << endl;

    // 37. nth_element() - Partially sorts the vector such that the nth element is in place
    nth_element(vec.begin(), vec.begin() + 2, vec.end());
    cout << "After nth_element (2nd element): ";
    for (int x : vec) cout << x << " ";
    cout << endl;

    // 38. inner_product() - Computes the dot product of two vectors
    vector<int> vec3 = {1, 1, 1, 1, 1};
    int product = inner_product(vec.begin(), vec.end(), vec3.begin(), 0);
    cout << "Dot product: " << product << endl;

    // 39. iota() - Fills the vector with sequentially increasing values
    iota(vec.begin(), vec.end(), 1);
    cout << "After iota(): ";
    for (int x : vec) cout << x << " ";
    cout << endl;

    // 40. all_of() - Checks if all elements satisfy a condition
    cout << "All elements > 0? " << (all_of(vec.begin(), vec.end(), [](int x) { return x > 0; }) ? "Yes" : "No") << endl;

    // 41. any_of() - Checks if any element satisfies a condition
    cout << "Any element > 5? " << (any_of(vec.begin(), vec.end(), [](int x) { return x > 5; }) ? "Yes" : "No") << endl;

    return 0;
}