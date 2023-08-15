#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
	let total = 0;
	for (let i of list) {
		if (i === searchElement) {
			total++;
		}
	}
	return total;
};
