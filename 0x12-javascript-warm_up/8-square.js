#!/usr/bin/node

let size;
if (!isNaN(parseInt(process.argv[2]))) {
  size = parseInt(process.argv[2]);
  if (size > 0) {
    const figure = 'X'.repeat(size);
    for (let h = 0; h < size; h++) {
      console.log(figure);
    }
  }
} else {
  console.log('Missing size');
}
