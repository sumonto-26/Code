#include <iostream>
using namespace std;

int main(){
    int number;
    cin >> number;

    for (int j = 1; j < number*4; j+= 4)
    {
        cout << j << " " << j+1 << " " << j+2 << " PUM" << endl;
    }
    
    return 0;
}