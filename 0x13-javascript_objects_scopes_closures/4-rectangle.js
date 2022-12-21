#!/usr/bin/node
/**
 * Prints a rectangle
 */
class Rectangle {
  constructor (w, h) {
    if (typeof w === 'number' && w > 0 && typeof h === 'number' && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let myVar = '';
      for (let j = 0; j < this.width; j++) {
        myVar = myVar + 'X';
      }
      console.log(myVar);
    }
  }

  rotate () {
    let x = 0;
    x = this.width;
    this.width = this.height;
    this.height = x;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}
module.exports = Rectangle;
