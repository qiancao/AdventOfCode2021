import numpy as np
import itertools
from functools import reduce

WINSCORE = 21
startPositionPtrs = [x-1 for x in [4,8]] #[x-1 for x in [10,9]] # ptrs to starting positions
playerNames = [str(x) for x in range(1,3)]

makePlayer = lambda pos, name: type("Player",(object,),{"ptr": pos, # ptr to trackArr
                                                        "score": 0,
                                                        "name": name})
makeDie = lambda: type("Die",(object,),{"ptr": 0, # ptr to dieArr
                                        "rolls": 0})

trackArr = np.arange(10)+1
dieArr = np.arange(3)+1
sumN = 3 # sum three die rolls at a time

def roll(die):
    inds = range(die.ptr,die.ptr+sumN)
    shift = np.sum(dieArr.take(inds, mode="wrap"))
    die.ptr += sumN
    die.rolls += sumN
    return shift

def move(player, die):
    shift = roll(die)
    player.ptr = ((player.ptr+shift) % len(trackArr)) # could use arr.take here as well
    player.score += trackArr[player.ptr]
    # print(f"Player {player.name} rolls {shift} and moves to space {trackArr[player.ptr]} for a total score of {player.score}.")
    return player.score

players = [makePlayer(x,y) for x,y in zip(startPositionPtrs, playerNames)]
die = makeDie()
endGame = False
while True:
    for player in players:
        score = move(player, die)
        if score >= WINSCORE:
            endGame = True
            break
    if endGame:
        break
    
print(np.min([x.score for x in players])*die.rolls)