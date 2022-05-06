/*
A Map holds key-value pairs where the keys can be any datatype.
A Map remembers the original insertion order of the keys.
*/

//You can add elements to a Map with the set() method:

let fruits = new Map();
//set the values: "key", value
fruits.set("apples", 500);
fruits.set("Bannanas", 300);
fruits.set("oranges", 200);

//The get() method gets the value of a key in a Map:
fruits.get("apples");
//The has() method returns true if a key exists in a Map:
fruits.has("apples");