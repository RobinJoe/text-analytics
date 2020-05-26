document.getElementById("vowel").addEventListener("click",vowelSelect);
//Event listener for clicking the vowel request button
function vowelSelect() {
    var letter1 = " ";
    var vowels = "AEIOU";
//Set up a function called vowel select
//Create two objects, and place nothing inside 1, and vowels inside the second.
//These are lists.

letter1 = vowels.charAt(Math.floor(Math.random() * vowels.length));
//Multiply the result of the Math.random function by the length - the number of characters - in the vowels object.
//Math.random returns a value between 0 and 1. Math.floor rounds down to the nearest whole number.

console.log(letter1);
buttonAction(letter1)
//Log the selected letter chosen to the console.
}

document.getElementById("consonant").addEventListener("click",consonantSelect);
//repeat the same action for consonants.
function consonantSelect() {
    var letter2 = " ";
    var consonants = "BCDFGHJKLMNPQRSTVWXYZ";

letter2 = consonants.charAt(Math.floor(Math.random() * consonants.length))

console.log(letter2);
buttonAction(letter2)
}


//Now that the script logs letters, we need the HTML of the web page to express the
//selected letters.
//Retrieve the image file with the name that matches the selected letter.
let letterSelected = document.getElementById("letter-selected")

function buttonAction(selected) {
  let div = document.createElement("div");
  let img = document.createElement("img");
  img.setAttribute("src","img/"+selected+".png");
  div.appendChild(img);
  letterSelected.appendChild(div);
}

//An earlier attempt at an if else statement version of the letter selector:

//function buttonAction(T) {
   //let T = letter1
//   let div = document.createElement("div");
//   let img = document.createElement("img");

//   if (T.includes("AEIOU")) {
//     img.setAttribute("src","img/Vowel/"+T+".png");
//     div.appendChild(img);
//     letterSelected.appendChild(div);
//   } else {
//     img.setAttribute("src","img/Consonant/"+T+".png");
//     div.appendChild(img);
//     letterSelected.appendChild(div);
//   }

//}

//document.getElementsById("vowel").addEventListener("click", buttonAction);

//let letterSelected = document.getElementById("letter-selected")

//function buttonAction() {
//    let T0 = letter2
//    let div = document.createElement("div");
//    let img = document.createElement("img");
//    img.setAttribute("src","/img/Consonant/"+T0.imageName());
//}

//document.getElementById("consonant").addEventListener("click", buttonAction);

//Another earlier attempt

//function  letterSelctor(len) {
//    var letter = " ";
//    var consonants = "BCDFGHJKLMNPQRSTVWXYZ";
//    var vowel = "AEIOU";

//for( var i=0; i < len; i++ )
//    letter += consonants.charAt(Math.floor(Math.random() * consonants.length));

//return letter;
//}