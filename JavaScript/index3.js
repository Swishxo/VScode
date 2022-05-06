//user input

//Easy way to get input 

//var myName = window.prompt("Whats your name?"); //user input stored in var
//console.log("Hello", myName);//display input 

//harder way to get user input, but is more convenient 
//after creating elements in html document within body

//doucment: reffers to html your JS is linked to
document.getElementById("myButton").onclick = function(){//when myButton is clicked, 
    //whatever value is entered is stored in myName 
    var myName = document.getElementById("myText").value;

    console.log("Hello", myName);
}
