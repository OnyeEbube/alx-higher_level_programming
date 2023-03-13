#!/usr/bin/node
/*
 * A script that prints two arguments passed to it, in the following format: “ is ”
 */
const myVar = process.argv;
console.log(myVar[2] + ' is ' + myVar[3]);
