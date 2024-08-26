// DATE ==> 26 AUGUST 2024;
// AUTHOR ==> SUMONTO;
// PROBLEM NAME ==> E. Building an Aquarium;
// PROBLEM RATING ==> 1100;
// PROBLEM TAGS ==> Binary Search, Sortings;

#include <iostream>
#include <vector>
using namespace std;

long long max_element(vector<long long> a){
    long long answer = 0;
    for(int i=0; i<a.size(); i++){
        if (answer < a[i]) answer = a[i];
    }
    return answer;
}

long long find_water(vector<long long> a, long long height){
    long long  ans = 0;
    for(int i=0; i<a.size(); i++){
        if(height-a[i] > 0) ans += height - a[i];
    }
    return ans;
}

int main(){
    int tt;
    cin >> tt;
    while (tt--){
        long long n,x;
        cin >> n >> x;
        vector <long long> a(n);
        for(int i=0; i<n; ++i)
            cin >> a[i];

        // finding height;
        long long answer = -1;
        long long min = 0, max = x + max_element(a);
        while(min <= max){
            long long mid = min + (max-min)/2;
            if(find_water(a,mid) <= x){
                answer = mid;
                min = mid+1;
            }
            else max = mid-1;
        }

        cout << answer<< endl;
    }

    return 0;
}