#!/usr/bin/node

const arg = process.argv;
const a = arg[2];
const b = arg[3];

function add (a, b) {
  const result = parseInt(a) + parseInt(b);
  console.log(result);
}
add(a, b);
