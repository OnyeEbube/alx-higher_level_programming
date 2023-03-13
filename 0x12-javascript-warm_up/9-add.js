#!/usr/bin/node
/* A script that prints the addition of 2 integers
 * The first argument is the first integer
 * The second argument is the second integer
 * You have to define a function with this prototype: function add(a, b)
 */
const a = parseInt(process.argv[2]);
const b = parseInt(process.argv[3]);
function add(a, b) {
  let sum = a + b;
  return (sum);
}
console.log(add(a, b));
