#!/usr/bin/node

const arg = process.argv[2];
let num;

if (!isNaN(arg)) {
  num = parseInt(arg);
} else {
  console.log('Missing size');
}

for (let i = 0; i < num; i++) {
  let row = '';
  for (let j = 0; j < num; j++) {
    row += 'X';
  }
  console.log(row);
}
