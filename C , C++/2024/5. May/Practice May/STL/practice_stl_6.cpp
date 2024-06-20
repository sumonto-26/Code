// YouTube Video Link: https://www.youtube.com/watch?v=okLflHtlCuk&list=PLauivoElc3gh3RCiQA82MDI-gJfXQQVnn&index=7&ab_channel=Luv
// Topic: STL Unordered Maps

#include<bits/stdc++.h>
using namespace std;

// Function to print elements of the unordered map
void print_map(unordered_map<int, string> &m) {
    cout << m.size() << endl; // Print size of the map
    for (auto &pr : m) { // Iterate through the map
        cout << pr.first << " " << pr.second << endl; // Print key-value pairs
    }
}


int main() {

    /*unordered_map<int, string> m; // Create an unordered map
    
    // Add elements to the map
    m[5] = "cdc"; // Element with key 5 and value "cdc"
    m[1] = "abc"; // Element with key 1 and value "abc"
    m[7] = "acd"; // Element with key 7 and value "acd"
    m[6]; // Add element with key 6 and empty string value
    m[5] = "Five is changed"; // Update value of key 5
    m.insert({4, "afg"}); // Insert element with key 4 and value "afg"
    m.insert(make_pair(2, "abc")); // Insert element with key 2 and value "abc"

    // Print the map
    print_map(m);*/

    /*
    auto it = m.find(2); // Find element with key 2
    if (it != m.end()){ // Check if element is found
        m.erase(it);   // Erase element if found
    }
    */

    /*
    if (it == m.end()){ // Check if element is not found
        cout << "No value found" << endl; // Print message if element is not found
    }
    else{
        cout << (*it).first << " " << (*it).second << endl; // Print key-value pair if element is found
    }
    */

    // Alternative ways to print the map

    // Method 1: Using iterators
    /*
    for (auto it = m.begin(); it != m.end(); it++) { // Iterate through the map
        cout << (*it).first << " " << (it -> second) << endl; // Print key-value pairs
    }
    */

    // Method 2: Using range-based for loop
    /*
    for (auto pr : m) { // Iterate through the map
        cout << pr.first << " " << pr.second << endl; // Print key-value pairs
    }
    */




    /*
    Given N strings and Q queries.
    In each query you are given a string
    print frequency of that string
    
    N <= 10^6
    |S| <= 100
    Q <= 10 ^ 6
    */

    // ANSWER //
    unordered_map <string, int> m;
    int n;
    cin >> n;
    for (int i=0; i<n; ++i){
        string s;
        cin >> s;
        // m[s] = m[s] + 1;
        m[s]++;
    }
    int q;
    cin >> q;
    while (q--){
        string s;
        cin >> s;
        cout << m[s] << endl;
    }

    return 0;

}

/*
Benefits:

Utilizes unordered map for efficient storage and retrieval of key-value pairs.
Provides a function to print elements of the map for easy debugging and analysis.
Uses modern C++ features like range-based for loop for concise and readable code.
Includes comments to explain the purpose and usage of each section of code.
Troubles:

The commented-out code sections might lead to confusion if uncommented without understanding their purpose.
*/   