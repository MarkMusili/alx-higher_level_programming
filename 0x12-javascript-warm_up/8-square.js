#!/usr/bin/node
const x = process.argv[2];
try {
  const num = parseInt(x);

  if (isNaN(num)) {
    throw new Error('Missing size');
  }
  for (let i = 0; i < num; i++) {
    let square = '';
    for (let j = 0; j < num; j++) {
      square += 'X';
    }
    console.log(square);
  }
} catch (err) {
  console.log(err.message);
}
