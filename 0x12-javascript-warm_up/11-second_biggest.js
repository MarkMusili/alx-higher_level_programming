#!/usr/bin/node
const list = process.argv.slice(2).map(Number);

if (list.length <= 1) {
  console.log(0);
} else {
  const maxNum = Math.max(...list);
  const index = list.indexOf(maxNum);
  list.splice(index, 1);

  const secondMax = Math.max(...list);
  console.log(secondMax);
}
