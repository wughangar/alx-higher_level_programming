#!/usr/bin/node

const orgList = require('./100-data').list;

const newList = orgList.map((num, index, orglist) => {
	return num * index;
});

console.log(orgList);
console.log(newList);
