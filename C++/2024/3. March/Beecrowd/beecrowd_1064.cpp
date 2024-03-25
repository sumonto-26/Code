#include <iostream>
#include <iomanip>
using namespace std;

int main(){
    int positives = 0;
    float sum = 0;
    for (int i=0; i<6; i++){
        float number;
        cin >> number;
        if (number > 0){
            positives++;
            sum += number;
        }
    }
    double average = sum / positives;
    cout << positives << " valores positivos" << endl;
    cout << fixed << setprecision(1) << average <<endl;
    
    return 0;
}