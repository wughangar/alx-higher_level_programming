#!/usr/bin/node

const args = process.argv.slice(2);

if (args.length === 0) {
  console.log('No arguments');
} else if (args.length === 1) {
  console.log('Agument found');
} else {
  console.log('Arguements found');
}
