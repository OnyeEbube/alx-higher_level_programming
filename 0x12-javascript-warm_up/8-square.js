#!/usr/bin/node
/*
 * A script that prints a square
 * The first argument is the size of the square
 * If the first argument can’t be converted to an integer, print “Missing size”
 * You must use the character X to print the square
 */
const myVar = process.argv[2]
if ((!(myVar)) || (!(parseInt(myVar)))) {
  console.log('Missing size');
} else {
  let x;
  let y;
  for (x = 0; x < (parseInt(myVar)); x++) {
    let i;
    i = '';
    for (y = 0; y < (parseInt(myVar)); y++) {
      i = i + 'X';
    }
    console.log(i);
  }
}
