// Week 3 - Day 1 - JavaScript XP Exercises

const { myProfile } = require("./Exercises XP Gold.js");

// Exercise 1: Favorite food and meal
const favoriteFood = "pizza";
const favoriteMeal = "dinner";
console.log(`I eat ${favoriteFood} at every ${favoriteMeal}.`);

// Exercise 2: Watched series
const myWatchedSeries = [
  "The Office",
  "Stranger Things",
  "Breaking Bad",
  "The Crown",
];
console.log(`I watched ${myWatchedSeries.length} series:`);
for (const series of myWatchedSeries) {
  console.log(`- ${series}`);
}

// Exercise 3: Replace a value in an array
const myWatchedSeries2 = [
  "The Office",
  "Stranger Things",
  "Breaking Bad",
  "The Crown",
];
myWatchedSeries2[2] = "Better Call Saul";
console.log("Updated series:", myWatchedSeries2);

// Exercise 4: Temperature conversion
const celsius = 20;
const fahrenheit = (celsius / 5) * 9 + 32;
console.log(`${celsius}°C is ${fahrenheit}°F.`);

// Exercise 5: Comparison
const number1 = 5;
const number2 = 7;
console.log(`Is ${number1} greater than ${number2}?`, number1 > number2);

console.log(myProfile);
console.log(`My name is ${myProfile.name}, I am ${myProfile.age} years old and I live in ${myProfile.city}.`);

// Exercise 7: Array of users
const users = [
  { firstName: "Bradley", lastName: "Bouley", age: 40 },
  { firstName: "Chloe", lastName: "Bouley", age: 35 },
  { firstName: "Jonathan", lastName: "Bouley", age: 30 },
];

for (const user of users) {
  console.log(`${user.firstName} ${user.lastName} is ${user.age} years old.`);
}

// Exercise 8: Functions
function sumNumbers(a, b) {
  return a + b;
}

console.log("The sum is:", sumNumbers(10, 5));

// Exercise 9: String transformation
const sentence = "This is a random sentence.";
console.log(sentence.toUpperCase());
console.log(sentence.replace("random", "short"));

// Exercise 10: Guessing logic
const guess = 10;
if (guess > 10) {
  console.log("Your guess is too high.");
} else if (guess < 10) {
  console.log("Your guess is too low.");
} else {
  console.log("Correct! You guessed the number.");
}

// ---------------------------------------------------------------
// Exercise 1: Find the numbers divisible by 23
// ---------------------------------------------------------------
function displayNumbersDivisible(divisor = 23) {
  let total = 0;
  let result = [];

  for (let i = 0; i <= 500; i++) {
    if (i % divisor === 0) {
      result.push(i);
      total += i;
    }
  }

  console.log("Numbers divisible by", divisor + ":", result.join(" "));
  console.log("Sum:", total);
}

displayNumbersDivisible();
displayNumbersDivisible(3);
displayNumbersDivisible(45);

// ---------------------------------------------------------------
// Exercise 2: Shopping List
// ---------------------------------------------------------------
const stock = {
  banana: 6,
  apple: 0,
  pear: 12,
  orange: 32,
  blueberry: 1,
};

const prices = {
  banana: 4,
  apple: 2,
  pear: 1,
  orange: 1.5,
  blueberry: 10,
};

const shoppingList = ["banana", "orange", "apple"];

function myBill() {
  let total = 0;

  for (const item of shoppingList) {
    if (item in stock && stock[item] > 0) {
      total += prices[item];
      stock[item] -= 1;
    }
  }

  return total;
}

console.log("Shopping bill:", myBill());
console.log("Updated stock:", stock);

// ---------------------------------------------------------------
// Exercise 3: What's in my wallet ?
// ---------------------------------------------------------------
function changeEnough(itemPrice, amountOfChange) {
  const coinValues = [0.25, 0.1, 0.05, 0.01];
  const totalChange = amountOfChange.reduce(
    (sum, coin, index) => sum + coin * coinValues[index],
    0
  );

  return totalChange >= itemPrice;
}

console.log(changeEnough(4.25, [25, 20, 5, 0]));
console.log(changeEnough(14.11, [2, 100, 0, 0]));
console.log(changeEnough(0.75, [0, 0, 20, 5]));

