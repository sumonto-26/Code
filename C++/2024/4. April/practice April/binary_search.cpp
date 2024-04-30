#include <bits/stdc++.h>
using namespace std;

void binary_seach(vector<int> vec, int F){
    sort(vec.begin(), vec.end());
    
    int start = 0;
    int finish = vec.size()-1;

    while (start < finish){
        int mid = (start+finish)/2;
        
        if (F == vec[start]){
            cout << start << endl;
            break;
        }
        if (F == vec[finish]){
            cout << finish << endl;
            break;
        }

        if (F < vec[mid]){
            finish = mid-1 ;
        }
        else if( F > vec[mid]){
            start = mid+1 ;
        }
        if(F == vec[mid]){
            cout << mid << endl;
            break;
        }
    }
    
}

int main(){
    vector <int> v = {10, 20, 52, 65, 70, 80, 100, 101}; // vector must be sorted.
    
    int F;
    cin >> F;
    binary_seach(v, F) ;

}