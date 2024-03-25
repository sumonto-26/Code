
#include <iostream>
#include <cmath>
using namespace std;

int main(){

    int n ;
    cin >> n;

    int year = floor(n / 365);
    cout << year <<" ano(s)" << endl;

    int month = (n-(year*365)) / 30;
    cout << month << " mes(es)" << endl;

    int day = (n-((year*365)+(month*30)));
    cout << day << " dia(s)" << endl;

    return 0;
}
