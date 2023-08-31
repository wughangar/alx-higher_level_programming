#!/usr/bin/node

const arg = process.argv;
function add (a, b) {
  console.log(parseInt(a) + parseInt(b));
}

if (arg.length >= 4) {
  add(arg[2], arg[3]);
} else {
  console.log('NaN');
}
