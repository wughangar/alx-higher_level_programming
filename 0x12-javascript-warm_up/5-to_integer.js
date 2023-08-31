#!/usr/bin/node

const arg = process.argv[2];

if (!isNaN(arg)) {
  const args = parseInt(arg);
  console.log('My number: ' + args);
} else {
  console.log('Not a number');
}
