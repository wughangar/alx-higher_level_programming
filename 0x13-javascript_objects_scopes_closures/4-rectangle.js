#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || typeof w !== 'number' || typeof h !== 'number') {
      return {};
    }
    this.width = w;
    this.height = h;
  }

  print () {
    for (let rows = 0; rows < this.height; rows++) {
      let printStr = '';
      for (let col = 0; col < this.width; col++) {
        printStr += 'X';
      }
      console.log(printStr);
    }
  }

  // exchanges the width and height of the rectangle
  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  // multiplies the theight and width by 2
  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
