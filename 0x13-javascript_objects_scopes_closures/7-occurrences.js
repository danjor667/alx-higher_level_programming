#!/usr/bin/node
function nbOccurences (nums, num) {
  let count = 0;
  for (const ele of nums) {
    if (ele === num) {
      count++;
    }
  }
  return count;
}
module.exports = { nbOccurences };
