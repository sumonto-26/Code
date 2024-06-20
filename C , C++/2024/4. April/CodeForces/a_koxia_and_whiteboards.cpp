#include <iostream>
#include <algorithm> // For sort

using namespace std;

void print_array(int a[], int size){
    for (int i=0; i<size; ++i){
        cout << a[i] << " ";
    }
    cout << endl;
}

int main(){
    int N;
    cin >> N;
    while(N--){
        int n, m;
        cin >> n >> m;
        
        int a[n];
        for (int i = 0; i < n; ++i){
            cin >> a[i];
        }

        int b[m];
        for (int j = 0; j < m; ++j){
            cin >> b[j];
        }

        // Sort array 'a'
        sort(a, a + n);

        // Sort array 'b' in descending order
        sort(b, b + m, greater<int>());

        // Replace the first 'm' elements of array 'a' with elements from array 'b'
        for (int i = 0; i < m; ++i){
            a[i] = b[i];
        }

        // print_array(a, n);

        unsigned long long sum = 0;
        for (int i=0; i<n; ++i){
            sum += a[i];
        }
        cout << sum << endl;
    }

    return 0;
    
    // not compelite // not compelite // not compelite // not compelite // 
    // not compelite // not compelite // not compelite // not compelite // 
    // not compelite // not compelite // not compelite // not compelite // 
    // not compelite // not compelite // not compelite // not compelite // 
    // not compelite // not compelite // not compelite // not compelite // 
    // not compelite // not compelite // not compelite // not compelite // 
    // not compelite // not compelite // not compelite // not compelite // 
}
