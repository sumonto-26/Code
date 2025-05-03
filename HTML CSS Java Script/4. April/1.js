// console.log("Hello World for everyone!!!!!"); 
// console.log("Hello World for everyone!!!!!"); 
// console.log("Hello World for everyone!!!!!"); 
n = 99.99;
x = null;
y = undefined;
bool1 = true;
bool2 = false;
// var was used before 2015 now let and const are used.
var Name = "Sumonto"; // can update can re-declared A Global scope Variable
let age = "Fifteen"; // can update can't re-declared A Block scope Variable
const pi = 3.1415926; // can't update can't re-declared A Block scope Variable

let a;
// const b;// given error

// Printing variables
/*
console.log(Name);
console.log(age);
console.log(n);
console.log(x);
console.log(y);
console.log(pi);
console.log(bool1);
console.log(bool2);
console.log(a);
*/

/*
{
    let a = 5;
    console.log(a);
}
{
    let a = 10;
    console.log(a);
}
*/

/*
let bi = BigInt("1232344454654654635435132413254");
let sy = Symbol("HeLlO");

console.log(typeof(Name));
console.log(x);
console.log(typeof(x));
console.log(bi);
console.log(typeof(bi));
console.log(sy);
console.log(typeof(sy));
*/

const Student = {
    // Key : Value,
    fullName : "Student name",
    age : 20,
    cgpa : 9.5,
    isPass : true
};

Student["age"] = Student["age"]+1;
Student["age"] = Student.age+1;
Student.age = Student["age"]+1;
Student.age = Student.age+1;

Student.fullName = 'SUMONTO datta';

console.log(typeof(Student));
console.log(typeof(Student.isPass));
console.log(Student["fullName"]);
console.log(Student.age);