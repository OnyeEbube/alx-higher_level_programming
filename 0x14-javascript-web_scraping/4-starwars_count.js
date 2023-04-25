#!/usr/bin/node

const request = require('request');
const starWars = process.argv[2];
const basicId = '18';
let count = 0;

request.get(starWars, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    data.results.forEach((film) => {
      film.characters.forEach((character) => {
        if (character.includes(basicId)) {
          count += 1;
        }
      });
    });
    console.log(count);
  }
});
