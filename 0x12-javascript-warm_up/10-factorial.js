#!/usr/bin/node
const x = process.argv[2];

function factorial (x) {
  if (!x) {
    return (1);
  }
  if (x == 1) {
    return (1);
  }
  return (x * factorial(x - 1));
}

console.log(factorial(parseInt(x)));
