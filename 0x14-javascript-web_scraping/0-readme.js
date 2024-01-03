#!/usr/bin/node

const fs = require('fs');

function callback (error, data) {
  if (error) {
    console.log(`${error}`);
  } else {
    console.log(`${data}`);
  }
}

function readFile (file) {
  fs.readFile(file, callback);
}

if (process.argv.length === 3) {
  const file = process.argv[2];
  readFile(file);
}
