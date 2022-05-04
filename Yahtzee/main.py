#Programmer: Jonathan Swardson
#Email: jswardson@cnm.edu
#Purpose: Play A Game of Yahtzee
#Version: 3.9.7

from random import randrange
import pygame
from SpriteSheet import SpriteSheet


pygame.init()

class Dice:
   def  __init__(self, number, image):
       self. number = number
       self.image = image


class Ticket():
    def __init__(self, image, renderTag, used):
        self. renderTag = renderTag
        self.image = image
        self.used = used
    
#Functions
def DisplayStartDice(diceToRoll, offsetX, offsetY):
    blitImages.clear()
    numbers.clear()
    diceScores.clear()
    
    pygame.mixer.Sound.play(rollSound)

    turns = maxTurns
    
    for i in range(diceToRoll):
        dice = diceArray[randrange(0, 5)]
   
        blitImage = screen.blit(dice.image, (i * 85 + offsetX, 0 + offsetY))
        dicePos[blitImage.x] = dice.number
        
        blitImages.append(blitImage)

def RollSelectedDice(selectedDice):
    for d in selectedDice:
        dice = diceArray[randrange(0, 5)]
        blitImage = screen.blit(dice.image, (d.x, 630))

        dicePos[d.x] = dice.number

    diceSelected.clear()

def Submit(dicePosArray):
    global gameWon
    for dp in dicePosArray:
        diceScores.append(dicePos[dp])

    CheckScore(diceScores)
    DisplayStartDice(5, 290, 630)

    diceSelected.clear()

    if gameWon == False:
        pygame.display.flip()
        pygame.draw.rect(screen, (226, 160, 116), (0, 0, 1080, 600))
        Notify("Score: " + str(playerScore), (255, 255, 255), 0, 0)
        DisplayTickets(tickets, 920, 90)

    if fullHouse == True and threeOfAKind == True and fourOfAKind == True and smallStraight == True and largeStraight == True:
        gameWon = True

def Notify(message, color, x, y):
    notification = gameFont.render(message, True, color)

    screen.blit(notification, (x, y))
    pygame.display.update()

def CheckScore(results):
    numberArray = results
    global fullHouse
    global threeOfAKind
    global fourOfAKind
    global smallStraight
    global largeStraight

    global playerScore
    global ticketRemove

    for n in results:
        numbers.append(results.count(n))
        
    newNumbers = sorted(numberArray)
    newNumbers = list(set(newNumbers))

    if 5 in numbers:
        playerScore += 50
        pygame.mixer.Sound.play(submitSound)
    elif 2 in numbers and 3 in numbers and fullHouse == False:
        fullHouse = True
        playerScore += 25

        tickets[0].renderTag = "opaque"
        
        pygame.mixer.Sound.play(submitSound)
    elif len(newNumbers) == 4 and smallStraight == False:
        smallStraight = True

        
        tickets[3].renderTag = "opaque"

        
        playerScore += 30
        pygame.mixer.Sound.play(submitSound)
    elif len(newNumbers) == 5 and largeStraight == False:
        largeStraight = True

        tickets[4].renderTag = "opaque"
        
        playerScore += 40
        pygame.mixer.Sound.play(submitSound)
    elif 4 in numbers and 1 in numbers and fourOfAKind == False:
        fourOfAKind = True

        tickets[2].renderTag = "opaque"
        
        playerScore += 10
        pygame.mixer.Sound.play(submitSound)
    elif 3 in numbers and not 2 in numbers and threeOfAKind == False:
        threeOfAKind = True

        tickets[1].renderTag = "opaque"
        
        playerScore += 15
        pygame.mixer.Sound.play(submitSound)
    else:
        pygame.mixer.Sound.play(errorSound)

def DisplayTickets(tickets, x, y):
     for t in tickets:
        if t.renderTag == "render":
             screen.blit(t.image, (x, y * tickets.index(t)))
        elif t.renderTag == "opaque":
            screen.blit(t.used, (x, y * tickets.index(t)))
            print()
        
        
#Screen
(width, height) = (1080, 720)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Yahtzee")

 #Available Rolls
fullHouse = False
threeOfAKind = False
fourOfAKind = False
smallStraight = False
largeStraight = False
    
#Variables
playerScore = 0

gameWon = False
fillScreen = True

diceScores = []
blitImages = []
numbers = []

dicePos = {
    290:"tbd",
    375:"tbd",
    460:"tbd",
    545:"tbd",
    630:"tbd"
    }

pos = [
    290,
    375,
    460,
    545,
    630
    ]

#Roll Tickets
ticketImage = pygame.image.load('Assets/Tickets.png')
ticketSheet = SpriteSheet(ticketImage)

