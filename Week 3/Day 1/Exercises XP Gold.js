// Exercise 1: List of people
const people = ["Greg", "Mary", "Devon", "James"];

// Part I - Review about arrays
people.shift(); // 1. Remove Greg
people[people.indexOf("James")] = "Jason"; // 2. Replace James with Jason
people.push("YourName"); // 3. Add your name to the end

const maryIndex = people.indexOf("Mary"); // 4. Mary’s index
console.log(maryIndex);

const peopleCopy = people.slice(1, 3); // 5. Copy without Mary and your name
console.log(peopleCopy);

console.log(people.indexOf("Foo")); // 6. Returns -1 because Foo is not in the array

const last = people[people.length - 1]; // 7. Last element of the array
console.log(last);

// Part II - Loops
for (let i = 0; i < people.length; i++) {
  console.log(people[i]);
}

for (let i = 0; i < people.length; i++) {
  console.log(people[i]);
  if (people[i] === "Devon") {
    break;
  }
}

// Exercise 2: Your favorite colors
const colors = ["blue", "red", "green", "yellow", "purple"];

for (let i = 0; i < colors.length; i++) {
  console.log(`My #${i + 1} choice is ${colors[i]}`);
}

// Bonus
const suffixes = ["st", "nd", "rd", "th", "th", "th", "th", "th", "th", "th"];
for (let i = 0; i < colors.length; i++) {
  const suffix = suffixes[i] || "th";
  console.log(`My ${i + 1}${suffix} choice is ${colors[i]}`);
}

// Exercise 3: Repeat the question
let number = Number(prompt("Please enter a number"));

while (Number.isNaN(number) || number < 10) {
  number = Number(prompt("Please enter a valid number greater than or equal to 10"));
}

console.log(`You entered: ${number}`);

// Exercise 4: Building Management
const building = {
  numberOfFloors: 4,
  numberOfAptByFloor: {
    firstFloor: 3,
    secondFloor: 4,
    thirdFloor: 9,
    fourthFloor: 2,
  },
  nameOfTenants: ["Sarah", "Dan", "David"],
  numberOfRoomsAndRent: {
    sarah: [3, 990],
    dan: [4, 1000],
    david: [1, 500],
  },
};

console.log(building.numberOfFloors);
console.log(
  building.numberOfAptByFloor.firstFloor +
    building.numberOfAptByFloor.thirdFloor
);
console.log(
  building.nameOfTenants[1],
  building.numberOfRoomsAndRent.dan[0]
);

if (
  building.numberOfRoomsAndRent.sarah[1] +
    building.numberOfRoomsAndRent.david[1] >
  building.numberOfRoomsAndRent.dan[1]
) {
  building.numberOfRoomsAndRent.dan[1] = 1200;
}

console.log(building.numberOfRoomsAndRent.dan);

// Exercise 5: Family
const family = {
  father: "John",
  mother: "Jane",
  son: "Tom",
  daughter: "Emma",
};

for (const key in family) {
  console.log(key);
}

for (const key in family) {
  console.log(family[key]);
}

// Exercise 6: Rudolf
const details = {
  my: "name",
  is: "Rudolf",
  the: "reindeer",
};

let sentence = "";
for (const key in details) {
  sentence += `${key} ${details[key]} `;
}
console.log(sentence.trim());

// Exercise 7: Secret Group
const names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];
const secretSociety = names
  .map((name) => name[0])
  .sort()
  .join("");

console.log(secretSociety);

// Exercise 6: Object exercise
const myProfile = {
  name: "John",
  age: 25,
  city: "Paris",
  hobbies: ["reading", "traveling", "coding"],
};

module.exports = { myProfile };

