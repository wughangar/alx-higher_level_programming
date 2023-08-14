#!/usr/bin/node

const arg = process.argv[2];
let num = 0;

if (!isNaN(arg)) {
  num = parseInt(arg);
} else {
  console.log('Missing size');
}

for (let i = 0; i < num; i++) {
  let row = 'X';
  for (let j = 0; j < num; j++) {
    row += 'X';
  }
  console.log(row);
}
