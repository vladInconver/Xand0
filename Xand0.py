list = list(range(1,10))

def game_window(list):
   for i in range(3):
      print("|", list[0 + i * 3], "|", list[1 + i * 3], "|", list[2 + i * 3], "|")

def move_player(player):
   valid = False
   while not valid:
      answer = input("Куда поставим " + player+"? (Введите число в промежутке 1-9) ")
      try:
         answer = int(answer)
      except:
         print("Вы уверены, что ввели число?")
         continue
      if answer >= 1 and answer <= 9:
         if(str(list[answer-1]) not in "XO"):
            list[answer-1] = player
            valid = True
         else:
            print("Клетка занята!")
      else:
        print("Введите число от 1 до 9.")

def victory(list):
   coords = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
   for coord in coords:
       if list[coord[0]] == list[coord[1]] == list[coord[2]]:
          return list[coord[0]]
   return False

def main(list):
    counter = 0
    win = False
    while not win:
        game_window(list)
        if counter % 2 == 0:
           move_player("X")
        else:
           move_player("O")
        counter += 1
        if counter > 4:
           player = victory(list)
           if player:
              print(player, "победил!")
              win = True
              break
        if counter == 9:
            print("Ничья")
            break
    game_window(list)
main(list)

input("Нажмите Enter игра закончена")
