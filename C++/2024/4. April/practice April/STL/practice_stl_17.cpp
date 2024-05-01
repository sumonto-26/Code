// DATE ==> 1 MAY 2024
// Topic ==> Lambda Functions and All_of, None_of, Any_of.
// Youtube Video Link ==> https://www.youtube.com/watch?v=o-WpVoRgSj4&ab_channel=Luv


#include<bits/stdc++.h>
using namespace std;

bool is_positive(int x){
    return x > 0;
}

int main(){
    // Lambda Function.
    // cout << [](int x){return x+2;}(2) << endl;
    // cout << [](int x, int y){return x+y;}(2, 39) << endl;
    auto sum = [](int x, int y){return x+y;};
    cout << sum(10,3) << endl;


    // all_of
    vector<int> v = {3,2,4,4,5};
    cout << all_of(v.begin(), v.end(), [](int x){return x>0;})  << endl; 
    cout << all_of(v.begin(), v.end(), is_positive) << endl;

    // any_of
    vector <int> ve = {3,-1,-2,-44,-5,-5};
    cout << any_of(v.begin(), v.end(), [](int x){return x > 0;}) << endl;

    // none_of
    vector <int> vec = {3,54,3,-2,3,1};
    cout << none_of(v.begin(), v.end(), [](int x){return x > 0;}) << endl;

    return 0;
}