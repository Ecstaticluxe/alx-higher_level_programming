#!/usr/bin/node

function factorial(n) {
	if (isNaN(parseInt(n))) {
		return 1; // Factorial of NaN is 1
	}
	n = parseInt(n);

	if (n === 0 || n === 1) {
		return (1);
	} else {
		return n * factorial(n - 1);
	}
}

const input = process.argv[2];
console.log(factorial(input));
