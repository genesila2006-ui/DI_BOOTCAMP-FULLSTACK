// Daily Challenge 1 - Triangle Pattern

// Version 1: One loop
let pattern1 = "";
for (let i = 1; i <= 6; i++) {
  pattern1 += "* ";
  console.log(pattern1.trim());
}

// Version 2: Nested loops
for (let i = 1; i <= 6; i++) {
  let row = "";
  for (let j = 1; j <= i; j++) {
    row += "* ";
  }
  console.log(row.trim());
}
