#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const file = process.argv[3];

request(url, (error, response, content) => {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(file, content, 'utf-8', (error) => {
      if (error) {
        console.log(error);
      }
    });
  }
});
