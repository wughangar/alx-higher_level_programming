#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const filePath = process.argv[3];

request.get(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    process.exit(1);
  }

  if (response.statusCode !== 200) {
    console.error('Error: Failed to fetch the webpage. Status code:', response.statusCode);
    process.exit(1);
  }

  fs.writeFile(filePath, body, 'utf8', (writeError) => {
    if (writeError) {
      console.error('Error writing to the file:', writeError);
      process.exit(1);
    }
  });
});
