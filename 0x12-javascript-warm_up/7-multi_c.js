#!/usr/bin/node
/*
 * A script that prints x times “C is fun”
 * Where x is the first argument of the script
 * If the first argument can’t be converted to an integer, print “Missing number of occurrences”
 */
const myVar = parseInt(process.argv[2]);
if (!myVar) {
  console.log('Missing number of occurrences');
} else {
  let i;
  for (i = 0; i < myVar; i++) {
    console.log('C is fun');
  }
}
