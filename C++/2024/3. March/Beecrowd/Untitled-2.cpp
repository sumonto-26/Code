/*
#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;

int main(){

    double R;
    cin >> R;

    double x = (4.0/3);
    double formula = x * 3.14159 * pow(R,3);
    ans = "VOLUME = "<< fixed << setprecision(3) << formula <<endl;



    return 0;
}

#include <iostream>
using namespace std;

int main(){

    int a,b,c;
    cin >> a;
    cin >> b;
    cin >> c;

    int ans = 0;

    if (a>b){
        if (a>c){
            ans = a ;
        }
        else{
            ans = c;
        }
    }

    else if (b>a){
        if (b>c){
            ans = b;
        }
        else{
            ans = c;
        }
    }

    else{
        if (b>c){
            ans = b;
        }
        else{
            ans = c;
        }
    }

    cout << ans << " eh o maior" << endl;

    return 0;
}


#include <iostream>
#include <iomanip>
using namespace std;

int main(){

    double a,b,c;
    cin >> a;
    cin >> b;
    cin >> c;


    double TRIANGULO = (a*c)/2;
    cout << "TRIANGULO: " << fixed << setprecision(3) << TRIANGULO <<endl;

    double CIRCULO = 3.14159*c*c;
    cout << "CIRCULO: " << fixed << setprecision(3) << CIRCULO <<endl;

    double TRAPEZIO = ((a+b)/2)*c;
    cout << "TRAPEZIO: " << fixed << setprecision(3) << TRAPEZIO <<endl;

    double QUADRADO = b*b;
    cout << "QUADRADO: " << fixed << setprecision(3) << QUADRADO <<endl;

    double RETANGULO = a*b;
    cout << "RETANGULO: " << fixed << setprecision(3) << RETANGULO <<endl;


    return 0;
}


// 1015 //
#include <iostream>
#include <iomanip>
#include <cmath>
using namespace std;

int main(){
    double x1,y1,x2,y2;
    cin >> x1;
    cin >> y1;
    cin >> x2;
    cin >> y2;

    double distance = sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2));
    cout << fixed << setprecision(4) << distance << endl;

    return 0;
}

// 1017 //
#include <iostream>
#include <iomanip>
using namespace std;

int main(){

    double time, speed;
    cin >> time;
    cin >> speed;

    double fuel = (time * speed) / 12;
    cout << fixed << setprecision(3) << fuel << endl;

    return 0;
}



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


#include <iostream>
using namespace std;

int main(){

    int a,b,c,d;
    cin >> a,
    cin >> b,
    cin >> c,
    cin >> d;

    if (b > c && d > a && (c+d) > (a+b) && d > 0 && c > 0 && a % 2 == 0){
        cout << "Valores aceitos" << endl ;
    }
    else{
        cout << "Valores nao aceitos" << endl ;
    }

    return 0;
}


*/

#include <iostream>
using namespace std;

void bubbleSort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                // Swap arr[j] and arr[j+1]
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}

// Function declaration
std::string print_ans(const int arr[], int n) {
    // Example: Concatenate all elements of the array into a string
    std::string result;
    for (int i = 0; i < n; ++i) {
        result += std::to_string(arr[i]) + "\n";
    }
    return result;


}
int main(){

    int n = 3;
    int* arr = new int[n];
    for (int i = 0;  i<n; i++){
        cin >> arr[i];
    }

    string ans = print_ans(arr, n);
    bubbleSort(arr, n);
    cout << print_ans(arr, n);
    cout << endl;
    cout << ans;    


    return 0;
}