/*
Before the game begins, players set up the board and place the ships accordingly to the following rules:

There must be single battleship (size of 4 cells), 2 cruisers (size 3), 3 destroyers (size 2) and 4 submarines (size 1). Any additional ships are not allowed, as well as missing ships.
Each ship must be a straight line, except for submarines, which are just single cell.
The ship cannot overlap, but can be contact with any other ship.
*/

function validateBattlefield(field) {
  const maxX = field.length;
  const maxY = field[0].length;
  const queue = [];
  // Arrangement to navigate up, down, left and right, including yourself
  const dx = [0, -1, 1, 0, 0];
  const dy = [0, 0, 0, -1, 1];
  // Array for searching the location of a collision with a combat ship
  const sdx = [-1, -1, -1, 0, 0, 1, 1, 1];
  const sdy = [-1, 0, 1, -1, 1, -1, 0, 1];

  const ship = {
    battleship: 0,
    cruiser: 0,
    destroyer: 0,
    submarine: 0,
  };

  for (let x = 0; x < maxX; x++) {
    for (let y = 0; y < maxY; y++) {
      if ([0, 2].includes(field[x][y])) continue;
      if (field[x][y] === 1) queue.push([x, y]);
      let shipLocation = [];
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

      // validate the ship
      if (shipLocation.length > 1) {
        const xLocOfShip = shipLocation.map((ship) => ship[0]);
        const yLocOfShip = shipLocation.map((ship) => ship[1]);
        if (
          xLocOfShip.every((x) => x === xLocOfShip[0]) ===
          yLocOfShip.every((y) => y === yLocOfShip[0])
        )
          return false;
      }
      // Collision detection with other combat ships
      for (const loc of shipLocation) {
        for (let i = 0; i < sdx.length; i++) {
          const nx = loc[0] + sdx[i];
          const ny = loc[1] + sdy[i];
          if (shipLocation.some((a) => a[0] === nx && a[1] === ny)) continue;
          if (nx < 0 || nx >= maxX || ny < 0 || ny >= maxY) continue;
          if (field[nx][ny] === 1) return false;
        }
      }
      switch (shipLocation.length) {
        case 1:
          ship.submarine += 1;
          break;
        case 2:
          ship.destroyer += 1;
          break;
        case 3:
          ship.cruiser += 1;
          break;
        case 4:
          ship.battleship += 1;
          break;
      }
    }
  }

  if (
    ship.battleship === 1 &&
    ship.cruiser === 2 &&
    ship.destroyer === 3 &&
    ship.submarine === 4
  ) {
    return true;
  }
  return false;
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
  [1, 1, 0, 0, 0, 0, 0, 0, 1, 0],
  [1, 1, 0, 0, 1, 1, 1, 0, 1, 0],
  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
  [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]; // false

const test3 = [
  [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
  [0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 1, 0, 1, 1],
  [0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
  [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 1, 0, 1, 1, 1, 1, 0],
  [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 1, 0, 1, 1, 1, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]; // false

const test4 = [
  [0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
  [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
  [0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
  [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
  [0, 1, 0, 1, 0, 0, 0, 1, 0, 0],
  [0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
  [0, 0, 0, 1, 0, 1, 0, 1, 0, 0],
]; // true

const test5 = [
  [0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
  [0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
  [1, 1, 1, 0, 1, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
  [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
  [1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
  [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]; // true

const test6 = [
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
]; // false

const test7 = [
  [1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
  [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
  [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
  [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
  [0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]; // false

const test8 = [
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
];

console.log(validateBattlefield(test8));
