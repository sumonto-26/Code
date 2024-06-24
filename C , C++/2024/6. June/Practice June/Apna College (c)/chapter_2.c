// 1:07:40 second finish
#include <stdio.h>
#include <math.h>

int main(){
    /*int a,b;
    scanf("%d %d", &a, &b); // input a and b

    // %d is format specifiers
    printf("a = %d and b = %d \n", a, b);
    printf("a+b = %d \n", a+b);
    printf("a-b = %d \n", a-b);
    printf("a*b = %d \n", a*b);
    printf("a/b = %d \n", a/b);*/

    /*
    int a = 22;
    int b = a;
    int c = a-2;
    int d = 1, e; // we difine e but e have't any value.
    //int n, m = 10**2; // INVALID SYNTAX
    int n,m = pow(10,2); // VALID SYNTAX
    int x,y,z;
    x = y = z = e = 100 ;
    printf("m == %d \n", m);

    printf("%d \n", 12%5);
    printf("%d \n", -12%-5);
    printf("%d \n", -12%5);
    printf("%d \n", 12%-5);
*/
    // Logical Operators 
    // AND &&
    printf("%d \n", 1<2 && 1+1 == 2); // 1, 1
    printf("%d \n", 3<2 && 1+1 == 2); // 0, 1
    printf("%d \n", 1<2 && 1+1 == 3); // 1, 0
    printf("%d \n\n", 3<2 && 1+1 == 3); // 0, 0
    // OR ||
    printf("%d \n", 1<2 || 1+1 == 2); // 1, 1
    printf("%d \n", 3<2 || 1+1 == 2); // 0, 1
    printf("%d \n", 1<2 || 1+1 == 3); // 1, 0
    printf("%d \n\n", 3<2 || 1+1 == 3); // 0, 0
    // NOT !
    printf("%d \n", !(1<2) ); // 1
    printf("%d \n", !(3<2) ); // 0

    //Assignment Operators
    int a = 10;
    a += 10;
    printf("a+10 = %d \n", a);
    a -= 10;
    printf("a-10 = %d \n", a);
    a *= 10;
    printf("a*10 = %d \n", a);
    a /= 10;
    printf("a/10 = %d \n", a);
    a %= 10;
    printf("a%c10 = %d \n", '%', a);



    return 0;
}