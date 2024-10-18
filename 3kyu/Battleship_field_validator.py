# -*- coding: utf-8 -*-

"""
Before the game begins, players set up the board and place the ships accordingly to the following rules:
- There must be single battleship (size of 4 cells), 2 cruisers (size 3), 3 destroyers (size 2) and 4 submarines (size 1). Any additional ships are not allowed, as well as missing ships.
- Each ship must be a straight line, except for submarines, which are just single cell.
- The ship cannot overlap or be in contact with any other ship, neither by edge nor by corner.
"""

# broken logic
def validate_battlefield(battleField):
    total_cell = 20
    positioning = []

    for grid_idx, grid in enumerate(battleField):
        for idx, value in enumerate(grid):
            if value:
                positioning.append((grid_idx, idx))

    if total_cell != len(positioning):
        return False

    row = {'row': True}
    col = {'col': True}
    idx = 0
    while idx < len(positioning):
        if not positioning:
            break
        if idx == -1:
            idx = 0

        cell = positioning[idx]
        # Returns false if it is an edge.
        if (cell[0] - 1, cell[1] - 1) in positioning:
            return False
        if (cell[0] + 1, cell[1] - 1) in positioning:
            return False
        if (cell[0] - 1, cell[1] + 1) in positioning:
            return False
        if (cell[0] + 1, cell[1] + 1) in positioning:
            return False

        if (cell[0] + 1, cell[1]) in positioning:
            if col.get(cell[1]):
                col[cell[1]].append(cell)
            else:
                col[cell[1]] = [cell]

            if not ((cell[0] + 2, cell[1]) in positioning):
                col[cell[1]].append((cell[0] + 1, cell[1]))
                positioning.remove((cell[0] + 1, cell[1]))

            positioning.pop(idx)
            idx -= 1
        elif (cell[0], cell[1] + 1) in positioning:
            if row.get(cell[0]):
                row[cell[0]].append(cell)
            else:
                row[cell[0]] = [cell]

            if not ((cell[0], cell[1] + 2) in positioning):
                row[cell[0]].append((cell[0], cell[1] + 1))
                positioning.remove((cell[0], cell[1] + 1))

            positioning.pop(idx)
            idx -= 1
        else:
            idx += 1

    number_of_submarines_found = len(positioning)
    print(col, '/', row, '/', positioning)
    ships = {4: 1, 3: 2, 2: 3, 1: 4}

    def check_number_of_ship(data):
        row = data.get('row')
        col = data.get('col')

        if row:
            data.pop('row')
        if col:
            data.pop('col')

        for k, lt in data.items():
            executed = False
            ship_range = len(lt)

            tmp = 0
            is_first = True
            for i, v in enumerate(lt):
                if is_first:
                    is_first = False
                    continue

                if ship_range == i + 1 and not executed:
                    break
                if row:
                    if (v[0], v[1] - 1) == lt[i - 1]:
                        if i + 1 != len(lt):
                            if (v[0], v[1] + 1) == lt[i + 1]:
                                continue
                        executed = True
                        checked_ship_range = len(lt[tmp:i + 1])
                        if checked_ship_range:
                            tmp = i + 1
                            ships[checked_ship_range] = ships.get(checked_ship_range) - 1
                if col:
                    if (v[0] - 1, v[1]) == lt[i - 1]:
                        if i + 1 != len(lt):
                            if (v[0] + 1, v[1]) == lt[i + 1]:
                                continue
                        executed = True
                        checked_ship_range = len(lt[tmp:i + 1])
                        print(checked_ship_range)
                        if checked_ship_range:
                            tmp = i + 1
                            ships[checked_ship_range] = ships.get(checked_ship_range) - 1

                # 세로버전 제작 필요.
            if executed:
                continue

            if ship_range == 5:
                ship_range = ship_range - 1
                ships[1] -= 1
            ships[ship_range] = ships.get(ship_range) - 1

        return True

    row_result = check_number_of_ship(row)
    col_result = check_number_of_ship(col)
    ships[1] = ships.get(1) - number_of_submarines_found
    bat, cur, des, sub = ships.items()

    print(row_result, col_result, ships, (bat[1], cur[1], des[1], sub[1]) == (0, 0, 0, 0))
    if row_result and col_result and (bat[1], cur[1], des[1], sub[1]) == (0, 0, 0, 0):
        return True
    else:
        return False

if __name__ == "__main__":
    test1 = [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
             [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
             [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
             [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
             [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]] # this test is vaild.
    test2 = [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
             [1, 1, 0, 0, 0, 0, 0, 0, 1, 0],
             [1, 1, 0, 0, 1, 1, 1, 0, 1, 0],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
             [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    test3 = [[0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
             [0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 1, 0, 1, 1],
             [0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
             [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 1, 0, 1, 1, 1, 1, 0],
             [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 1, 0, 1, 1, 1, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    test4 = [[0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
             [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
             [0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
             [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
             [0, 1, 0, 1, 0, 0, 0, 1, 0, 0],
             [0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
             [0, 0, 0, 1, 0, 1, 0, 1, 0, 0]]

    test5 = [[0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
             [0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
             [1, 1, 1, 0, 1, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
             [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
             [1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
             [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    test6 = [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
             [1, 1, 0, 0, 0, 0, 0, 0, 1, 0],
             [1, 1, 0, 0, 1, 1, 1, 0, 1, 0],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
             [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    print(validate_battlefield(test3))
