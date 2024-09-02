// DATE ==> 2 September 2024
// TOPIC ==> Lecture 25: Binary Search Top Interview Problem | Book Allocation | Painter Partition | Ship Package


#include <bits/stdc++.h>
using namespace std;

/* Book Allocation **
Given that there are N books and M students. Also given are the number of pages in each book in ascending order.
The task is to assign books in such a way that the maximum number of pages assigned to a student is minimum, 
with the condition that every student is assigned to read some consecutive books. Print that minimum number of pages.
*/
long long findPages(int N, vector<int> a, int M) {
    // code here
    if(N<M) return -1;
    int start = 0, end = 0, ans = -1, mid;
    for(int i=0; i<N; i++){
        start = max(start,a[i]);
        end += a[i];
    }
    while(start<= end){
        mid = start + (end-start)/2;
        long long page = 0, counter = 1;
        for(int i=0; i<N; i++){
            page += a[i];
            if(page>mid){
                counter++;
                page = a[i];
            } 
        }
        if(counter <= M){
            ans = mid;
            end = mid-1; 
        }
        else start = mid+1;
    }
    return ans;
}

int main(){
    int N, M;
    cin >> N;
    vector<int> a(N);
    for(int i=0; i<N; i++) cin >> a[i];
    cin >> M;

    cout << findPages(N,a,M)<< endl;


}