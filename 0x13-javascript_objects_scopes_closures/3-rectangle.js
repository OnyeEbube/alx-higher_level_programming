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

  print() {
    for (let i = 0; i < height; i++) {
      let myVar = '';
      for (let j = 0; j < width; j++) {
        myVar = myVar + 'X';
      }
      console.log(myVar);
    }
  }
}
module.exports = Rectangle;
