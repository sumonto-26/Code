// DATE ==> 28 April 2024
// Topic ==> STACK_PROBLEM "Next Greater Element using stack."
// Video Link ==> https://www.youtube.com/watch?v=T-E3hWEPWWU&t=371s&ab_channel=Luv

#include <bits/stdc++.h>
using namespace std;

vector<int> NGE(vector<int> v){
    vector <int> nge(v.size());
    stack <int> st;
    for (int i=0; i<v.size(); ++i){
        while(!st.empty() && v[i] >v[st.top()]){
            nge[st.top()] = i;
            st.pop();
        }
        st.push(i);
    }
    while(!st.empty()){
        nge[st.top()] = -1;
        st.pop();
    }
    return nge;
}

int main(){

    int n;
    cin >> n;
    vector <int> vec(n);
    for (int i=0; i<n; ++i){
        cin >> vec[i];
    }

    vector<int> nge = NGE(vec);
    for (int i=0; i<n; ++i){
        // cout << vec[i] << " " << (nge[i] == -1 ? -1 : vec[nge[i]]) <<endl;
        cout << (nge[i] == -1 ? -1 : vec[nge[i]]) << " ";
    }

    return 0;
}