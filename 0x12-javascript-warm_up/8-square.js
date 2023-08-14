#!/usr/bin/node

const arg = process.argv[2];
let num;

if (!isNaN(arg)) {
  num = parseInt(arg);
} else {
  console.log('Missing size');
}

for (let i = 1; i < num; i++) {
  let row = 'X';
  for (let j = 1; j < num; j++) {
    row += 'X';
  }
  console.log(row);
}
