#!/usr/bin/node
const x = process.argv[2];
try {
  const num = parseInt(x);

  if (isNaN(num)) {
    throw new Error('Missing number of occurrences');
  }
  for (let i = 0; i < num; i++) {
    console.log('C is fun');
  }
} catch (err) {
  console.log(err.message);
}
