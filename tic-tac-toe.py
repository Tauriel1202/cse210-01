#Assignment Name: Tic-Tac-Toe! Author: Courtney M. Christensen --> Github Name: Tauriel1202

turnCount = 1
spaces = [1,2,3,4,5,6,7,8,9]
odd = [1,3,5,7,9]
even = [2,4,6,8]  

def board():
  print(f'{spaces[0]}|{spaces[1]}|{spaces[2]}\n-+-+-\n{spaces[3]}|{spaces[4]}|{spaces[5]}\n-+-+-\n{spaces[6]}|{spaces[7]}|{spaces[8]}')

def turn(turnCount):
  ask = int(input('Which tile would you like? Please input a number: '))-1

  if type(spaces[ask]) == str:
    print('This tile is already taken. Please choose an open tile. ')
    ask = int(input('Which tile would you like? Please input a number: '))-1

  else:
    if turnCount in odd:
      spaces[ask] = 'x'

    elif turnCount in even:
      spaces[ask] = 'o'
    
def player(turnCount):
  print(f'Turn: {turnCount}')
  if turnCount in odd:
    print("Player X's Turn!")
  
  if turnCount in even:
    print("Player O's turn!")
  
def rowWin():
  for i in range(0,9,3):
    for j in 'xo':
      if spaces[i] == j and spaces[i+1] == j and spaces[i+2] == j:
        winStatement(j.upper())
   
    else:
      pass

def columnWin():
  for i in range(0,3,1):
    for j in 'xo':
      if spaces[i] == j and spaces[i+3] == j and spaces[i+6] == j:
        winStatement(j.upper())
      else:
        pass

def diagWin():
  for i in 'xo':
    if spaces[0] == i and spaces[4] == i and spaces[8] == i:
      winStatement(i.upper())
    elif spaces[2] == i and spaces[4] == i and spaces[6] == i:
      winStatement(i.upper())

def winStatement(player):
  board()
  print(f'{player} wins!')
  quit()

def win():
  rowWin()
  columnWin()
  diagWin()

def main():
  global turnCount

  while win() != 1 and turnCount < 10:
    board()
    player(turnCount)
    turn(turnCount)
    turnCount += 1
    win()
  else:
    print('It is a draw!')

if __name__ == '__main__':
  main()

