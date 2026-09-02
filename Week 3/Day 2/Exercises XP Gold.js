// EXERCISE 1: Random Number
function randomNumberExercise() {
  const randomNum = Math.floor(Math.random() * 100) + 1;
  console.log("Random number:", randomNum);
  
  let evenNumbers = [];
  for (let i = 0; i <= randomNum; i += 2) {
    evenNumbers.push(i);
  }
  
  console.log("Even numbers from 0 to", randomNum, ":", evenNumbers.join(" "));
}

randomNumberExercise();

// EXERCISE 2: Capitalized Letters
function capitalize(str) {
  let result1 = "";
  let result2 = "";

  for (let i = 0; i < str.length; i++) {
    if (i % 2 === 0) {
      result1 += str[i].toUpperCase();
      result2 += str[i].toLowerCase();
    } else {
      result1 += str[i].toLowerCase();
      result2 += str[i].toUpperCase();
    }
  }

  return [result1, result2];
}

console.log(capitalize("abcdef"));

// EXERCISE 3: Is Palindrome?
function isPalindrome(str) {
  const reversed = str.split("").reverse().join("");
  return str === reversed;
}

console.log(isPalindrome("madam"));
console.log(isPalindrome("bob"));
console.log(isPalindrome("kayak"));
console.log(isPalindrome("hello"));

// EXERCISE 4: Biggest Number
function biggestNumberInArray(arrayNumber) {
  let biggest = 0;

  for (let i = 0; i < arrayNumber.length; i++) {
    if (typeof arrayNumber[i] === "number" && arrayNumber[i] > biggest) {
      biggest = arrayNumber[i];
    }
  }

  return biggest;
}

console.log(biggestNumberInArray([-1, 0, 3, 100, 99, 2, 99]));
console.log(biggestNumberInArray(["a", 3, 4, 2]));
console.log(biggestNumberInArray([]));

// EXERCISE 5: Unique Elements
function getUniqueElements(arr) {
  return [...new Set(arr)];
}

console.log(getUniqueElements([1, 2, 3, 3, 3, 3, 4, 5]));

// EXERCISE 6: Calendar
function createCalendar(year, month) {
  const weekdays = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"];
  
  const table = document.createElement("table");
  table.style.border = "1px solid black";
  table.style.borderCollapse = "collapse";

  // Create header with weekday names
  const headerRow = document.createElement("tr");
  for (let day of weekdays) {
    const th = document.createElement("th");
    th.textContent = day;
    th.style.border = "1px solid black";
    th.style.padding = "10px";
    th.style.width = "40px";
    th.style.textAlign = "center";
    headerRow.appendChild(th);
  }
  table.appendChild(headerRow);

  // Get the first day of the month and number of days
  const firstDay = new Date(year, month - 1, 1).getDay();
  const daysInMonth = new Date(year, month, 0).getDate();

  // Adjust for Monday start (getDay returns 0 for Sunday)
  const startDay = firstDay === 0 ? 6 : firstDay - 1;

  let date = 1;
  let currentRow = document.createElement("tr");

  // Add empty cells before the first day
  for (let i = 0; i < startDay; i++) {
    const td = document.createElement("td");
    td.style.border = "1px solid black";
    td.style.padding = "10px";
    td.style.height = "40px";
    currentRow.appendChild(td);
  }

  // Add dates
  for (let i = startDay; date <= daysInMonth; i++) {
    if (i % 7 === 0 && i !== 0) {
      table.appendChild(currentRow);
      currentRow = document.createElement("tr");
    }

    const td = document.createElement("td");
    td.textContent = date;
    td.style.border = "1px solid black";
    td.style.padding = "10px";
    td.style.textAlign = "center";
    td.style.height = "40px";
    currentRow.appendChild(td);
    date++;
  }

  // Fill remaining cells
  while (currentRow.children.length < 7) {
    const td = document.createElement("td");
    td.style.border = "1px solid black";
    td.style.padding = "10px";
    td.style.height = "40px";
    currentRow.appendChild(td);
  }

  table.appendChild(currentRow);
  return table;
}

// Add calendar to DOM if available
if (typeof document !== "undefined") {
  const container = document.body;
  if (container) {
    container.appendChild(createCalendar(2012, 9));
  }
}


