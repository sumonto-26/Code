#include <iostream>
#include <vector>
#include <algorithm> 

using namespace std;

int main() {
    int N;
    cin >> N;
    vector<int> v(N);

    for(int i = 0; i < N; ++i) {
        cin >> v[i];
    }

    vector<int> copy_v = v;
    sort(copy_v.begin(), copy_v.end()); 

    for (int i = 0; i < N; ++i) {
        auto it = upper_bound(copy_v.begin(), copy_v.end(), v[i]);
        if (it != copy_v.end()) {
            v[i] = *it;
        }
    }

    for (int i = 0; i < N; ++i) {
        cout << v[i] << " ";
    }
    cout << endl;

    return 0;
}
