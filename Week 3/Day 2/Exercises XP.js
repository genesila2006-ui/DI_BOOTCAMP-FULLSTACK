// Exercise 1: Display Numbers Divisible by a Number
// Base solution with bonus parameter
function displayNumbersDivisible(divisor = 23) {
    let sum = 0;
    let numbers = [];

    for (let i = 0; i <= 500; i++) {
        if (i % divisor === 0) {
            numbers.push(i);
            sum += i;
        }
    }

    console.log(numbers.join(" "));
    console.log(`Sum : ${sum}`);
}

displayNumbersDivisible(); // Runs with default divisor 23
// displayNumbersDivisible(3);
// displayNumbersDivisible(45);

// ===============================================
// Exercise 2: Shopping List
// ===============================================
const stock = { 
    "banana": 6, 
    "apple": 0,
    "pear": 12,
    "orange": 32,
    "blueberry": 1
};  

const prices = {    
    "banana": 4, 
    "apple": 2, 
    "pear": 1,
    "orange": 1.5,
    "blueberry": 10
}; 

const shoppingList = ["banana", "orange", "apple"];

function myBill() {
    let totalPrice = 0;

    for (let item of shoppingList) {
        if (item in stock && stock[item] > 0) {
            totalPrice += prices[item];
            stock[item] -= 1; // Bonus: decrease stock by 1
        }
    }

    return totalPrice;
}

console.log(myBill());

// ===============================================
// Exercise 3: What's in my wallet?
// ===============================================
function changeEnough(itemPrice, amountOfChange) {
    const quarterValue = 0.25;
    const dimeValue = 0.10;
    const nickelValue = 0.05;
    const pennyValue = 0.01;

    let totalChange = 
        (amountOfChange[0] * quarterValue) + 
        (amountOfChange[1] * dimeValue) + 
        (amountOfChange[2] * nickelValue) + 
        (amountOfChange[3] * pennyValue);

    return totalChange >= itemPrice;
}

console.log(changeEnough(4.25, [25, 20, 5, 0])); // true
console.log(changeEnough(14.11, [2, 100, 0, 0])); // false
console.log(changeEnough(0.75, [0, 0, 20, 5])); // true

// ===============================================
// Exercise 4: Vacations Costs
// ===============================================
// Bonus implementation: prompt inside totalVacationCost()
function hotelCost(nights) {
    while (isNaN(nights) || nights === "" || nights === null) {
        nights = prompt("Invalid input. Enter number of nights for the hotel:");
    }
    return Number(nights) * 140;
}

function planeRideCost(destination) {
    while (!destination || typeof destination !== "string" || !isNaN(destination)) {
        destination = prompt("Invalid destination. Enter your flight destination:");
    }
    
    let destLower = destination.trim().toLowerCase();
    if (destLower === "london") return 183;
    if (destLower === "paris") return 220;
    return 300;
}

function rentalCarCost(days) {
    while (isNaN(days) || days === "" || days === null) {
        days = prompt("Invalid input. Enter number of days for the car rental:");
    }
    
    let numDays = Number(days);
    let cost = numDays * 40;
    if (numDays > 10) {
        cost *= 0.95; // 5% discount
    }
    return cost;
}

function totalVacationCost() {
    let nightsPrompt = prompt("How many nights would you like to stay in the hotel?");
    let destinationPrompt = prompt("What is your plane destination?");
    let daysPrompt = prompt("How many days would you like to rent a car?");

    let hotel = hotelCost(nightsPrompt);
    let plane = planeRideCost(destinationPrompt);
    let car = rentalCarCost(daysPrompt);

    console.log(`The car cost: $${car}, the hotel cost: $${hotel}, the plane tickets cost: $${plane}`);
    return hotel + plane + car;
}

// ===============================================
// Exercise 5: Users
// ===============================================
// 1. Retrieve the div and console.log it
let divContainer = document.getElementById("container");
console.log(divContainer);

// 2. Change the name "Pete" to "Richard"
let ulLists = document.querySelectorAll(".list");
ulLists[0].children[1].textContent = "Richard";

// 3. Delete the second <li> of the second <ul>
ulLists[1].children[1].remove();

// 4. Change the name of the first <li> of each <ul> to your name
ulLists.forEach(ul => {
    ul.firstElementChild.textContent = "Eugene";
});

// Add class student_list and university/attendance
ulLists.forEach(ul => ul.classList.add("student_list"));
ulLists[0].classList.add("university", "attendance");

// Styling via JS
divContainer.style.backgroundColor = "lightblue";
divContainer.style.padding = "10px";

ulLists[0].lastElementChild.style.display = "none"; // Hide Dan
ulLists[0].children[1].style.border = "1px solid black"; // Border for Richard
document.body.style.fontSize = "18px";

// Bonus
if (divContainer.style.backgroundColor === "lightblue") {
    let users = [];
    ulLists.forEach(ul => {
        Array.from(ul.children).forEach(li => {
            if (li.style.display !== "none") users.push(li.textContent);
        });
    });
    alert(`Hello ${users.join(" and ")}`);
}

// ===============================================
// Exercise 6: Change the navbar
// ===============================================
// 1. Change id attribute
let navBar = document.getElementById("navBar");
navBar.setAttribute("id", "socialNetworkNavigation");

// 2. Add new <li> with "Logout"
let newLi = document.createElement("li");
let newText = document.createTextNode("Logout");
newLi.appendChild(newText);
navBar.firstElementChild.appendChild(newLi);

// 3. Retrieve first and last <li> elements and display text
let firstLink = navBar.firstElementChild.firstElementChild.textContent;
let lastLink = navBar.firstElementChild.lastElementChild.textContent;

console.log(firstLink);
console.log(lastLink);

// ===============================================
// Exercise 7: My Book List
// ===============================================
const allBooks = [
    {
        title: "Atomic Habits",
        author: "James Clear",
        image: "https://images.unsplash.com/photo-1544716278-ca5e3f4abd8c",
        alreadyRead: true
    },
    {
        title: "The Alchemist",
        author: "Paulo Coelho",
        image: "https://images.unsplash.com/photo-1512820790803-83ca734da794",
        alreadyRead: false
    }
];

const section = document.querySelector(".listBooks");

allBooks.forEach(book => {
    const bookDiv = document.createElement("div");
    
    const details = document.createElement("p");
    details.textContent = `${book.title} written by ${book.author}`;
    
    if (book.alreadyRead) {
        details.style.color = "red";
    }
    
    const img = document.createElement("img");
    img.src = book.image;
    img.style.width = "100px";
    
    bookDiv.appendChild(details);
    bookDiv.appendChild(img);
    section.appendChild(bookDiv);
});