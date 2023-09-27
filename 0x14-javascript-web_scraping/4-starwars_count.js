#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    process.exit(1);
  }
  if (response.statusCode !== 200) {
    console.error('Error: Failed to fetch character data. Status code:', response.statusCode);
    process.exit(1);
  }
  try {
    const moviesData = JSON.parse(body).results;
    const characterID = 18;

    const numberOfMovies = moviesData.filter(movie =>
      movie.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterID}/`)
    ).length;

    console.log(`${numberOfMovies}`);
  } catch (parseError) {
    console.error('Error parsing API response:', parseError);
    process.exit(1);
  }
});
