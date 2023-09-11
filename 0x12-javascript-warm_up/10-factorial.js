#!/usr/bin/node

const i = parseInt(process.argv[2]);

function factorial (i) {
  if (i === 0 || isNaN(i)) {
    return 1;
  }
  return i * factorial(i - 1);
}
console.log(factorial(i));
