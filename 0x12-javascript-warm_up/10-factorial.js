#!/usr/bin/node

const arg = process.argv[2];
let num;

if (!isNaN(arg)) {
	num = parseInt(arg);
} else {
	console.log(1);
	process.exit();
}

function factorial(num) {
	if (num === 0 || num === 1)
	{
		return 1;
	} else {
		return num * factorial(num - 1);
	}
}

const result = factorial(num);

console.log(result);
