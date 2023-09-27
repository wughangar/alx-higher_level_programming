#!/usr/bin/node

const request = require('request');

const movieID = process.argv[2];

const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieID}`;

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    process.exit(1);
  }

  if (response.statusCode !== 200) {
    console.error('Error: Failed to fetch movie data. Status code:', response.statusCode);
    process.exit(1);
  }

  try {
    const movieData = JSON.parse(body);
    console.log(`${movieData.title}`);
  } catch (parseError) {
    console.error('Error parsing API response:', parseError);
    process.exit(1);
  }
});
