#!/usr/bin/node

function myFunction (x, theFunction) {
  for (let i = x; i > 0; i--) {
    theFunction();
  }
}

module.exports = myFunction;
