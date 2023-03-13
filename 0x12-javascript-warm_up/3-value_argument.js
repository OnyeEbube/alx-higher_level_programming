#!/usr/bin/node
/*
 * A script that prints the first argument passed to it:
 * If no arguments are passed to the script, print “No argument”
 */
const argc = process.argv
if (!argc[2]) {
  console.log('No argument')
} else {
  console.log(argc[2])
}
