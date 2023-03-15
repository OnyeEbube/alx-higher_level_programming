#!/usr/bin/node

exports.logMe = function count (item) {
  console.log(`$(counter): $(item)`);
  counter += 1;
};
