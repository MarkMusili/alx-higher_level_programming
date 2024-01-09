#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const movies = JSON.parse(body);

    const filmsWithWedge = movies.results.filter((film) =>
      film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')
    );
    console.log(`${filmsWithWedge.length}`);
  }
});
