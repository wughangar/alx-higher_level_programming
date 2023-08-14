#!/usr/bin/node

const arg = process.argv[2];
let x = 0;

if (!isNaN(arg)) {
  x = parseInt(arg);
} else {
  console.log('Missing number of occurrences');
}
while (x > 0) {
  console.log('C is fun');
  x--;
}