// ---------------------------------------------------------------
// Exercise 4: Vacations Costs
// ---------------------------------------------------------------
function hotelCost() {
  let nights;

  while (true) {
    nights = Number(prompt("How many nights would you like to stay?"));
    if (!Number.isNaN(nights) && nights > 0) {
      return nights * 140;
    }
    console.log("Please enter a valid number of nights.");
  }
}

function planeRideCost() {
  let destination;

  while (true) {
    destination = prompt("Where are you flying to?");
    if (typeof destination === "string" && destination.trim() !== "") {
      const cleanDestination = destination.trim().toLowerCase();
      if (cleanDestination === "london") return 183;
      if (cleanDestination === "paris") return 220;
      return 300;
    }
    console.log("Please enter a valid destination.");
  }
}

function rentalCarCost() {
  let days;

  while (true) {
    days = Number(prompt("How many days would you like to rent the car?"));
    if (!Number.isNaN(days) && days > 0) {
      let total = days * 40;
      if (days > 10) {
        total *= 0.95;
      }
      return total;
    }
    console.log("Please enter a valid number of days.");
  }
}

function totalVacationCost() {
  const hotel = hotelCost();
  const plane = planeRideCost();
  const car = rentalCarCost();

  const total = hotel + plane + car;
  console.log(`The car cost: $${car}, the hotel cost: $${hotel}, the plane tickets cost: $${plane}.`);
  console.log(`Total vacation cost: $${total}`);
  return total;
}

totalVacationCost();

// ---------------------------------------------------------------
// Exercise 5: Users (DOM)
// ---------------------------------------------------------------
const userContainer = document.getElementById("container");
console.log(userContainer);

const allLists = document.querySelectorAll(".list");
const pete = allLists[0].querySelectorAll("li")[1];
pete.textContent = "Richard";

const secondListItems = allLists[1].querySelectorAll("li");
secondListItems[1].remove();

for (const list of allLists) {
  const firstItem = list.querySelector("li");
  if (firstItem) firstItem.textContent = "YourName";
}

allLists.forEach((list) => list.classList.add("student_list"));
allLists[0].classList.add("university", "attendance");

userContainer.style.backgroundColor = "lightblue";
userContainer.style.padding = "10px";

const dan = document.querySelector("li:last-child");
if (dan) dan.style.display = "none";

const richard = document.querySelector("li:nth-child(2)");
if (richard) richard.style.border = "2px solid black";

document.body.style.fontSize = "20px";

if (userContainer.style.backgroundColor === "lightblue") {
  const names = [...document.querySelectorAll("li")].map((li) => li.textContent.trim());
  alert(`Hello ${names[0]} and ${names[1]}`);
}

// ---------------------------------------------------------------
// Exercise 6: Change the navbar
// ---------------------------------------------------------------
const navBar = document.getElementById("navBar");
navBar.setAttribute("id", "socialNetworkNavigation");

const ul = navBar.querySelector("ul");
const newLi = document.createElement("li");
const logoutText = document.createTextNode("Logout");
newLi.appendChild(logoutText);
ul.appendChild(newLi);

const firstLi = ul.firstElementChild;
const lastLi = ul.lastElementChild;
console.log(firstLi.textContent);
console.log(lastLi.textContent);

// ---------------------------------------------------------------
// Exercise 7: My Book List
// ---------------------------------------------------------------
const section = document.querySelector(".listBooks");
const allBooks = [
  {
    title: "Harry Potter",
    author: "J.K. Rowling",
    image: "https://images.unsplash.com/photo-1512820790803-83ca734da794",
    alreadyRead: true,
  },
  {
    title: "The Hobbit",
    author: "J.R.R. Tolkien",
    image: "https://images.unsplash.com/photo-1544947950-fa07a98d237f",
    alreadyRead: false,
  },
];

allBooks.forEach((book) => {
  const div = document.createElement("div");
  div.style.marginBottom = "20px";

  const title = document.createElement("p");
  title.textContent = `${book.title} written by ${book.author}`;

  if (book.alreadyRead) {
    title.style.color = "red";
  }

  const image = document.createElement("img");
  image.src = book.image;
  image.width = 100;

  div.appendChild(title);
  div.appendChild(image);
  section.appendChild(div);
});
