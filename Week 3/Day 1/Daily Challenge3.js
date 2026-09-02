const numbers = [5, 0, 9, 1, 7, 4, 2, 6, 3, 8];

// 1. .toString()
const str1 = numbers.toString();
console.log(str1); // "5,0,9,1,7,4,2,6,3,8"
console.log(typeof str1); // "string"

// .toString() always uses commas and does not let you choose a separator.

// 2. .join()
const joinComma = numbers.join(",");
console.log(joinComma); // "5,0,9,1,7,4,2,6,3,8"

const joinPlus = numbers.join("+");
console.log(joinPlus); // "5+0+9+1+7+4+2+6+3+8"

const joinSpace = numbers.join(" ");
console.log(joinSpace); // "5 0 9 1 7 4 2 6 3 8"

const joinEmpty = numbers.join("");
console.log(joinEmpty); // "5091742638"

// Try .join("-") or .join(" | ") too — any string works as the separator.

// 3. Bonus: Bubble Sort (descending) with nested for loops
console.log("Starting array:", numbers);

for (let i = 0; i < numbers.length - 1; i++) {
  for (let j = 0; j < numbers.length - 1 - i; j++) {
    if (numbers[j] < numbers[j + 1]) {
      let temp = numbers[j];
      numbers[j] = numbers[j + 1];
      numbers[j + 1] = temp;

      console.log(`Swapped index ${j} and ${j + 1}:`, numbers);
    }
  }

  console.log(`End of pass ${i + 1}:`, numbers);
}

console.log("Final sorted array:", numbers);
// [9,8,7,6,5,4,3,2,1,0]

/*
How to think about it:
- Outer loop (i): how many passes are needed? Answer: length - 1 times.
- Inner loop (j): compare each pair of neighbors and swap if they are in the wrong order.
- Why numbers.length - 1 - i? Because each pass places one more value in its final position.
- The temp variable is necessary because otherwise numbers[j] would be overwritten before saving it.
*/