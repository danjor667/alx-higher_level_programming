#!/usr/bin/node
exports.converter = function (base) {
  return function otherFunction (number) {
    return Number(number).toString(base);
  };
};
// exports.otherFunction = function (number, base) {
//    return Number(number).toString(base);
// }
