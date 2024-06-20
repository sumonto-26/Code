// DATE ==> 28 April 2024
// AUTHOR ==> SUMONTO

#include <bits/stdc++.h>
using namespace std;


int main() {
    double a, b;
    cin >> a >> b;
    
    vector<double> lights;
    for (int i = 0; i < a; ++i) {
        double light;
        cin >> light;
        lights.push_back(light);
    }
    
    sort(lights.begin(), lights.end());

    vector<double> d;
    d.push_back(lights[0]);

    for (int j = 0; j < a - 1; ++j) {
        d.push_back((lights[j + 1] - lights[j]) / 2);
    }
    d.push_back(b - lights[a - 1]);

    double answer = *max_element(d.begin(), d.end());
    cout << fixed << setprecision(10) << round(answer * 1e10) / 1e10 << endl;
    return 0;
}