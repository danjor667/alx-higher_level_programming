#!/usr/bin/node

const arg = process.argv;
let max = arg[0];
let secondMax = arg[1];
if (arg.length === 3 || arg.length === 2) {
  console.log(secondMax);
} else {
  for (const ele of arg) {
    if (ele > max) {
      secondMax = max;
      max = ele;
    } else if (ele > secondMax) {
      secondMax = ele;
    }
  }
  console.log(secondMax);
}
