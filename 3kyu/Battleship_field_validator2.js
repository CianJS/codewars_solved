/*
https://www.codewars.com/kata/571ec81d7e8954ce1400014f/python

Argument is guaranteed to be 10*10 two-dimension array. Elements in the array are numbers, 0 if the cell is free and 1 if occupied by ship.

Before the game begins, players set up the board and place the ships accordingly to the following rules:
- There must be single battleship (size of 4 cells), 2 cruisers (size 3), 3 destroyers (size 2) and 4 submarines (size 1). Any additional ships are not allowed, as well as missing ships.
- Each ship must be a straight line, except for submarines, which are just single cell.
- The ship cannot overlap, but can be contact with any other ship.
*/

function validateBattlefield2(field) {
  const fieldSize = field.length;
  const maxX = field.length;
  const maxY = field[0].length;
  const ships = {
    4: 1,
    3: 2,
    2: 3,
    1: 4,
  };
  const dx = [0, 1, -1, 0, 0];
  const dy = [0, 0, 0, 1, -1];
  const shipLocationList = [];
  for (let row = 0; row < fieldSize; row++) {
    for (let col = 0; col < fieldSize; col++) {
      const queue = [];
      const shipLocation = [];
      if (field[row][col] === 1) queue.push([row, col]);
      while (queue.length > 0) {
        const [m, n] = queue.shift();
        for (let i = 0; i < dx.length; i++) {
          const nx = m + dx[i];
          const ny = n + dy[i];
          if (nx < 0 || nx >= maxX || ny < 0 || ny >= maxY) continue;
          if (field[nx][ny] === 1) {
            field[nx][ny] = 2; // 방문 처리
            queue.push([nx, ny]);
            shipLocation.push([nx, ny]);
          }
        }
      }
      if (shipLocation.length > 0) shipLocationList.push(shipLocation);
    }
  }
  if (shipLocationList.flatMap((v) => v).length !== 20) return false;

  function getRemoveShipIndexRange(shipLocList, shipSize) {
    shipLocList.sort((a, b) => a[1] - b[1]);
    if ([1, 2].includes(shipLocList.length)) return shipLocList.length;
    let direction;
    for (let i = 0; i < shipSize - 1; i++) {
      const [firstShipX, firstShipY] = shipLocList[i];
      const [secondShipX, secondShipY] = shipLocList[i + 1];
      if (!direction) {
        // is X?
        if (
          !direction &&
          firstShipY === secondShipY &&
          firstShipX < secondShipX
        ) {
          direction = 'x';
        }
        // is Y?
        if (
          !direction &&
          firstShipX === secondShipX &&
          firstShipY < secondShipY
        ) {
          direction = 'y';
        }
        if (!direction) return 1;
      }
      if (
        direction === 'x' &&
        (firstShipY !== secondShipY || firstShipX !== secondShipX - 1)
      ) {
        return i + 1;
      }
      if (
        direction === 'y' &&
        (firstShipX !== secondShipX || firstShipY !== secondShipY - 1)
      ) {
        return i + 1;
      }
    }
    return shipSize;
  }
  return shipLocationList.every((shipLocs) => {
    while (shipLocs.length > 0) {
      let maxShipSize = 4;
      for (let i = maxShipSize; i > 0; i--) {
        if (shipLocs.length >= i) {
          const removeRange = getRemoveShipIndexRange(shipLocs, i);
          if (ships[removeRange] <= 0) return false;
          shipLocs.splice(0, removeRange);
          ships[removeRange] -= 1;
          i = 4;
        }
      }
    }
    return true;
  });
}

const test1 = [
  [1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
  [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
  [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
  [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
  [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]; // true

const test2 = [
  [1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
  [1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
  [1, 1, 0, 0, 1, 1, 1, 0, 1, 0],
  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
  [1, 0, 0, 0, 1, 1, 1, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]; // true

const test3 = [
  [1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
  [1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
  [1, 1, 0, 0, 1, 1, 1, 0, 1, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
  [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
  [0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
  [0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]; // false

const test4 = [
  [1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
  [1, 1, 0, 0, 0, 0, 0, 0, 1, 0],
  [1, 1, 0, 0, 1, 1, 1, 0, 1, 0],
  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
  [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]; // true

const test5 = [
  [1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
  [1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
  [1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
  [1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
  [1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]; // true

console.log(validateBattlefield2(test5));
