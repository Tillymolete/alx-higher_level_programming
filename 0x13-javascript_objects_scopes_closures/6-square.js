#!/usr/bin/node
const SquareG = require('./5-square');

class Square extends SquareG {
  charPrint (c = 'X') {
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
