#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

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
    const characterName = 'Wedge Antilles';
    const movies = movieData.results;

    const numberOfMovies = movies.filter(movie =>
      movie.characters.some(character => character.includes(characterName))
    ).length;

    console.log(`${numberOfMovies}`);
  } catch (parseError) {
    console.error('Error parsing API response:', parseError);
    process.exit(1);
  }
});
