#!/usr/bin/node
exports.esrever = function (list) {
  let newList = [];
  let y = list.length - 1;
  while (y >= 0) {
    newList.push(list[y]);
    y--;
  }
  return (newList);
};
