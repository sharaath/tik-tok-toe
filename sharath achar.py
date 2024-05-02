li = [0, 0, 0, 0, 0, 0, 0, 0, 0]
def board():
  count = 0
  for x in range(3):
    print("\n+---+---+---+")
    print("|", end="")
    for y in range(3):
      if li[count]==0:
        print(" "+str(count+1),  end=" |")
      else:
        print(" "+li[count], end=" |")
      count+=1
  print("\n+---+---+---+")

def swap_users():
  if globals()['user'] =="X":
    globals()['user'] = "O"
  else:
    globals()['user'] = "X"

def win():
  # rows
  if( (li[0]=="X" and li[1]=="X" and li[2]=="X") or (li[0]=="O" and li[1]=="O" and li[2]=="O")):
    return False

  if(( li[3]== "X" and li[4]=="X" and li[5]=="X")or( li[3]== "O" and li[4]=="O" and li[5]=="O")) :
    return False

  if(( li[6]=="X" and li[7]=="X" and li[8]=="X") or( li[6]=="O" and li[7]=="O" and li[8]=="O") ):
    return False
  # cols
  if(( li[0]== "X" and li[3]=="X" and li[6]=="X")or( li[0]== "O" and li[3]=="O" and li[6]=="O")) :
    return False
  if(( li[1]== "X" and li[4]=="X" and li[7]=="X")or( li[1]== "O" and li[4]=="O" and li[7]=="O")) :
    return False
  if(( li[2]== "X" and li[5]=="X" and li[8]=="X")or( li[2]== "O" and li[5]=="O" and li[8]=="O")) :
    return False
  #diag
  if(( li[0]== "X" and li[4]=="X" and li[8]=="X")or( li[0]== "O" and li[4]=="O" and li[8]=="O")) :
    return False
  if(( li[2]== "X" and li[4]=="X" and li[6]=="X")or( li[2]== "O" and li[4]=="O" and li[6]=="O")) :
    return False

def full():
  for i in li:
    if i==0:
      return False
  return True
      

board()
user = "X"
game = True
while game:
  n = int(input("Enter the Selection: "))
  li[n-1]=user
  board()
  if win()==False:
    if user=="X":
      print("X won the game")
    else: 
      print("O won the game")
    break   
  if full()==True:
    print("The game is drawn")
    break
  swap_users()
