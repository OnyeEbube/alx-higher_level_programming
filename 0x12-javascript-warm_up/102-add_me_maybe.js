#!/usr/bin/node
/*
 * A function that increments and calls a function
 * The function must be visible from outside
 * Prototype: function (number, theFunction)
 */
exports.addMeMaybe = function (number, theFunction) {
  theFunction(++number);
};
