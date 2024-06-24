// DATE ==> 24 June 2024
#include <stdio.h>
#include <math.h>

int main(){
    
    // Problem 1.
    /*
    int n;
    printf("Enter a Number: ");
    scanf("%d", &n);

    int sum = 0;
    for (int i=1; i<=n; i++){
        sum += i;
    }
    printf("%d == %d", sum, ((n*n)+n)/2);
    */

    // Problem 2.
    /*
    int n;
    printf("Enter a Number: ");
    scanf("%d", &n);

    int sum = 0;
    for (int i=1; i<=n; i++){
        sum += i*i;
    }
    printf("%d", sum);
    */

    // Problem 3.
    int n;
    printf("Enter a Number: ");
    scanf("%d", &n);

    int sum = 0;
    for (int i=1; i<=n; i++){
        sum += pow(i,i);
    }
    printf("%d", sum);


    return 0;
}