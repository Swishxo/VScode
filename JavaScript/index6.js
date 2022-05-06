// object = a container for properties/methods

//property = values/variables that describe what an object has 
//methods = functions that describe what an object can do

var human = {
    //properties
    name: "Rick",
    age: 65,

    //methods
    eat: function(){
        console.log("Rick is eating");
    },//each function is seperated by a comma 

    drink: function(){
        console.log("Rick is drinking");
    },//each function is seperated by a comma
    sleep: function(){
        console.log("Rick is sleeping");
    }
};

//how to access objects, dot-notation or brackets
human.name //dot-notation
human["name"] //bracket notation

console.log(human.name);
console.log(human["age"]);

//access the functions
human.eat();
human.drink();
human.sleep();


