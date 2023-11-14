#!/usr/bin/node
const list = process.argv.slice(2).map(Number);

if (list.length <= 1) {
  console.log(0);
} else {
  const max_num = Math.max(...list);
  const index = list.indexOf(max_num);
  list.splice(index, 1);

  const second_max = Math.max(...list);
  console.log(second_max);
}