ticketCrossed = pygame.image.load('Assets/TicketsX.png')
ticketCrossedSheet = SpriteSheet(ticketCrossed)

ticketSize = 1

tickets = [
    Ticket(ticketSheet.GetImage(0, 157, 83, ticketSize, (255, 255, 255)), "render", ticketCrossedSheet.GetImage(0, 157, 83, ticketSize, (255, 255, 255))),
    Ticket(ticketSheet.GetImage(1, 157, 83, ticketSize, (255, 255, 255)), "render", ticketCrossedSheet.GetImage(1, 157, 83, ticketSize, (255, 255, 255))),
    Ticket(ticketSheet.GetImage(2, 157, 83, ticketSize, (255, 255, 255)), "render", ticketCrossedSheet.GetImage(2, 157, 83, ticketSize, (255, 255, 255))),
    Ticket(ticketSheet.GetImage(3, 157, 83, ticketSize, (255, 255, 255)), "render", ticketCrossedSheet.GetImage(3, 157, 83, ticketSize, (255, 255, 255))),
    Ticket(ticketSheet.GetImage(4, 157, 83, ticketSize, (255, 255, 255)), "render", ticketCrossedSheet.GetImage(4, 157, 83, ticketSize, (255, 255, 255)))
    ]

#Audio
submitSound =  pygame.mixer.Sound("Assets/Submit.wav")
diceClick = pygame.mixer.Sound("Assets/click_02.wav")
rollSound =  pygame.mixer.Sound("Assets/DiceRoll.wav")
errorSound =  pygame.mixer.Sound("Assets/error.wav")

gameFont = pygame.font.SysFont('Hectiva.ttf', 72)
maxTurns = 2
turns = 0

#UI Variables
uiImage = pygame.image.load('Assets/UI.png').convert_alpha()
uiSheet = SpriteSheet(uiImage)  

submitButton = uiSheet.GetImage(0, 163, 83, 1, (255, 255, 255))
rerollButton = uiSheet.GetImage(1, 163, 83, 1, (255, 255, 255))

#Dice
diceSelected = []
diceImage = pygame.image.load('Assets/Dice.png').convert_alpha()
diceSheet = SpriteSheet(diceImage)
diceSize = 1
diceColor = (240, 240, 255)
diceArray = [
             Dice(1, diceSheet.GetImage(0, 83, 83, diceSize, diceColor)),
             Dice(2, diceSheet.GetImage(1, 83, 83, diceSize, diceColor)),
             Dice(3, diceSheet.GetImage(2, 83, 83, diceSize, diceColor)),
             Dice(4, diceSheet.GetImage(3, 83, 83, diceSize, diceColor)),
             Dice(5, diceSheet.GetImage(4, 83, 83, diceSize, diceColor)),
             Dice(6, diceSheet.GetImage(5, 83, 83, diceSize, diceColor))
            ]   


#Music
pygame.mixer.music.load('Assets/hotel.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.3)


#Set Up Basic Elements
screen.fill((226, 160, 116))

#UI
pygame.draw.rect(screen, (168, 120, 88), (0, 628, 1080, 88), 0, 3)
Notify("Score: " + str(playerScore), (255, 255, 255), 0, 0)

pygame.display.flip()

#Submit Button
sb = screen.blit(submitButton, (718, 630))

#Tickets
DisplayTickets(tickets, 920, 90)

#Reroll Button
rb = screen.blit(rerollButton, (120, 630))

DisplayStartDice(5, 290, 630)

pygame.display.update()

#Game Logic
while True:
    if gameWon == True:
        if fillScreen == True:
            screen.fill((226, 160, 116))
            fillScreen = False

        Notify("Game Over", (255, 255, 255), 440, 300)
        Notify("Score: " + str(playerScore), (255, 255, 255), 440, 360)
    
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            for dice in blitImages:
                if dice.collidepoint(pygame.mouse.get_pos()):                 
                    diceClick.set_volume(0.2)
                    pygame.mixer.Sound.play(diceClick)
                    diceSelected.append(dice)

            if rb.collidepoint(pygame.mouse.get_pos()):
                if turns == maxTurns:
                    pygame.mixer.Sound.play(errorSound)
                elif not diceSelected:
                    pygame.mixer.Sound.play(errorSound)
                elif turns < maxTurns:
                    turns += 1
                    pygame.mixer.Sound.play(rollSound) 
                    RollSelectedDice(diceSelected)
                    pygame.display.update()

            if sb.collidepoint(pygame.mouse.get_pos()):
                Submit(dicePos)
                diceClick.set_volume(0.2)
                pygame.mixer.Sound.play(rollSound) 

                turns = 0
                pygame.display.update()
                
        if event.type == pygame.QUIT:
            False
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                gameWon = True
        

