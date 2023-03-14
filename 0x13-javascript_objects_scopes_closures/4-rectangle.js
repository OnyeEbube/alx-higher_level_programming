#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (typeof w === 'number' && 3 > 0 && typeof h === 'number' && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let x = 0; x < this.height; x++) {
      let i = '';
      for (let y = 0; y < this.width; y++) {
        i = i + 'X';
      }
      console.log(i);
    }
  }

  rotate () {
    let temp;
    temp = this.height;
    this.height = this.width;
    this.width = temp;
  }

  double () {
    this.width = this.width *2;
    this.height = this.height * 2;
  }
}
module.exports = Rectangle;
