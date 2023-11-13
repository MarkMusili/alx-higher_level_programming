#!/usr/bin/node
const list = process.argv.slice(2);

if (list.length <= 1) {
  console.log(0);
} else {
  const num = Math.max(...list);
  console.log(num);
}
