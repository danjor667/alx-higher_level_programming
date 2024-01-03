#!/usr/bin/node

const fs = require('fs');

function callback (error) {
  if (error) {
    console.log(`${error}`);
  }
}

function writeText (file, text) {
  fs.writeFile(file, text, callback);
}

if (process.argv.length === 4) {
  const file = process.argv[2];
  const text = process.argv[3];
  writeText(file, text);
}
