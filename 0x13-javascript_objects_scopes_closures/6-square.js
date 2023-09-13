#!/usr/bin/node
const OldSquare = require('./5-square');
class Square extends OldSquare {
    constructor (size) {
        super(size, size);
    }

    charPrint (c = 'X') {
        const fig = c.repeat(this.width);
        for (let i = 0; i < this.height; i++) {
            console.log(fig);
        }
    }

}
module.exports = Square;