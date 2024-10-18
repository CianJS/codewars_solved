# -*- coding: utf-8 -*-

"""
https://www.codewars.com/kata/571ec81d7e8954ce1400014f/python

Argument is guaranteed to be 10*10 two-dimension array. Elements in the array are numbers, 0 if the cell is free and 1 if occupied by ship.

Before the game begins, players set up the board and place the ships accordingly to the following rules:
- There must be single battleship (size of 4 cells), 2 cruisers (size 3), 3 destroyers (size 2) and 4 submarines (size 1). Any additional ships are not allowed, as well as missing ships.
- Each ship must be a straight line, except for submarines, which are just single cell.
- The ship cannot overlap, but can be contact with any other ship.
"""
from collections import deque

def validate_battlefield2(field):
    field_size = len(field)  # 필드의 크기 (10x10 배열)
    max_x = len(field)  # 필드의 최대 X 값 (열 크기)
    max_y = len(field[0])  # 필드의 최대 Y 값 (행 크기)
    
    # 배의 크기와 갯수를 저장하는 딕셔너리 (전함: 1개, 순양함: 2개, 구축함: 3개, 잠수함: 4개)
    ships = {4: 1, 3: 2, 2: 3, 1: 4}
    
    # 상하좌우와 현재 위치를 나타내는 이동 벡터
    dx = [0, 1, -1, 0, 0]
    dy = [0, 0, 0, 1, -1]
    
    # 각 배의 위치를 저장할 리스트
    ship_location_list = []

    # 필드의 각 좌표를 탐색
    for row in range(field_size):
        for col in range(field_size):
            queue = deque()  # BFS를 위한 큐
            ship_location = []  # 한 배의 좌표를 저장할 리스트
            if field[row][col] == 1:  # 배가 있는 좌표를 찾으면 큐에 추가
                queue.append((row, col))
            while queue:
                m, n = queue.popleft()  # 현재 좌표를 큐에서 꺼냄
                for i in range(len(dx)):  # 상하좌우로 탐색
                    nx = m + dx[i]
                    ny = n + dy[i]
                    if nx < 0 or nx >= max_x or ny < 0 or ny >= max_y:  # 범위 바깥이면 무시
                        continue
                    if field[nx][ny] == 1:  # 배가 있는 좌표일 경우
                        field[nx][ny] = 2  # 방문한 좌표는 2로 표시하여 중복 방지
                        queue.append((nx, ny))  # 연결된 배의 좌표를 큐에 추가
                        ship_location.append((nx, ny))  # 배의 좌표 저장
            if ship_location:
                ship_location_list.append(ship_location)  # 하나의 배가 끝나면 리스트에 저장

    # 모든 배들의 좌표가 합쳐서 정확히 20칸이어야 함 (배의 총 크기 4+6+6+4=20)
    if sum(len(ship) for ship in ship_location_list) != 20:
        return False

    # 배가 올바르게 배치되었는지 검사하는 함수
    def get_remove_ship_index_range(ship_loc_list, ship_size):
        # 좌표를 y 좌표 기준으로 정렬
        ship_loc_list.sort(key=lambda s: s[1])
        
        # 배의 크기가 1이나 2일 경우
        if len(ship_loc_list) in [1, 2]:
            return len(ship_loc_list)
        
        direction = None  # 배의 방향을 저장할 변수
        
        # 배가 일직선으로 배치되었는지 확인
        for i in range(ship_size - 1):
            first_ship_x, first_ship_y = ship_loc_list[i]
            second_ship_x, second_ship_y = ship_loc_list[i + 1]
            if not direction:
                # x 방향으로 연결되었는지 확인
                if first_ship_y == second_ship_y and first_ship_x < second_ship_x:
                    direction = 'x'
                # y 방향으로 연결되었는지 확인
                elif first_ship_x == second_ship_x and first_ship_y < second_ship_y:
                    direction = 'y'
                if not direction:  # 만약 직선으로 배치되지 않았으면 1을 반환
                    return 1
            # x 방향일 때 연결이 끊기면 잘못된 배치
            if direction == 'x' and (first_ship_y != second_ship_y or first_ship_x != second_ship_x - 1):
                return i + 1
            # y 방향일 때 연결이 끊기면 잘못된 배치
            if direction == 'y' and (first_ship_x != second_ship_x or first_ship_y != second_ship_y - 1):
                return i + 1
        return ship_size  # 모든 조건을 통과하면 배의 크기 반환

    # 배의 위치가 규칙에 맞게 배치되었는지 확인
    for ship_locs in ship_location_list:
        while ship_locs:
            max_ship_size = 4  # 최대 크기 4인 배부터 확인
            for i in range(max_ship_size, 0, -1):
                if len(ship_locs) >= i:  # 현재 배의 좌표가 i 이상일 때
                    remove_range = get_remove_ship_index_range(ship_locs, i)  # 올바른 크기로 배치되었는지 확인
                    if ships[remove_range] <= 0:  # 해당 크기의 배가 이미 모두 배치되었다면 False 반환
                        return False
                    del ship_locs[:remove_range]  # 처리된 배 좌표 삭제
                    ships[remove_range] -= 1  # 남은 배 수를 줄임
                    if ship_locs:
                      return True
                    break
    return True  # 모든 배가 규칙에 맞게 배치되었으면 True 반환


if __name__ == "__main__":
    test1 = [
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
    ] # True
    test2 = [
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
    ] # True
    test3 = [
      [1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
      [1, 1, 0, 0, 0, 0, 0, 0, 1, 0],
      [1, 1, 0, 0, 1, 1, 1, 0, 1, 0],
      [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
      [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ] # True
    test4 = [
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
    ] # False
    test5 = [
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
    ] # True
    test6 = [
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
    ] # True
    test7 = [
      [1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
      [1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
      [1, 1, 0, 0, 1, 1, 1, 0, 1, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
      [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
      [0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
      [0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ] # True
    test8 = [
      [1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
      [1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
      [1, 1, 0, 0, 1, 1, 1, 0, 1, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
      [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
      [0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
      [0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ] # False
    print(validate_battlefield(test8))