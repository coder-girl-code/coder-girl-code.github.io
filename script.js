document.write("<h2>Hello!</h2>");
console.log("Helloooooooooo!");
//var name = prompt("Enter your name: ");
//var age = prompt(name + " enter your age:");
// Use of the console displays results in the browsers console

//nameh2 = document.getElementById("name");
//console.log(nameh2);
//nameh2.innerHTML = name;


function onButtonPress(){
    
    name = document.getElementById("nameInput").value

    age = document.getElementById("ageInput").value

    color = document.getElementById("colorInput").value

    console.log("My name is " + name + ' and age is ' + age);


    //h2 = document.getElementsByTagName("h2")

    nameonpage = document.getElementById("nameonpage")
    nameonpage.innerHTML = name;
    ageonpage = document.getElementById("ageonpage")
    ageonpage.innerHTML = age;

    para = document.getElementById("ageIdentifier")


    if (age<13){
        para.innerHTML = "<h2>You are a junior person!<h2><img src='https://static.vecteezy.com/system/resources/previews/000/549/920/original/children-character-set-vector.jpg'>";
    }
    else if (age<18){
        para.innerHTML = "<h2>You are a teenager!<h2><img src='https://img.freepik.com/free-vector/young-people-being-happy_23-2148453662.jpg'>";
    }
    else if (age<100){
        para.innerHTML = "<h2>You are an adult!<h2><img src='https://static.vecteezy.com/system/resources/thumbnails/000/988/062/small_2x/ggroup-of-people-avatar-cartoon.jpg'>";
    }
    else if (age>=100){
        para.innerHTML = "<h2>You are not human -_-<h2><img src='https://i.pinimg.com/736x/69/02/f9/6902f939be2dc07c3a29dd6520e4043e.jpg'>";
    }

    nameonpage.style.backgroundColor = color;
    nameonpage.style.width = '100px';
    nameonpage.style.padding = "10px"

    ageonpage.style.backgroundColor = color;
    ageonpage.style.width = '100px';
    ageonpage.style.padding = '10px'

}


// if the person is a teenager 13 - 17
// if the person is an adult 18 or above
// if the person is a junior bellow 13 
