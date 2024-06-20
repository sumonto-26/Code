#include <stdio.h>
#include <math.h>

int main(){
    // IF , ELSE IF , ELSE
/*
    int age;
    printf("Enter your age: \n");
    scanf("%d", &age);
    if(age >= 18) {
    printf("you are an adult");
    }
    else {
    printf("you are not an adult");
    }

    
    if(age < 12) {
    printf("child");
    }
    else if(age < 18) {
    printf("teenager");
    }
    else {
    printf("adult");
    }
*/

    // Ternary Operator.
    int age;
    printf("Enter age : ");
    scanf("%d", &age);
    age > 18 ? printf("adult \n") : printf("not adult \n");
    int number = 7;

    int luckyNumber = 7;
    number == luckyNumber ? printf("you are lucky \n") : printf("you are not lucky \n");

    // Switch (integer)
    int day1 = 5;
    switch(day1) {
    case 1 : printf("monday \n");
        break;
    case 2 : printf("tuesday \n");
        break;
    case 3 : printf("wednesday \n");
        break;
    case 4 : printf("thursday \n");
        break;
    case 5 : printf("friday \n");
        break;
    case 6 : printf("saturday \n");
        break;
    case 7 : printf("sunday \n");
        break;
    }

    // Switch (character)
    char day2 = 'f';
    switch(day2) {
    case 'm' : printf("monday \n");
        break;
    case 't' : printf("tuesday \n");
        break;
    case 'w' : printf("wednesday \n");
        break;
    case 'T' : printf("thursday \n");
        break;
    case 'f' : printf("friday \n");
        break;
    case 's' : printf("saturday \n");
        break;
    case 'S' : printf("sunday \n");
        break;

    }

    return 0;
}