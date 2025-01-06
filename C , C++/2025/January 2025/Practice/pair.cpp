// DATE ==> 6 January 2025
// AUTHOR ==> SUMONTO
#include <bits/stdc++.h>
#include <utility>  // for pair;
using namespace std;

void print_pair(pair<auto,auto> p){
    cout << p.first << " " << p.second << endl;
}

int main(){
    pair<int, string> p0;
    p0.first = 99;
    p0.second = "pair";
    cout << "P0 ==> " ;
    print_pair(p0);
  
    pair<int, int> p1 = {1,2};
    cout <<"p1 ==> " ;
    print_pair(p1);

    pair<int, double> p2 = make_pair(7,3.1415926);
    cout <<"p2 ==> ";
    print_pair(p2);
    
    p2.second = 3.1416;
    cout <<"p2 ==> ";
    print_pair(p2);

    pair<int, double> &p3 = p2; // pass by reference
    p2.first = 26;
    cout <<"p3 ==> ";
    print_pair(p3);
    cout << (p3.first<p3.second) << endl;

    pair <string, char> p4("Hello", 'W');
    cout <<"p4 ==> ";
    print_pair(p4); 

    pair <string, char> p5("World", 'H');
    cout <<"p5 ==> ";
    print_pair(p5); 

    p4.swap(p5);

    cout <<"p4 ==> ";
    print_pair(p4); 
    cout <<"p5 ==> ";
    print_pair(p5);
    
    return 0;
} 
