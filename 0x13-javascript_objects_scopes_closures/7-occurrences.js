#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let total = 0;
  for (const i of list) {
    if (i === searchElement) {
      total++;
    }
  }
  return total;
};
