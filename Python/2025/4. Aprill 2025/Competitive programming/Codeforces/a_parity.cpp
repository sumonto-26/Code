#include <bits/stdc++.h>
using namespace std;
int main(){
    int b,k;
    cin >> b >> k;
    vector<int> arr;

    int sum = 0; 
    for(int i=0; i<k; i++){
        int ele; cin >> ele;
        sum += ele%2;
        arr.push_back(ele);
    }
    int last = arr[k-1];
    if(b%2 == 1){
        if(sum%2 == 0) cout << "even" << endl;
        else cout << "odd" << endl;
    }
    else{
        if(last%2 == 0) cout << "even" << endl;
        else cout << "odd" << endl;
    }
    
    return 0;
}