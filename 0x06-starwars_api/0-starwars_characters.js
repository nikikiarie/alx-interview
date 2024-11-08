#!/usr/bin/node
const request = require('request');
const idMovie = process.argv[2];
const requestOptions = {
  url: 'https://swapi-api.hbtn.io/api/films/' + idMovie,
  method: 'GET'
};

// Fetches the film details using the film ID
request(requestOptions, function (error, response, body) {
  if (!error) {
    const characterUrls = JSON.parse(body).characters;
    fetchAndPrintCharacters(characterUrls, 0);
  }
});

function fetchAndPrintCharacters (characterUrls, currentIndex) {
  // Requests and logs each character's name in sequence
  request(characterUrls[currentIndex], function (error, response, body) {
    if (!error) {
      console.log(JSON.parse(body).name);
      if (currentIndex + 1 < characterUrls.length) {
        fetchAndPrintCharacters(characterUrls, currentIndex + 1);
      }
    }
  });
}
