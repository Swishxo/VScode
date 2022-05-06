/*
Function: used to perform a block of code, a particular task/procedure AKA (subroutine)

We invoke AKA (Call) a fucnction when we want to do something
*/

//Keyword function and the name of function 
function sayHello(){
    console.log("hello");
};

function dayType(){
    console.log("Today is a nice day");
};

function signOff(){
    console.log("Goodbye");
};
//call function
sayHello();
dayType();
signOff();

//can pass variables as parameters to functions to be used
var myName = "Steph";
function testFunc(myName){
    console.log(myName);
};
testFunc(myName);

