// Version 1: using one loop
let pattern = "";
for (let i = 1; i <= 6; i++) {
  pattern += "* ";
  console.log(pattern.trim());
}

console.log("-------------------");

// Version 2: using nested loops
for (let row = 1; row <= 6; row++) {
  let line = "";
  for (let col = 1; col <= row; col++) {
    line += "* ";
  }
  console.log(line.trim());
}
