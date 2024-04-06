#include <iostream>
using namespace std;

int main(){
    int n;
    cin >> n;

    int arr[n];
    int min_arr = 1000000001, max_arr = 0;
    for (int i=0; i<n; i++){
        cin >> arr[i];
        if (arr[i] > max_arr){
            max_arr = arr[i];
        }
        if (arr[i] < min_arr){
            min_arr = arr[i];
        }
    }

    int ans = ((max_arr - min_arr)+1) - n;
    cout << ans;

    return 0;
}