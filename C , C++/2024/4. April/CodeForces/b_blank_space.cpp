#include <iostream>
#include <vector>

using namespace std;

int main() {
    int t;
    cin >> t; 

    for (int _ = 0; _ < t; _++) {
        int a;
        cin >> a;

        vector<int> b(a);
        for (int i = 0; i < a; i++) {
            cin >> b[i];
        }

        vector<int> l;
        int n = 0;
        for (int i = 0; i < a; i++) {
            if (b[i] == 0) {
                n++;
            }
            if (b[i] != 0 || i == a - 1) {
                l.push_back(n);
                n = 0;
            }
        }

        int maxElement = -1;
        for (int i = 0; i < l.size(); i++) {
            if (l[i] > maxElement) {
                maxElement = l[i];
            }
        }
        cout << maxElement << endl;
    }

    return 0;
}
