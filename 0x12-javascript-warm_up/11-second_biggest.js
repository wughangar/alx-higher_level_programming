#!/usr/bin/node

const arg = process.argv.slice(2);

if (arg.length === 0 || arg.length == 1) {
	console.log(0);
} else {
	function secondLast(numbers) {
		let first = -Infinity;
		let second = -Infinity;
		let x;
		for (x of numbers) {
			if (x > first) {
				second = first;
				first = x;
			} else if (x > second && x !== first) {
				second = x;
			}
		}
		return second;
}

const ans = secondLast(arg);
console.log(ans);
}
