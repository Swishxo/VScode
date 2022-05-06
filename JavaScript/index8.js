//for-loop vs for-in loop

let letters = ["H","E","L","P"];

//for-loop
for(let i = 0; i < letters.length; i++){
    console.log(letters[i]);
}
//for-in loop: mainly used to loop through objects
for(let i in letters){
    console.log(letters[i]);
}

let Car = {
    make: "BMW",
    year: 2015,
    color: "Blue"
}

for(let property in Car){
    console.log(Car[property]);
}