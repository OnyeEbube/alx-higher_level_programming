#!/usr/bin/node
const size = process.argv[2];

if (!parseInt(size)){
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
    let myVar = '';
    for (let j = 0; j < size; j++) {
      myVar = myVar + 'X';
    }
    console.log(myVar);
  }
}
