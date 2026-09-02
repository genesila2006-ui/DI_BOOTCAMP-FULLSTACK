// EXERCISE 1: Find the numbers divisible by 23
function displayNumbersDivisible(divisor = 23) {
  let numbers = [];
  let sum = 0;

  for (let i = 0; i <= 500; i++) {
    if (i % divisor === 0) {
      numbers.push(i);
      sum += i;
    }
  }

  console.log(numbers.join(" "));
  console.log("Sum:", sum);
}

displayNumbersDivisible();
displayNumbersDivisible(3);
displayNumbersDivisible(45);

// EXERCISE 2: Shopping List
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

  for (let item of shoppingList) {
    if (item in stock && stock[item] > 0) {
      total += prices[item];
      stock[item]--;
    }
  }

  return total;
}

console.log("Bill:", myBill());

// EXERCISE 3: What's in my wallet?
function changeEnough(itemPrice, amountOfChange) {
  const coinValues = [0.25, 0.1, 0.05, 0.01];
  let total = 0;

  for (let i = 0; i < amountOfChange.length; i++) {
    total += amountOfChange[i] * coinValues[i];
  }

  return total >= itemPrice;
}

console.log(changeEnough(4.25, [25, 20, 5, 0]));
console.log(changeEnough(14.11, [2, 100, 0, 0]));
console.log(changeEnough(0.75, [0, 0, 20, 5]));

// EXERCISE 4: Vacation Costs
function hotelCost() {
  let nights = prompt("How many nights would you like to stay in the hotel?");

  while (!nights || isNaN(nights)) {
    nights = prompt("Please enter a valid number of nights:");
  }

  return parseInt(nights) * 140;
}

function planeRideCost() {
  let destination = prompt("Where would you like to go?");

  while (!destination || typeof destination !== "string" || destination.trim() === "") {
    destination = prompt("Please enter a valid destination:");
  }

  const destPrices = {
    London: 183,
    Paris: 220,
  };

  return destPrices[destination] || 300;
}

function rentalCarCost() {
  let days = prompt("How many days would you like to rent the car?");

  while (!days || isNaN(days)) {
    days = prompt("Please enter a valid number of days:");
  }

  let cost = parseInt(days) * 40;

  if (parseInt(days) > 10) {
    cost *= 0.95;
  }

  return cost;
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

// Uncomment to test vacation cost (requires browser/user input):
// totalVacationCost();

// EXERCISE 5: Users DOM Manipulation
// Requires HTML file with id="container" and two <ul class="list"> elements
if (typeof document !== "undefined") {
  const container = document.getElementById("container");
  if (container) {
    console.log(container);

    const lists = document.querySelectorAll(".list");
    const firstUl = lists[0];
    const secondUl = lists[1];

    firstUl.children[1].textContent = "Richard";
    if (secondUl.children.length > 1) {
      secondUl.children[1].remove();
    }

    for (let ul of lists) {
      ul.children[0].textContent = "Alex";
    }

    for (let ul of lists) {
      ul.classList.add("student_list");
    }

    firstUl.classList.add("university", "attendance");

    container.style.backgroundColor = "lightblue";
    container.style.padding = "20px";

    const danLi = Array.from(firstUl.children).find(li => li.textContent === "Dan");
    if (danLi) {
      danLi.style.display = "none";
    }

    const richardLi = Array.from(firstUl.children).find(li => li.textContent === "Richard");
    if (richardLi) {
      richardLi.style.border = "2px solid black";
    }

    document.body.style.fontSize = "18px";

    if (
      window
        .getComputedStyle(container)
        .backgroundColor.toLowerCase() === "rgb(173, 216, 230)" ||
      window.getComputedStyle(container).backgroundColor.toLowerCase() === "lightblue"
    ) {
      alert("Hello Alex and Alex");
    }
  }
}

// EXERCISE 6: Change the navbar
// Requires HTML file with id="navBar" containing <ul> with <li> items
if (typeof document !== "undefined") {
  const navBar = document.getElementById("navBar");
  if (navBar) {
    navBar.setAttribute("id", "socialNetworkNavigation");

    const newLi = document.createElement("li");
    const logoutText = document.createTextNode("Logout");
    newLi.appendChild(logoutText);
    navBar.querySelector("ul").appendChild(newLi);

    const ul = navBar.querySelector("ul");
    const firstLi = ul.firstElementChild;
    const lastLi = ul.lastElementChild;

    console.log("First link:", firstLi.textContent);
    console.log("Last link:", lastLi.textContent);
  }
}

// EXERCISE 7: My Book List
const allBooks = [
  {
    title: "Harry Potter",
    author: "J.K. Rowling",
    image: "https://via.placeholder.com/100?text=Harry+Potter",
    alreadyRead: true,
  },
  {
    title: "The Hobbit",
    author: "J.R.R. Tolkien",
    image: "https://via.placeholder.com/100?text=The+Hobbit",
    alreadyRead: false,
  },
];

if (typeof document !== "undefined") {
  const listBooksSection = document.querySelector(".listBooks");

  if (listBooksSection) {
    allBooks.forEach(book => {
      const bookDiv = document.createElement("div");
      const bookInfo = document.createElement("p");
      const bookImage = document.createElement("img");

      bookImage.src = book.image;
      bookImage.style.width = "100px";

      bookInfo.textContent = `${book.title} written by ${book.author}`;

      if (book.alreadyRead) {
        bookInfo.style.color = "red";
      }

      bookDiv.appendChild(bookImage);
      bookDiv.appendChild(bookInfo);
      listBooksSection.appendChild(bookDiv);
    });
  }
}
