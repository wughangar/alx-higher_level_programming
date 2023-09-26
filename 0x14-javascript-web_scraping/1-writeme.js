#!/usr/bin/node

const fs = require('fs');

if (process.argv.length < 4) {
  console.error('Usage: node write-file.js <file-path> <content>');
  process.exit(1);
}

const filePath = process.argv[2];
const content = process.argv[3];

fs.writeFile(filePath, content, 'utf8', (err) => {
  if (err) {
    console.error('Error writing to file:', err);
    process.exit(1);
  }
});
