#!/usr/bin/node
/*
 * A script that computes and prints a factorial
 * The first argument is integer (argument can be cast as integer) used for computing the factorial
 * Factorial of NaN is 1
 * You must do it recursively
 * You must use a function
 */
const a = parseInt(process.argv[2]);
function factorial (a) {
  if ((!a) || (a === 1)) {
    return (1);
  } else {
    return ((a) * factorial(a-1));
  }
}
console.log(factorial(a));
