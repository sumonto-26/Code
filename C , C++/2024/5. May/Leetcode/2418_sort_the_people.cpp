#include <bits/stdc++.h>
using namespace std;

int main(){
    vector<string> names(3);
    vector<int> heights(3);
    for(int i=0; i<3; ++i){
        cin >> names[i];
    }
    for(int j=0; j<3; ++j){
        cin >> heights[j];
    }

    vector<int> sort_heights = heights;
    sort(sort_heights.rbegin(), sort_heights.rbegin());

    vector <int> indexes ;
    for(int i=0; i < heights.size(); ++i){
        auto it = find(heights.begin(), heights.end(), sort_heights[i]);
        indexes.push_back(distance(heights.begin(), it));
    }
    vector <string> answer_vec;
    for (int a=0; a < names.size(); ++a){
        answer_vec.push_back(names[indexes[a]]);
    }
    
    
    for (auto value: answer_vec){
        cout << value<< " ";
    }
        
    }
