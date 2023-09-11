#!/usr/bin/node

const arg = process.argv;
let max = 0;
let secondMax = 0;
if (arg.length === 3 || arg.length === 2) {
  console.log(secondMax);
} else {
  for (const ele of arg) {
    if (ele > max) {
      secondMax = max;
      max = ele;
    }
  }
  console.log(secondMax);
}
