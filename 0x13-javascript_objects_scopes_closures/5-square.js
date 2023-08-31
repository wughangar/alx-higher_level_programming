#!/usr/bin/node

class Square extends require('./4-rectangle') {
  constructor (size) {
    super(size, size);
    this.size = size;
  }
}

module.exports = Square;
