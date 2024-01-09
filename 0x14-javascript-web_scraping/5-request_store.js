#!/usr/bin/node

const request = require('request');

const fs = require('fs');

const filename = process.argv[3];

const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    fs.writeFile(filename, body, 'utf-8', (err) => {
      if (err) {
        console.error(error);
      }
    });
  }
});
