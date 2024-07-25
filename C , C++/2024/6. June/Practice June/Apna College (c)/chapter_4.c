#include <stdio.h>
int main(){
    /*
    for (int i=0; i<5; i++){
        printf("Hello World.\n");
    }

    for (int i=1; i<=100; i++){
        printf("%d\n", i);
    }

    for (int i=100; i>=1; i = i-1){
        printf("%d\n", i);
    }
    
    for (int i=0; i<=10; i++){
        printf("%d \n", i);
    }
    */

    //INCREMENT OPERATORS
    // i++ [pre increment]
    // ++i [post increment]
    // i-- [pre decrement]
    // --i [post decrement]
/*
    int n = 1;
    printf("%d\n", n++); // use, then increase
    printf("%d\n", n); 
    int a = 1;
    printf("%d\n", ++a);// increase, then use
    printf("%d\n", ++a);// increase, then use

    for (float i = 1.0; i <= 5.0; i++){
        printf("%f \n", i);
    }
    for (char ch = 'a'; ch <= 'z'; ch++){
        printf("%c \n", ch);
    }
*/
/*
    // WHILE LOOP
    int i=0;
    while(i<5){
        printf("HELLO WORLD\n");
        i+=1;
    }
    int n,m=0;
    printf("ENTER N: ");
    scanf("%d", &n);
    while(m<=n){
        printf("%d\n",m);
        m++;
    }
*/

    // DO WHILE LOOP
/*
    int i = 0;
    do{
        printf("%d\n", i);
        i++;
    }
    while(i<=100);

    int i = 100;
    do{
        printf("%d\n",i);
        i--;
    }
    while (i>=0);

    int a,b=0;
    printf("ENTER A: ");
    scanf("%d", &a);
    do{
        printf("%d\n", b);
        b++;
    }while(b<=a);
*/

/*
    int n;
    printf("ENTER N: ");
    scanf("%d", &n);

    int sum = 0;
    for(int i=1, j=n ; i<=n && j>=1; i++, j-- ){
        sum += i;
        printf("%d\n", j);
    }
    printf("Sum is %d == %d\n", sum, (n+(n*n))/2);


    return 0;
*/

///////// BREAK; //////////
/*
    int a;
    printf("ENTER A NUMBER: ");
    scanf("%d", &a);

    for (int i=1; i<=10; i++){
        printf("%d x %d == %d\n", a,i, a*i);
    }

    int  n1;
    for(int i=1; ; i++){
        printf("Enter A Number: ");
        scanf("%d", &n1);
        printf("Your number is %d. \n", n1);

        if(n1 % 2 != 0) {
            printf("Thank You \n\n");
            break;
            }
    }

    int n2;
    while(1){
        printf("Enter A Number: ");
        scanf("%d", &n2);
        printf("Your number is %d. \n", n2);
        if (n2 % 7 == 0) {
            printf("Thank You \n\n");
            break;
            }
    }

    int n3;
    do{
        printf("Enter A Number: ");
        scanf("%d", &n3);
        printf("Your number is %d. \n", n3);
        if (n3 % 2 != 0) {
            printf("Thank You \n\n");
            break;
            }
    }
    while(1);
*/

/////// CONTINUE ///////
/*
    for(int i=0; i<=100; i++){
        if (i % 3 == 0){ // skip;
            continue;
        }
        printf("%d\n", i);
    }
*/

    // print all odds between 5-50
    int i = 5;
    do{
        if (i % 2 == 0){
            i ++;
            continue;
        }
        printf("%d\n", i);
        i ++;
    }
    while(i<=50);


}