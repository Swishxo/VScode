/*
A JavaScript Set is a collection of unique values.
Each value can only occur once in a Set.

*/

//Pass an Array to the new Set() constructor:

//const letters = new Set(["a","b","c"]);//A short cut

//Create a Set and add values:
 const letters = new Set();
 //add values to the set
 letters.add("a");
 letters.add("b");
 letters.add("c");
 letters.add("d");
 //can also add a variable
 var x = "Hello";
 letters.add(x);

 //use forEach() to loop through set
 letters.forEach(function(eachElement){
     console.log(eachElement);
 })

