#!/usr/bin/node

exports.converter = function (base) {
  return function (temp) {
    return temp.toString(base);
  };
};
