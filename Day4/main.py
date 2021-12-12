from dataclasses import dataclass, field
import copy

@dataclass
class BingoBoard:
   board: list[list] = field(default_factory=list)

filename = "./input.txt"
with open(filename, "r") as f:
    content = f.read()
   
WinningNumbers = content.split("\n")[0]

def CreateRow(row):
    result = [x.strip() for x in row.split(' ')]
    for counter,i in enumerate(result):
        if i == '':
            result.pop(counter)
    return result

def CalcuateBoard(Board, WinningNumber):
    SumOfBoard = 0
    for item in Board:  
        # [] goes through the board list by row if any number is -1 will switch it to 0
        SumOfBoard = SumOfBoard + (sum([0 if i == -1 else int(i) for i in item]))
    print(WinningNumber)
    print(SumOfBoard)
    print("Answer")
    return SumOfBoard * int(WinningNumber)




def CheckBoard():
 for ItemWinningNum in WinningNumbers.split(','):
  for ItemCompleteBoard in range(len(CompleteBoard)):
   for RowCompleteBoard in range(len(CompleteBoard[ItemCompleteBoard])):
     
     if ItemWinningNum in CompleteBoard[ItemCompleteBoard][RowCompleteBoard]: 
          CompleteBoard[ItemCompleteBoard][RowCompleteBoard] = [-1 if x==ItemWinningNum 
                        else x for x in CompleteBoard[ItemCompleteBoard][RowCompleteBoard]]
          Board = CompleteBoard[ItemCompleteBoard]

          for x in range(5):
           if Board[0][x] == -1 and Board[1][x] == -1 and Board[2][x] == -1 and Board[3][x] == -1 and Board[4][x] == -1:
              print(CalcuateBoard(Board, ItemWinningNum))
              return True
           elif Board[x][0] == -1 and Board[x][1] == -1 and Board[x][2] == -1 and Board[x][3] == -1 and Board[x][4] == -1:
              print(CalcuateBoard(Board, ItemWinningNum))
              return True
 return False

bingoboard = BingoBoard()
CompleteBoard = []
for counter, item in enumerate(content.split("\n")):
    if counter > 1:
        if item == "":
            # need to use the copy function something to do with refernces
            #that if you clear it will stay stuck on the last value
            CompleteBoard.append(bingoboard.board.copy())
            bingoboard.board.clear()
        else:
            bingoboard.board.append(CreateRow(item))

CompleteBoard.append(bingoboard.board.copy())

CheckBoard()