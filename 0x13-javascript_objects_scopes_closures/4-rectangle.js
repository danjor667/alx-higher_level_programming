#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if ((typeof w) !== 'number' || typeof h !== 'number' || w <= 0 || h <= 0) {
      // pass

    } else {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const fig = 'X'.repeat(this.width);
    for (let i = 0; i < this.height; i++) {
      console.log(fig);
    }
  }

  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }

  double () {
    this.width = 2 * this.width;
    this.height = 2 * this.height;
  }
}
module.exports = Rectangle;
