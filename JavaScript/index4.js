//type conversion of numbers, strings, booleans
//(Explicit vs implicit)

//change the data type of a value to another

var strNum = "24";
console.log(typeof strNum);//type is string
//convert to an int
var num = Number(strNum);
console.log(typeof num);

//convert back to a string
strNum = String(num);
console.log(typeof strNum);

