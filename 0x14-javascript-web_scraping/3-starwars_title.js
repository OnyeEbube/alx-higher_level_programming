#!/usr/bin/node

const request = require('request');
const starWars = 'https://swapi-api.alx-tools.com/api/films/';
const movieId = process.argv[2];
const url = starWars + movieId + '/';

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    console.log(`${data.title}`);
  }
});
