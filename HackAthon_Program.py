
# .lower, makes everything lowercase!!
#Not applicable for two players yet 

import RPi.GPIO as GPIO # configures the GPIO ipnts
GPIO.setmode(GPIO.BOARD)
import time
GPIO.setup(12,GPIO.IN)
GPIO.setup(11,GPIO.IN)
player1 = GPIO.input(12)
player2 = GPIO.input(11)
turn = 0



print('Welcome to Family, or in this case, Dual Feud!')
player_1 = input('Player 1, What is your name?')
print(GPIO.input(11))
player_2 = input('Player 2, What is your name?')
print('Ok, we have '+ player_1 + ' and ' + player_2 + '!')
print('Come on down!!!')
print()


def Categories():
  category = ['HBCU Culture', 'Songs', 'Celebrity Drama', 'Memes']

  print(*category, sep = ', ')

def Questions(player_1, player_2):

  point_1 = 0
  point_2 = 0
  print('The first category is HBCU Culture')
  print()
  ques = [ ('What is Morgan State\'s mascot?', 'bear'), ('Who is the real HU?', 'howard university'), ('What is the one song they play at every, and I mean every, HBCU?', 'swag surf')]
  # Stuff for buzzer for player 1 or player 2 
  try:
    while True:
      #GPIO.output(7, GPIO.input(11) )
      time.sleep(.1)
      print(GPIO.input(12))
      if (GPIO.input(11) == 1):
        print(player_1 + ' buzzed in first!')
     
        for i in ques:
          ans = input(i[0]) 
          if ans.lower() == i[1]:
            point_1 += 100 
            print('You got it right!')
          else :
            point_1 -= 20 
            print('You got it wrong!')
            print(player_2 + ' can now guess!')
            ans = input(i[0]) 
            if ans.lower() == i[1]:
              point_2 += 100 
              print('You got it right!')
            else :
              point_2 -= 20 
              print('You got it wrong!')
        break
      if (GPIO.input(12) == 1):
        print(player_2 + ' buzzed in first!')
        for i in ques:
          ans = input(i[0]) 
          if ans.lower() == i[1]:
            point_2 += 100 
            print('You got it right!')
          else :
            point_2 -= 20 
            print('You got it wrong!')
            print(player_1 + ' can now guess!')
            ans = input(i[0])
            if ans.lower() == i[1]:
              point_1 += 100 
              print('You got it right!')
            else :
              point_1 -= 20 
              print('You got it wrong!')
        break
  except KeyboardInterrupt:
      GPIO.cleanup()
  
    


  print('The second category is Songs')
  print()
  ques = [('Who made the song \'Stir Fry\'?', 'migos') , ('What does Playboi Carti call himself?', 'a rockstar'), ('Who is the best new female rapper?', 'cardi b')]
  # Stuff for buzzer for player 1 or player 2
  try:
    while True:
          #GPIO.output(7, GPIO.input(11) )
      time.sleep(.1)
      print(GPIO.input(12))
      if(GPIO.input(11) == 1):
        print(player_1 + ' buzzed in first!')
         
        for i in ques:
          ans = input(i[0]) 
          if ans.lower() == i[1]:
            point_1 += 100 
            print('You got it right!')
          else :
            point_1 -= 20 
            print('You got it wrong!')
            print(player_2 + ' can now guess!')
            ans = input(i[0]) 
            if ans.lower() == i[1]:
              point_2 += 100 
              print('You got it right!')
            else :
              point_2 -= 20 
              print('You got it wrong!')
        break
        if(GPIO.input(12) == 1):
          print(player_2 + ' buzzed in first!')
          for i in ques:
            ans = input(i[0]) 
            if ans.lower() == i[1]:
              point_2 += 100 
              print('You got it right!')
            else :
              point_2 -= 20 
              print('You got it wrong!')
              print(player_1 + ' can now guess!')
              ans = input(i[0])
              if ans.lower() == i[1]:
                point_1 += 100 
                print('You got it right!')
              else :
                point_1 -= 20 
                print('You got it wrong!')
        break
  except KeyboardInterrupt:
    GPIO.cleanup()

        
  
  print('The next category is Celebrity Drama')
  print()
  ques = [('Who did Cardi B get the knot from?', 'nicki minaj'), ('Which rapper recently died from an overdose?', 'mac miller'), ('What popular sitcom father just got sentenced for multiple rape charges?', 'bill cosby')]
  try:
    while True:
      #GPIO.output(7, GPIO.input(11) )
      time.sleep(.1)
      print(GPIO.input(12))
      if (GPIO.input(11) == 1):
        print(player_1 + ' buzzed in first!')
     
        for i in ques:
          ans = input(i[0]) 
          if ans.lower() == i[1]:
            point_1 += 100 
            print('You got it right!')
          else :
            point_1 -= 20 
            print('You got it wrong!')
            print(player_2 + ' can now guess!')
            ans = input(i[0]) 
            if ans.lower() == i[1]:
              point_2 += 100 
              print('You got it right!')
            else :
              point_2 -= 20 
              print('You got it wrong!')
        break
      if (GPIO.input(12) == 1):
        print(player_2 + ' buzzed in first!')
        for i in ques:
          ans = input(i[0]) 
          if ans.lower() == i[1]:
            point_2 += 100 
            print('You got it right!')
          else :
            point_2 -= 20 
            print('You got it wrong!')
            print(player_1 + ' can now guess!')
            ans = input(i[0])
            if ans.lower() == i[1]:
              point_1 += 100 
              print('You got it right!')
            else :
              point_1 -= 20 
              print('You got it wrong!')
        break
  except KeyboardInterrupt:
      GPIO.cleanup()
  print ('The next and last category for the game is.....Memes')
  print()
  ques = [('Which meme was popular in 2012?', 'pepe'), ('Which Wild N Out star has the most popular meme?', 'conceited'), ('What was the stupidest and most toxic meme in 2017?', 'tide pods')]
   # Stuff for buzzer for player 1 or player 2
  try:
    while True:
      #GPIO.output(7, GPIO.input(11) )
      time.sleep(.1)
      print(GPIO.input(12))
      if (GPIO.input(11) == 1):
        print(player_1 + ' buzzed in first!')
     
        for i in ques:
          ans = input(i[0]) 
          if ans.lower() == i[1]:
            point_1 += 100 
            print('You got it right!')
          else :
            point_1 -= 20 
            print('You got it wrong!')
            print(player_2 + ' can now guess!')
            ans = input(i[0]) 
            if ans.lower() == i[1]:
              point_2 += 100 
              print('You got it right!')
            else :
              point_2 -= 20 
              print('You got it wrong!')
        break
      if (GPIO.input(12) == 1):
        print(player_2 + ' buzzed in first!')
        for i in ques:
          ans = input(i[0]) 
          if ans.lower() == i[1]:
            point_2 += 100 
            print('You got it right!')
          else :
            point_2 -= 20 
            print('You got it wrong!')
            print(player_1 + ' can now guess!')
            ans = input(i[0])
            if ans.lower() == i[1]:
              point_1 += 100 
              print('You got it right!')
            else :
              point_1 -= 20 
              print('You got it wrong!')
        break
  except KeyboardInterrupt:
      GPIO.cleanup()
  if point_1 > point_2:
      print(player_1 + ' has won the game with ' + str(point_1) + ' points!')
  else:
      print(player_2 + ' has won the game with ' + str(point_2) + ' points!')
  
 

Categories()
Questions(player_1, player_2)



  

