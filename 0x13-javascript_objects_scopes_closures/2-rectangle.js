#!/usr/bin/node
/**
 * Defines a rectanglw with height and width
 */
class Rectangle {
  constructor (w, h) {
    if (typeof w === 'number' && w > 0 && typeof h === 'number' && h > 0) {
      this.weight = w;
      this.height = h;
    }
  }
}
module.exports = Rectangle;
