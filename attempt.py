




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
#import library
import pygame
import random

#define color
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)


(width, height) = (700, 600)
FPS = 60

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((width, height))
screen.fill(white)
pygame.display.flip()
pygame.display.set_caption("Duo Feud")
class Pane(object):
    def __init__(self):
        pygame.init()
        self.font = pygame.font.SysFont('Arial', 25)
        pygame.display.set_caption('Box Test')
        self.screen = pygame.display.set_mode((width, height), 0, 32)
        self.screen.fill((white))
        pygame.display.update()
    def addRect(self):
        self.rect = pygame.draw.rect(self.screen, (black), (45, 500,90,30), 2)
        self.rect1 = pygame.draw.rect(self.screen, (black), (495,500,90,30), 2)
        self.rect2 = pygame.draw.rect(self.screen, (black), (295,50,100,30), 2)
        pygame.display.update()
    def addText(self):
        self.screen.blit(self.font.render('Player 1', True, (200,0,0)), (50,500,80,20))
        self.screen.blit(self.font.render('Player 2', True, (200,0,0)), (500,500,80,30))
        self.screen.blit(self.font.render('Duo Feud', True, (200,0,0)), (300,50,150,30))
        pygame.display.update()
if __name__ == '__main__':
    Pan3 = Pane()
    Pan3.addRect()
    Pan3.addText()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit();
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = FALSE





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


pygame.quit()






  


