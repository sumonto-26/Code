#include <iostream>
using namespace std;

int main(){
    int month_number;
    cin >> month_number;

    string month_list[12] = {
        "January","February","March",
        "April","May","June",
        "July","August","September",
        "October","November","December"};

    cout << month_list[month_number-1] << endl;

    return 0;
}