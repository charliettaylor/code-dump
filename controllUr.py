import random as rand
import math

board = [
    [0, 0, 0, 0, -1, -1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, -1, -1, 0, 0]
]


def print_board():
    print(board)


def check_win(player) -> bool:
    pass

def sum(dice: list) -> int:
    ''' just adds rolls of dice and returns sum '''
    total = 0
    for num in dice:
        total += num
    return total


def take_turn(turn: int):
    ''' takes turn param to determine whose turn it is '''
    dice = []

    for roll in range(0, 3):
        dice.append(rand.randint(0,1))
    total = sum(dice)

    if total == 0:
        print('Lost a turn!')
    else:
        pass #add logic of moving pieces


def game_logic(steps: int) -> list:
    pass


def start() -> list:
    print("Welcome to the Royal Game of Ur!!!")
    p1 = input("Enter Player 1's name: ")
    p2 = input("Enter Player 2's name: ")
    return [p1, p2]


def game_loop():
    playerNames = start()
    P1 = Player()
    P1.set_name(playerNames[0])
    P2 = Player()
    P2.set_name(playerNames[1])
    
    win = False
    turn = 0
    while not win:
        if turn == 0:
            take_turn(turn)
            turn += 1
        elif turn == 1:
            take_turn(turn)
            turn -= 1


def get_abs_distance(coordinate: list) -> int:
    ''' calculates distance based on position[A,3] '''
    if coordinate[0] == 'A' or coordinate[0] == 'C':
        if coordinate[1] < 5:
            return abs(coordinate[1] - 5)
        else:
            return (12 + abs((coordinate[1] - 9)))
    elif coordinate[0] == 'B':
        return coordinate[1] + 4


def convert_coordinates(coordinate: list) -> list:
    ''' converts A,2 to 0,1 '''
    newCoord = [0,0]
    switch = {
        'A' : 0,
        'B' : 1,
        'C' : 2
    }
    return [switch.get(coordinate[0]), coordinate[1] - 1]


def main():
    pass


class Player:
    score = 0
    name = ''
    pieceCount = 0

    def set_name(self, newName):
        name = newName
    
class Piece():
    position = []
    absDistance = 0