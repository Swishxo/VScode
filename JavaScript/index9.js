//let = declare variables with a block scope {}
//var = declare variables with a function scope ()

let sum = 0;
let num = [3,5,2,9,6,4,1,8];

//call the forEach() on the array
num.forEach(total);//pass a function that will handel each element or the whole array

function total(element, index, array){
    console.log("Index: " + index + " Element: " + element);//display the index and element in array
    console.log();//display each element position
    console.log("Array: " + array);//display the whole array 

    //Easier to perform operations aswell
    sum += element;
}

console.log("The total of the elements is " + sum);