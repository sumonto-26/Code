#include <iostream>
#include <cmath>
using namespace std;

int main(){

    int second; 
    cin >> second;
    
    int hour = floor(second / 3600);
    int minute;

    if (hour != 0){
        minute = floor((second - (hour*3600)) / 60);
    }
    else{
        minute = floor(second / 60);
    }

    if (second < 60){
        cout << "0:0:" << second << endl;
    }
    else{
        cout << hour << ":" << minute << ":" << second - ((hour*3600)+(minute*60)) << endl; 

    }
    
    return 0;
}

