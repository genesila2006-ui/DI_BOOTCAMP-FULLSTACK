// Exercise 1: Checking the BMI

const person1 = {
  FullName: "John",
  Mass: 80,
  Height: 1.8,
  calcBMI: function () {
    return this.Mass / (this.Height * this.Height);
  },
};

const person2 = {
  FullName: "Sarah",
  Mass: 70,
  Height: 1.65,
  calcBMI: function () {
    return this.Mass / (this.Height * this.Height);
  },
};

function compareBMI(personA, personB) {
  const bmiA = personA.calcBMI();
  const bmiB = personB.calcBMI();

  if (bmiA > bmiB) {
    console.log(`${personA.FullName} has the largest BMI.`);
  } else if (bmiB > bmiA) {
    console.log(`${personB.FullName} has the largest BMI.`);
  } else {
    console.log("Both persons have the same BMI.");
  }
}

compareBMI(person1, person2);

// Exercise 2: Grade Average

function findAvg(gradesList) {
  const total = gradesList.reduce((sum, grade) => sum + grade, 0);
  const average = total / gradesList.length;

  console.log(`Average: ${average}`);

  if (average > 65) {
    console.log("You passed!");
  } else {
    console.log("You failed and must repeat the course.");
  }
}

// Bonus: split into two functions
function calculateAverage(gradesList) {
  const total = gradesList.reduce((sum, grade) => sum + grade, 0);
  return total / gradesList.length;
}

function checkResult(gradesList) {
  const average = calculateAverage(gradesList);
  console.log(`Average: ${average}`);

  if (average > 65) {
    console.log("You passed!");
  } else {
    console.log("You failed and must repeat the course.");
  }
}

findAvg([70, 80, 90, 60]);
checkResult([60, 70, 80, 50]);

// Extra exercise: not bad
const sentence = "The movie is not that bad, I like it";
const wordNot = sentence.indexOf("not");
const wordBad = sentence.indexOf("bad");

if (wordNot !== -1 && wordBad !== -1 && wordBad > wordNot) {
  const result = sentence.slice(0, wordNot) + "good" + sentence.slice(wordBad + 3);
  console.log(result);
} else {
  console.log(sentence);
}

const example1 = "This dinner is not that bad ! You cook well";
const example2 = "This movie is not so bad !";
const example3 = "This dinner is bad !";

for (const example of [example1, example2, example3]) {
  const notIndex = example.indexOf("not");
  const badIndex = example.indexOf("bad");

  const output =
    notIndex !== -1 && badIndex !== -1 && badIndex > notIndex
      ? example.slice(0, notIndex) + "good" + example.slice(badIndex + 3)
      : example;

  console.log(output);
}
