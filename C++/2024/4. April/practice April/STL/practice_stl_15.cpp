// Date ==> 29 April 2024
// Topic ==> Upper Bound and Lower Bound in C++ STL
// Youtube Video Link ==> https://www.youtube.com/watch?v=Cg7SI0WtmXY&t=508s&ab_channel=Luv

#include <bits/stdc++.h>
using namespace std;
int main(){
    int n;
    cin >> n;
    int arr[n];
    for (int i=0; i<n; ++i){
        cin >> arr[i];
    }


    for(int i=0; i<n; ++i){
        cout << arr[i] << " ";
    }



    return 0;
}