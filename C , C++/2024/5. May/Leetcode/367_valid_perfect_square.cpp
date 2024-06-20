#include <bits/stdc++.h>
using namespace std;
// Other's code.
int main(){
    int num;
    cin >> num;
    if(num==1){cout << "true" << endl;}
    if(num<4){cout << "false" << endl;}
    if(num==4){cout << "true" << endl;}
    int low=0,high=num/2-1;
    int mid;
    while(low<=high){
        mid=low+(high-low)/2;
        long long x = (long long)mid * mid;
        if(x==num){cout << "true" << endl;}
        if(x>num){high=mid-1;}
        else{low=mid+1;}
    }
    cout << "false" << endl;;

    return 0;
}