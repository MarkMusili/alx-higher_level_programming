#!/usr/bin/node
const num = process.argv[2];

function factorial (n) {
  if (isNaN(n)) {
    return 1;
  }

  let res = 1;
  while (n > 0) {
    res *= n;
    n--;
  }
  return res;
}
console.log(factorial(num));
