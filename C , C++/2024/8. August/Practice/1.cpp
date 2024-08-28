#include <iostream>
#include <vector>
using namespace std;

void print_vec(vector<int> vec){
    for(auto value: vec){
        cout << value << " ";
    }cout << endl;
}

int main(){
    int n;
    cin >> n;
    vector <int> vec(n);
    for(int i=0; i<n; i++) cin >> vec[i];
    cout << endl;

    for(int i=n-1; i>=0; i--){
        for(int j=i; j<n-1; j++){
            if(vec[j] > vec[j+1]) swap(vec[j], vec[j+1]);
            else break;
        }
    }

    print_vec(vec);



    return 0;
}