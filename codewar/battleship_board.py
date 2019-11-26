def solution(N, S, T):
    board = []
    ships = S.split(",")
    shots = T.split(" ")

    for x in range(0,N):
        board.append(["O"] * N)
        
    hit = "x"
    ship_numbers = set()
    
    for ship in ships:
        points = ship.split(' ')
        for point in points:
            y = ord(point[-1].upper()) - 65
            print(y)
            ship_number = int(point[0:point.index(point[-1])])
            x = ship_number-1
            board[x][y] = str(int(point[0]))
            ship_numbers.add(ship_number)
    
    for shot in shots:
        print(shot)
        y = ord(shot[-1].upper()) - 65
        ship_number = int(shot[0:shot.index(shot[-1])])
        x = ship_number-1
        value = board[x][y]
        if value != "O":
            board[x][y] = str(ship_number)+hit
       
    hit_ship_numbers = set()
            
    for row in board:
        for value in row:
            if value == "O":
                continue
            if value.find(hit) != -1:
                number = value[0:value.index(hit)]
                hit_ship_numbers.add(number)
                continue
            number = value[0]
            if int(number) in ship_numbers:
                ship_numbers.remove(int(number))
    
    sunk = len(ship_numbers)
    hit_not_sunk = len(hit_ship_numbers) - sunk
    result = str(sunk) + "," + str(hit_not_sunk)
    
    return result


if __name__ == "__main__":
    print(solution(3, "1A 1B,2C 2C","1B"))
    print(solution(4, "1B 2C,2D 4D","2B 2D 3D 4D 4A"))
    print(solution(12, "1A 2A,12A 12A","12A"))