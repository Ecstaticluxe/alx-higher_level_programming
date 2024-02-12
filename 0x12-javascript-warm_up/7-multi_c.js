#!/usr/bin/node

const [,, x] = process.argv;
const num = parseInt(x);

if (!isNaN(num)) {
  for (let i = 0; i < num; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
