/*
array = a special variable,
        that can hold more than one value.

        Each "space" is known as an element

        access elements by indexing ex.[0]

*/

var cars = ["Mustang", "BMX", "Tesla"];

console.log(cars);//displays the whole array
console.log(cars[0]);//display the first element
console.log(cars[1]);//display the second element
console.log(cars[2]);//display the third element

//To add elements to an array, you must use the push method
cars.push("Jaguar");
//console.log(cars[3]);

//To remove the last element of an array, us the pop method
cars.pop();
//console.log(cars[3]);

//Check the length of array
var numCars = cars.length;
console.log(numCars);

//can sort array in order, using sort method
cars = cars.sort();
console.log(cars);

//reverse sort an array
cars = cars.reverse();
console.log(cars);

