#!/usr/bin/node

const request = require('request');

request('https://swapi-api.hbtn.io/api/films/' + process.argv[2], function (err, res, body) {
  if (err) throw err;
  const characters = JSON.parse(body).characters;
  displayCharactersInOrder(characters, 0);
});

const displayCharactersInOrder = (characters, index) => {
  if (index === characters.length) return;
  request(characters[index], function (err, res, body) {
    if (err) throw err;
    console.log(JSON.parse(body).name);
    displayCharactersInOrder(characters, index + 1);
  });
};
