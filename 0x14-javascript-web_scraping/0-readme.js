#!/usr/bin/node

const fs = require('fs');

if (process.argv.length < 3) {
  console.error(' Usage: node read-file.js <file-path>');
  process.exit(1);
}

const filePth = process.argv[2];

fs.readFile(filePth, 'utf8', (err, data) => {
  if (err) {
    console.error('Error reading file:', err);
    process.exit(1);
  }
  console.log(data);
});
