#!/usr/bin/node

let message;
const arg = process.argv.length;
if (arg <= 2) {
  message = 'No argument';
} else if (arg === 3) {
  message = 'Argument found';
} else {
  message = 'Arguments found';
}
console.log(message);
