#Term Project:

from cmu_112_graphics import *
import random


def appStarted(app):
    app.spritePhotoImages = loadAnimatedGif('Background.gif')
    app.spriteCounter = 0
    app.unscaled = app.loadImage('Party Template.png')
    app.battleImage = app.scaleImage(app.unscaled,1/2)
    app.unscaledInstruction = app.loadImage('InstructionsBackground.jpg')
    #User Pokemon:
    app.firstPoke = loadAnimatedGif(f'/Users/shreyas/Desktop/15-112/Term Project/Gen 1 Sprites/{gifList[0]}')
    app.firstCounter = 0
    app.secondPoke = loadAnimatedGif(f'/Users/shreyas/Desktop/15-112/Term Project/Gen 1 Sprites/{gifList[1]}')
    app.secondCounter = 0
    app.thirdPoke = loadAnimatedGif(f'/Users/shreyas/Desktop/15-112/Term Project/Gen 1 Sprites/{gifList[2]}')
    app.thirdCounter = 0
    app.fourthPoke = loadAnimatedGif(f'/Users/shreyas/Desktop/15-112/Term Project/Gen 1 Sprites/{gifList[3]}')
    app.fourthCounter = 0
    app.fifthPoke = loadAnimatedGif(f'/Users/shreyas/Desktop/15-112/Term Project/Gen 1 Sprites/{gifList[4]}')
    app.fifthCounter = 0
    app.sixthPoke = loadAnimatedGif(f'/Users/shreyas/Desktop/15-112/Term Project/Gen 1 Sprites/{gifList[5]}')
    app.sixthCounter = 0
    #User Gym Maze Sprite Icon:
    app.userUp = loadAnimatedGif('UserSpriteUp.gif')
    app.userUpCounter = 0
    app.upBool = True
    app.userDown = loadAnimatedGif('UserSpriteDown.gif')
    app.userDownCounter = 0
    app.downBool = False
    app.walkStatus = False
    app.battle = app.loadImage('BattleBackground.jpeg')
    app.battleScreen = app.scaleImage(app.battle, 2/3)
    app.gymImage = app.loadImage('Gym.gif')
    app.gymBool = False
    app.gymLeader = app.loadImage('GymSprite1.png')
    app.gymTrainerOne = app.loadImage('GymSprite2.png')
    app.gymTrainerTwo = app.loadImage('GymSprite3.png')
    app.gx = app.width/2
    app.gy = app.height/2 + 150
    app.cx = 1000
    app.cy = 1000
    app.name = ''
    app.partyScreen = False
    app.firstScreen = True
    app.battleBool = False
    app.instructionScreen = False
    app.modesScreen = False
    app.randomizedParty = []
    app.profTaylor = app.loadImage('mdtaylor.jpg')
    #User Pokemon in battle:
    app.unscaledFirstPoke = app.loadImage(f'/Users/shreyas/Desktop/15-112/Term Project/BackSprites/{backGifList[0]}')
    app.firstBattlePoke = app.scaleImage(app.unscaledFirstPoke, 2)
    app.unscaledSecondPoke = app.loadImage(f'/Users/shreyas/Desktop/15-112/Term Project/BackSprites/{backGifList[1]}')
    app.secondBattlePoke = app.scaleImage(app.unscaledSecondPoke, 2)
    app.unscaledThirdPoke = app.loadImage(f'/Users/shreyas/Desktop/15-112/Term Project/BackSprites/{backGifList[2]}')
    app.thirdBattlePoke = app.scaleImage(app.unscaledThirdPoke, 2)
    app.unscaledFourthPoke = app.loadImage(f'/Users/shreyas/Desktop/15-112/Term Project/BackSprites/{backGifList[3]}')
    app.fourthBattlePoke = app.scaleImage(app.unscaledFourthPoke, 2)
    app.unscaledFifthPoke = app.loadImage(f'/Users/shreyas/Desktop/15-112/Term Project/BackSprites/{backGifList[4]}')
    app.fifthBattlePoke = app.scaleImage(app.unscaledFifthPoke, 2)
    app.unscaledSixthPoke = app.loadImage(f'/Users/shreyas/Desktop/15-112/Term Project/BackSprites/{backGifList[5]}')
    app.sixthBattlePoke = app.scaleImage(app.unscaledSixthPoke, 2)
    #First Opponent Pokemon:
    app.oppFirstPoke = loadAnimatedGif(f'/Users/shreyas/Desktop/15-112/Term Project/Gen 1 Sprites/{oppGifList[0]}')
    app.oppFirstCount = 0
    app.oppSecondPoke = loadAnimatedGif(f'/Users/shreyas/Desktop/15-112/Term Project/Gen 1 Sprites/{oppGifList[1]}')
    app.oppSecondCount = 0
    app.oppThirdPoke = loadAnimatedGif(f'/Users/shreyas/Desktop/15-112/Term Project/Gen 1 Sprites/{oppGifList[2]}')
    app.oppThirdCount = 0
    app.oppFourthPoke = loadAnimatedGif(f'/Users/shreyas/Desktop/15-112/Term Project/Gen 1 Sprites/{oppGifList[3]}')
    app.oppFourthCount = 0
    app.oppFifthPoke = loadAnimatedGif(f'/Users/shreyas/Desktop/15-112/Term Project/Gen 1 Sprites/{oppGifList[4]}')
    app.oppFifthCount = 0
    app.oppSixthPoke = loadAnimatedGif(f'/Users/shreyas/Desktop/15-112/Term Project/Gen 1 Sprites/{oppGifList[5]}')
    app.oppSixthCount = 0
    #Second Opponent Pokemon:
    app.secondOppFirst = loadAnimatedGif(f'/Users/shreyas/Desktop/15-112/Term Project/Gen 1 Sprites/{oppGifList2[0]}')
    app.secondOppFirstCount = 0
    app.secondOppSecond = loadAnimatedGif(f'/Users/shreyas/Desktop/15-112/Term Project/Gen 1 Sprites/{oppGifList2[1]}')
    app.secondOppSecondCount = 0
    app.secondOppThird = loadAnimatedGif(f'/Users/shreyas/Desktop/15-112/Term Project/Gen 1 Sprites/{oppGifList2[2]}')
    app.secondOppThirdCount = 0
    app.secondOppFourth = loadAnimatedGif(f'/Users/shreyas/Desktop/15-112/Term Project/Gen 1 Sprites/{oppGifList2[3]}')
    app.secondOppFourthCount = 0
    app.secondOppFifth = loadAnimatedGif(f'/Users/shreyas/Desktop/15-112/Term Project/Gen 1 Sprites/{oppGifList2[4]}')
    app.secondOppFifthCount = 0
    app.secondOppSixth= loadAnimatedGif(f'/Users/shreyas/Desktop/15-112/Term Project/Gen 1 Sprites/{oppGifList2[5]}')
    app.secondOppSixthCount = 0
    #Gym Leader/Third OpponentPokemon:
    app.leaderFirst = loadAnimatedGif(f'/Users/shreyas/Desktop/15-112/Term Project/Gen 1 Sprites/{oppGifList3[0]}')
    app.leaderFirstCount = 0
    app.leaderSecond = loadAnimatedGif(f'/Users/shreyas/Desktop/15-112/Term Project/Gen 1 Sprites/{oppGifList3[1]}')
    app.leaderSecondCount = 0
    app.leaderThird = loadAnimatedGif(f'/Users/shreyas/Desktop/15-112/Term Project/Gen 1 Sprites/{oppGifList3[2]}')
    app.leaderThirdCount = 0
    app.leaderFourth = loadAnimatedGif(f'/Users/shreyas/Desktop/15-112/Term Project/Gen 1 Sprites/{oppGifList3[3]}')
    app.leaderFourthCount = 0
    app.leaderFifth = loadAnimatedGif(f'/Users/shreyas/Desktop/15-112/Term Project/Gen 1 Sprites/{oppGifList3[4]}')
    app.leaderFifthCount = 0 
    app.leaderSixth = loadAnimatedGif(f'/Users/shreyas/Desktop/15-112/Term Project/Gen 1 Sprites/{oppGifList3[5]}')
    app.leaderSixthCount = 0

    app.trainerIndex = 0
    app.movePick = False
    app.partyPick = False
    app.firstMove = False
    app.secondMove = False
    app.thirdMove = False
    app.fourthMove = False
    app.initialAIIndex = 0
    app.currUserIndex = 0
    app.currOppIndex = 0
    app.bestAIMoveIndex = 0
    app.aliveIndex = [0,1,2,3,4,5]
    app.userDeaths = 0
    app.casual = False
    app.competitive = False
    #User Pokemon/MoveSet
    app.pokeObjList = [createPokemon(team[0])[0],createPokemon(team[1])[0], createPokemon(team[2])[0], createPokemon(team[3])[0], createPokemon(team[4])[0], createPokemon(team[5])[0]]
    app.userMoveObj = [createPokemon(team[0])[1],createPokemon(team[1])[1], createPokemon(team[2])[1], createPokemon(team[3])[1], createPokemon(team[4])[1], createPokemon(team[5])[1]]
    #First Trainer Pokemon/MoveSet
    app.oppPokeObj = [createPokemon(opponentTeam[0])[0],createPokemon(opponentTeam[1])[0], createPokemon(opponentTeam[2])[0], createPokemon(opponentTeam[3])[0], createPokemon(opponentTeam[4])[0], createPokemon(opponentTeam[5])[0]]
    app.oppMoveObj = [createPokemon(opponentTeam[0])[1],createPokemon(opponentTeam[1])[1], createPokemon(opponentTeam[2])[1], createPokemon(opponentTeam[3])[1], createPokemon(opponentTeam[4])[1], createPokemon(opponentTeam[5])[1]]
    #Second Trainer Pokemon/MoveSet
    app.oppPokeObjTwo = [createPokemon(oppTeam2[0])[0],createPokemon(oppTeam2[1])[0], createPokemon(oppTeam2[2])[0], createPokemon(oppTeam2[3])[0], createPokemon(oppTeam2[4])[0], createPokemon(oppTeam2[5])[0]]
    app.oppMoveObjTwo= [createPokemon(oppTeam2[0])[1],createPokemon(oppTeam2[1])[1], createPokemon(oppTeam2[2])[1], createPokemon(oppTeam2[3])[1], createPokemon(oppTeam2[4])[1], createPokemon(oppTeam2[5])[1]]
    #Leader Trainer Pokemon/MoveSet
    app.oppPokeObjThree = [createPokemon(leaderTeam[0])[0],createPokemon(leaderTeam[1])[0], createPokemon(leaderTeam[2])[0], createPokemon(leaderTeam[3])[0], createPokemon(leaderTeam[4])[0], createPokemon(leaderTeam[5])[0]]
    app.oppMoveObjThree = [createPokemon(leaderTeam[0])[1],createPokemon(leaderTeam[1])[1], createPokemon(leaderTeam[2])[1], createPokemon(leaderTeam[3])[1], createPokemon(leaderTeam[4])[1], createPokemon(leaderTeam[5])[1]]

    app.oneParty = True
    app.twoParty = False
    app.threeParty = False
    app.fourParty = False
    app.fiveParty = False
    app.sixParty = False
    app.deadIndex = 1000
    app.oppDeadList = []
    app.bestAIMove = []
    app.oppSwitch = False
    app.userSwitch = False
    app.aliveUser = 0
    app.oneTwelve = False
    app.timerSwitch = False
    app.deadList = []
    app.ctList = ['''def ct1(s, t):
    for c in s:
        if (s.count(c) > 1):]
        t += c
    while (len(t) > 4):
        t = t[0:-1]
    return t
    
    print(ct1('abbdca', '6'))
    
    *This prints a string of one line*''', 
    '''def ct2(L):
    if L == [ ]:
        return [ ]
    elif len(L) % 2 == 0:
        return [L[0]] + ct2(L[1:])
    else:
        return ct2(L[1:]) + [L[0]]
    
    print(ct2([1,2,3,4,5,6]))
    
    *This prints a list of 6 elements*''', 
    '''def ct3(s):
    r = ''
    if len(s) < 6:
        r = 'X'
    for i in range(len(s)):
        if s[i].isupper():
            r = s[i] + r
        elif s[i].isalpha():
            c = chr(ord(s[i])+1)
            r = r + c
        else:
            r = r + str(i)
    return r
    
    print(ct3("r0B0/t"))
    
    *This prints a string of one line*''',
    ''' def ct4(L):
    d = dict()
    for i in range(len(L)):
        for j in range(i+1, len(L)):
            if L[i] == L[j]:
                d[i+j] = i
    return d
    
    print(ct4([2,1,2,3,4,3]))
    
    *This print a dictionary with a length of 2*''',
    ''' def ct5(M):
    rows, cols = len(M), len(M[0])
    result = []
    for row in range(rows):
        for col in range(1, cols):
            M[row][0] += M[row][col]
        result = [M[row][0]] + result
    return result
    
    L = [ [ 1, 2, 3 ], [ 2, 5, 7 ] ]
    print(ct5(L))
    
    *This prints a list of 2 elements*''' ]
    app.randomCT = random.choice(app.ctList)

    #result variable --> If user wins or loses:
    app.result = False
    app.loss = False
    app.win = False


#I got this function for gifs from 
# https://www.cs.cmu.edu/~112/notes/notes-animations-part4.html
def loadAnimatedGif(path):
    # load first sprite outside of try/except to raise file-related exceptions
    spritePhotoImages = [ PhotoImage(file=path, format='gif -index 0') ]
    i = 1
    while True:
        try:
            spritePhotoImages.append(PhotoImage(file=path,
                                                format=f'gif -index {i}'))
            i += 1
        except Exception as e:
            return spritePhotoImages

def timerFired(app):
    #all the sprite/gif animations
    app.spriteCounter = (1 + app.spriteCounter) %  len(app.spritePhotoImages)
    app.firstCounter = (1+ app.firstCounter) %  len(app.firstPoke)-1
    app.secondCounter = (1 + app.secondCounter) %  len(app.secondPoke)-1
    app.thirdCounter = (1 + app.thirdCounter) %  len(app.thirdPoke)-1
    app.fourthCounter = (1 + app.fourthCounter) %  len(app.fourthPoke)-1
    app.fifthCounter = (1 + app.fifthCounter) %  len(app.fifthPoke)-1
    app.sixthCounter = (1 + app.sixthCounter) %  len(app.sixthPoke)-1
    app.oppFirstCount =  (1+ app.oppFirstCount) %  len(app.oppFirstPoke)-1
    app.oppSecondCount =  (1+ app.oppSecondCount) %  len(app.oppSecondPoke)-1
    app.oppThirdCount =  (1+ app.oppThirdCount) %  len(app.oppThirdPoke)-1
    app.oppFourthCount = (1+ app.oppFourthCount) %  len(app.oppFourthPoke)-1
    app.oppFifthCount =  (1+ app.oppFifthCount) %  len(app.oppFifthPoke)-1
    app.oppSixthCount =  (1+ app.oppSixthCount) %  len(app.oppSixthPoke)-1
    app.secondOppFirstCount =  (1+ app.secondOppFirstCount) %  len(app.secondOppFirst)-1
    app.secondOppSecondCount =  (1+ app.secondOppSecondCount) %  len(app.secondOppSecond)-1
    app.secondOppThirdCount =  (1+ app.secondOppThirdCount) %  len(app.secondOppThird)-1
    app.secondOppFourthCount =  (1+ app.secondOppFourthCount) %  len(app.secondOppFourth)-1
    app.secondOppFifthCount =  (1+ app.secondOppFifthCount) %  len(app.secondOppFifth)-1
    app.secondOppSixthCount =  (1+ app.secondOppSixthCount) %  len(app.secondOppSixth)-1
    app.leaderFirstCount = (1+ app.leaderFirstCount) %  len(app.leaderFirst)-1
    app.leaderSecondCount = (1+ app.leaderSecondCount) %  len(app.leaderSecond)-1
    app.leaderThirdCount = (1+ app.leaderThirdCount) %  len(app.leaderThird)-1
    app.leaderFourthCount = (1+ app.leaderFourthCount) %  len(app.leaderFourth)-1
    app.leaderFifthCount = (1+ app.leaderFifthCount) %  len(app.leaderFifth)-1
    app.leaderSixthCount = (1+ app.leaderSixthCount) %  len(app.leaderSixth)-1
    if(app.walkStatus == True):
        app.userUpCounter = (1+ app.userUpCounter) %  len(app.userUp)
        app.userDownCounter = (1+ app.userDownCounter) %  len(app.userDown)
    elif(app.walkStatus == False):
        app.userUpCounter = (1+ app.userUpCounter) %  len(app.userUp)-1
        app.userDownCounter = (1+ app.userDownCounter) %  len(app.userDown)-1
    #Checking for Opponent Team Deaths:
    

def mousePressed(app, event):
    app.cx = event.x
    app.cy = event.y
    if(app.aliveUser == 5):
        if(0 < app.cx < app.width and 320 < app.cy < 390):
            app.oneTwelve = True 
            oneTwelveMove(app,event)
            app.oneTwelve = False
    else:
        if(app.firstScreen == True):
            if(190 < app.cx < 290 and 170 < app.cy < 210):
                app.name = app.getUserInput("What is your name?")
                app.partyScreen = True
                app.firstScreen = False
            if(70 < app.cx < 170 and 170 < app.cy < 210):
                app.instructionScreen = True
                app.firstScreen = False
        elif(app.instructionScreen == True):
            if(260 < app.cx < 315 and 330 < app.cy < 365):
                app.instructionScreen = False
                app.firstScreen = True
        elif(app.partyScreen == True):
            if(260 < app.cx < 330 and 10 < app.cy < 45):
                app.competitive = True
                app.gymBool = True
                app.partyScreen = False
            if(260 < app.cx < 330 and 340 < app.cy < 375):
                app.casual = True
                app.gymBool = True
                app.partyScreen = False
        if(app.movePick == True):
            gameAI(app,event)
            if(app.competitive == True):
                moveIndex = bestAIMove(app,event)
                app.bestAIMoveIndex = moveIndex
            elif(app.casual == True):
                index = casualAIMove(app,event)
                app.bestAIMoveIndex  = index
            fightMouse(app, event)
            app.movePick = False
        elif(app.battleBool == True):
                if(app.width/2 < app.cx < app.width and 320<app.cy<355):
                    app.movePick = True
                if(app.width/2 < app.cx < app.width and 355 < app.cy < 390):
                    app.movePick = False
                    app.partyPick = True
                    app.oneParty = False
                    app.twoParty = False
                    app.threeParty = False
                    app.fourParty = False
                    app.fiveParty = False
                    app.sixParty = False
                    app.battleBool = False
        elif(app.partyPick == True):
            if((app.pokeObjList[0].getHealth() > 0) and (0 < app.cx < app.width/2 and 0 < app.cy < app.height/3)):
                app.oneParty = True
                app.battleBool = True
                app.currUserIndex = 0
            if((app.pokeObjList[1].getHealth() > 0) and (app.width/2 < app.cx < app.width and 0 < app.cy < app.height/3)):
                app.twoParty = True
                app.battleBool = True
                app.currUserIndex = 1
            if((app.pokeObjList[2].getHealth() > 0) and (0 < app.cx < app.width/2 and app.height/3 < app.cy < 2*app.height/3)):
                app.threeParty = True
                app.battleBool = True
                app.currUserIndex = 2
            if((app.pokeObjList[3].getHealth() > 0) and (app.width/2 < app.cx < app.width and app.height/3 < app.cy < 2*app.height/3)):
                app.fourParty = True
                app.battleBool = True
                app.currUserIndex = 3
            if((app.pokeObjList[4].getHealth() > 0) and (0 < app.cx < app.width/2 and 2*app.height/3 < app.cy < app.height)):
                app.fiveParty = True
                app.battleBool = True
                app.currUserIndex = 4
            if((app.pokeObjList[5].getHealth() > 0) and (app.width/2 < app.cx < app.width and 2*app.height/3 < app.cy < app.height)):
                app.sixParty = True
                app.battleBool = True 
                app.currUserIndex = 5
            app.partyPick = False
            app.userSwitch = True
        elif(app.result == True):
            if(260 < app.cx < 315 and 330 < app.cy < 365):
                app.result = False
                app.firstScreen = True
                #If user loses and restarts by pressing the back button, it will reheal all the AI's pokemon
                for i in app.oppPokeObj: 
                    i.heal()
                for x in app.oppPokeObjTwo:
                    x.heal()
                for y in app.oppPokeObjThree:
                    y.heal()
        
#Competetive Game AI
def gameAI(app , event):
    #for AI, loop through all the opponentPokeObjects
    #use .getTypes() on each of them to retrieve types of each OppPoke
    #use .getTypes() to retrieve the type of currPoke
    #Use typeeffectiveness - best template to see which pokemon would do the
    # most "damage"/most type effective
    #switch currOppIndex to that, so Poke switches out
    #If stays the same, loop through moves to see most damage (another function), and use that
    currentPokemon = app.pokeObjList[app.currUserIndex]
    (type1, type2) = currentPokemon.getTypes()
    if(app.trainerIndex == 0):
        currentOppPokeList = app.oppPokeObj
    elif(app.trainerIndex == 1):
        currentOppPokeList = app.oppPokeObjTwo
    elif(app.trainerIndex == 2):
        currentOppPokeList = app.oppPokeObjThree
    (oppType1, oppType2) = currentOppPokeList[app.currOppIndex].getTypes()
    compDamage = 0
    if(oppType1 != '' and oppType2 != ''):
        compDamage = typeEffectiveness(1, oppType1, type1, type2)
        compDamage *= typeEffectiveness(1, oppType2, type1, type2)
    elif(oppType2 == ''):
        compDamage = typeEffectiveness(1, oppType1, type1, type2)
    #loop through all types and see which one is the best for the AI to switch out
    for index in range(0 , len(currentOppPokeList)):
        if(index in app.aliveIndex):    
            (compType1, compType2) = currentOppPokeList[index].getTypes()
            if(compType1 != '' and compType2 != ''):
                damage = typeEffectiveness(1, compType1, type1, type2)
                damage *= typeEffectiveness(1, compType2, type1, type2)
            elif(compType2 == ''):
                damage = typeEffectiveness(1, compType1, type1, type2)
            #bestTemplate
            if(damage > compDamage):
                compDamage = damage
                app.currOppIndex = index
                app.oppSwitch = True
                if(app.trainerIndex == 0):
                    print(f"The AI has switched to {opponentTeam[app.currOppIndex]}")
                elif(app.trainerIndex == 1):
                    print(f"The AI has switched to {oppTeam2[app.currOppIndex]}")
                elif(app.trainerIndex == 2):
                    print(f"The AI has switched to {leaderTeam[app.currOppIndex]}")
    #switched out to best poke - now compare all moves and see which does the most damage
    app.oppSwitch = False

#Competitive mode - AI always picks best move
def bestAIMove(app, event):
    if(app.trainerIndex == 0):
        currOppPoke = app.oppPokeObj[app.currOppIndex]
        possMoves = app.oppMoveObj[app.currOppIndex]
    elif(app.trainerIndex == 1):
        currOppPoke = app.oppPokeObjTwo[app.currOppIndex]
        possMoves = app.oppMoveObjTwo[app.currOppIndex]
    elif(app.trainerIndex == 2):
        currOppPoke = app.oppPokeObjThree[app.currOppIndex]
        possMoves = app.oppMoveObjThree[app.currOppIndex]
    currUserPoke = app.pokeObjList[app.currUserIndex]
    compDamage = 0
    for index in range(0,4):
        damage = currOppPoke.getDamage(currUserPoke, possMoves[index])
        if(damage > compDamage):
            compDamage = damage
            moveIndex = index
    return moveIndex

#Casual Mode - AI picks one random move out of the four

def casualAIMove(app,event):
    if(app.trainerIndex == 0):
        possMoves = app.oppMoveObj[app.currOppIndex]
    elif(app.trainerIndex == 1):
        possMoves = app.oppMoveObjTwo[app.currOppIndex]
    elif(app.trainerIndex == 2):
        possMoves = app.oppMoveObjThree[app.currOppIndex]
    index = random.randint(0,3)
    return index

def oneTwelveMoveDraw(app, canvas):
    canvas.create_rectangle(0, 0, 350, 395, fill = "SteelBlue1")
    canvas.create_text(app.width/2, 45, text = "        Professor Taylor's 112 Move!: \nGet this code tracing right on the first try \nand reduce the opponent's health by half!", font = "Helvetica 16 bold italic", fill = "red")
    canvas.create_text(app.width/4 + 25 , app.height/2, text = app.randomCT, font = "Helvetica 12 ")
    canvas.create_image(270, 160, image = ImageTk.PhotoImage(app.profTaylor))


def oneTwelveMove(app,event):
    index = app.ctList.index(app.randomCT)
    answer = app.getUserInput('What is the answer?')
    if(app.trainerIndex == 0):
        currOppPoke = app.oppPokeObj[app.currOppIndex]
    elif(app.trainerIndex == 1):
        currOppPoke = app.oppPokeObjTwo[app.currOppIndex]
    elif(app.trainerIndex == 2):
        currOppPoke = app.oppPokeObjThree[app.currOppIndex]
    if(index == 0):
        if(answer == '6abb'):
            app.showMessage('You are correct!')
            currOppPoke.oneTwelveReduce()
        else:
            app.showMessage('Sorry, you are incorrect!')
    if(index == 1):
        if(answer == '[1, 3, 5, 6, 4, 2]'):
            app.showMessage('You are correct!')
            currOppPoke.oneTwelveReduce()
        else:
            app.showMessage('Sorry, you are incorrect!')
    if(index == 2):
        if(answer == 'BXs134'):
            app.showMessage('You are correct!')
            currOppPoke.oneTwelveReduce()
        else:
            app.showMessage('Sorry, you are incorrect!')
    if(index == 3):
        if(answer == "{2: 0, 8: 3}"):
            app.showMessage('You are correct!')
            currOppPoke.oneTwelveReduce()
        else:
            app.showMessage('Sorry, you are incorrect!')
    if(index == 4):
        if(answer == '[14, 6]'):
            app.showMessage('You are correct!')
            currOppPoke.oneTwelveReduce()
        else:
            app.showMessage('Sorry, you are incorrect!')
    
    app.aliveUser = 0
    app.battleBool = True
    
def fightMouse(app, event): #deals with the fighting/move aspect and mousePressed
    currName = team[app.currUserIndex]
    moveSet = getMoves(currName,'KantoPokemon.csv')
    deathVar = 0
    deathVar2 = 0
    #Sees which trainer the user is fighting first
    if(app.trainerIndex == 0):
        currOppPoke = app.oppPokeObj[app.currOppIndex]
        currOppMoves = app.oppMoveObj[app.currOppIndex]
    elif(app.trainerIndex == 1):
        currOppPoke = app.oppPokeObjTwo[app.currOppIndex]
        currOppMoves = app.oppMoveObjTwo[app.currOppIndex]
    elif(app.trainerIndex == 2):
        currOppPoke = app.oppPokeObjThree[app.currOppIndex]
        currOppMoves = app.oppMoveObjThree[app.currOppIndex]
    
    if(0 < app.cx < app.width/2 and 320 < app.cy < 355):
        app.firstMove = True
        deathVar = app.pokeObjList[app.currUserIndex].Attack(currOppPoke, app.userMoveObj[app.currUserIndex][0])
        
    if(app.width/2 < app.cx < app.width and 320 < app.cy < 355):
        app.secondMove = True
        deathVar = app.pokeObjList[app.currUserIndex].Attack(currOppPoke, app.userMoveObj[app.currUserIndex][1])
        
    if(0 < app.cx < app.width/2 and 355 < app.cy< app.height):
        app.thirdMove = True
        deathVar = app.pokeObjList[app.currUserIndex].Attack(currOppPoke, app.userMoveObj[app.currUserIndex][2])
        
    if(app.width/2 < app.cx < app.width and 355 < app.cy < app.height):
        app.fourthMove = True
        deathVar = app.pokeObjList[app.currUserIndex].Attack(currOppPoke, app.userMoveObj[app.currUserIndex][3])
    
    if(app.oppSwitch == False):
        deathVar2 =  currOppPoke.Attack(app.pokeObjList[app.currUserIndex], currOppMoves[app.bestAIMoveIndex])

    if(deathVar == 1):
        app.aliveIndex.remove(app.currOppIndex)
        if(len(app.aliveIndex) == 0):
            if(app.trainerIndex == 2): #If user battles the last trainer and WINS, they win the game
                app.result = True
                app.win = True
            else:
                app.gymBool = True
                app.battleBool = False
        else:
            app.currOppIndex = random.choice(app.aliveIndex)

    if(deathVar2 == 1):
        app.userDeaths += 1
        app.aliveUser = 0
        app.movePick = False
        app.oneParty = False
        app.twoParty = False
        app.threeParty = False
        app.fourParty = False
        app.fiveParty = False
        app.sixParty = False
        app.battleBool = False
        if(app.userDeaths == 6):
            app.result = True
            app.loss = True
        else:
            app.partyPick = True
        
    app.aliveUser += 1
    app.firstMove = False
    app.secondMove = False
    app.thirdMove = False
    app.fourthMove = False

def chooseParty(app, canvas):
    canvas.create_rectangle(0, 0, 400, 400, fill = "sky blue")
    canvas.create_line(app.width/2,0, app.width/2, app.height, fill = "black", width = "3")
    canvas.create_line(0, app.height/3, app.width, app.height/3, fill = "black", width = "3")
    canvas.create_line(0, 2*app.height/3, app.width, 2*app.height/3, fill = "black", width = "3")
    im = app.firstPoke[app.firstCounter]
    canvas.create_image(app.width/4, 40, image =im)
    im2 = app.secondPoke[app.secondCounter]
    canvas.create_image(3*app.width/4, 40, image = im2)
    im3 = app.thirdPoke[app.thirdCounter]
    canvas.create_image(app.width/4, app.height/3 + 40, image = im3)
    im4 = app.fourthPoke[app.fourthCounter]
    canvas.create_image(3*app.width/4, app.height/3 + 40, image =im4)
    im5 = app.fifthPoke[app.fifthCounter]
    canvas.create_image(app.width/4, 2*app.height/3 + 40, image = im5)
    im6 = app.sixthPoke[app.sixthCounter]
    canvas.create_image(3*app.width/4, 2*app.height/3 + 40, image =im6)
    #draw health bars for each pokemon
    oneHealth = app.pokeObjList[0].getHealth()
    onePercent = oneHealth/300
    oneAdd = 70 * onePercent
    endGreenOne = 50 + oneAdd
    canvas.create_rectangle(50, 80, endGreenOne, 90, fill = "lime green", outline = "black",
    width = "1")
    canvas.create_rectangle(endGreenOne, 80, 120, 90, fill = "black", outline = "black",
    width = "1")
    canvas.create_text(85, 100, text = f"HP: {oneHealth} / 300", font = "Helvetica 8 bold")

    twoHealth = app.pokeObjList[1].getHealth()
    twoPercent = twoHealth/300
    twoAdd = 70 * twoPercent
    endGreenTwo = 230 + twoAdd
    canvas.create_rectangle(230, 80, endGreenTwo, 90, fill = "lime green", outline = "black",
    width = "1")
    canvas.create_rectangle(endGreenTwo, 80, 300, 90, fill = "black", outline = "black",
    width = "1")
    canvas.create_text(265, 100, text = f"HP: {twoHealth} / 300", font = "Helvetica 8 bold")

    threeHealth = app.pokeObjList[2].getHealth()
    threePercent = threeHealth/300
    threeAdd = 70 * threePercent
    endGreenThree = 50 + threeAdd
    canvas.create_rectangle(50, 210, endGreenThree, 220, fill = "lime green", outline = "black",
    width = "1")
    canvas.create_rectangle(endGreenThree, 210, 120, 220, fill = "black", outline = "black",
    width = "1")
    canvas.create_text(85, 230, text = f"HP: {threeHealth} / 300", font = "Helvetica 8 bold")


    fourHealth = app.pokeObjList[3].getHealth()
    fourPercent = fourHealth/300
    fourAdd = 70 * fourPercent
    endGreenFour = 230 + fourAdd
    canvas.create_rectangle(230, 210, endGreenFour, 220, fill = "lime green", outline = "black",
    width = "1")
    canvas.create_rectangle(endGreenFour, 210, 300, 220, fill = "black", outline = "black",
    width = "1")
    canvas.create_text(265, 230, text = f"HP: {fourHealth} / 300", font = "Helvetica 8 bold")


    fiveHealth = app.pokeObjList[4].getHealth()
    fivePercent = fiveHealth/300
    fiveAdd = 70 * fivePercent
    endGreenFive = 50 + fiveAdd
    canvas.create_rectangle(50, 340, endGreenFive, 350, fill = "lime green", outline = "black",
    width = "1")
    canvas.create_rectangle(endGreenFive, 340, 120, 350, fill = "black", outline = "black",
    width = "1")
    canvas.create_text(85, 360, text = f"HP: {fiveHealth} / 300", font = "Helvetica 8 bold")


    sixHealth = app.pokeObjList[5].getHealth()
    sixPercent = sixHealth/300
    sixAdd = 70 * sixPercent
    endGreenSix = 230 + sixAdd
    canvas.create_rectangle(230, 340, endGreenSix, 350, fill = "lime green", outline = "black",
    width = "1")
    canvas.create_rectangle(endGreenSix, 340, 300, 350, fill = "black", outline = "black",
    width = "1")
    canvas.create_text(265, 360, text = f"HP: {sixHealth} / 300", font = "Helvetica 8 bold")

    
    #draws the moveSet for each pokemon in the party screen
    firstMoveSet = getMoves(team[0], 'KantoPokemon.csv')
    secondMoveSet = getMoves(team[1], 'KantoPokemon.csv')
    thirdMoveSet = getMoves(team[2], 'KantoPokemon.csv')
    fourthMoveSet = getMoves(team[3], 'KantoPokemon.csv')
    fifthMoveSet = getMoves(team[4], 'KantoPokemon.csv')
    sixthMoveSet = getMoves(team[5], 'KantoPokemon.csv')
    canvas.create_text(90, 120, text = f'{firstMoveSet[0], firstMoveSet[1]}\n{firstMoveSet[2], firstMoveSet[3]}', font = "Helvetica 8 bold")
    canvas.create_text(270, 120, text = f'{secondMoveSet[0], secondMoveSet[1]}\n{secondMoveSet[2], secondMoveSet[3]}', font = "Helvetica 8 bold")
    canvas.create_text(90, 250, text = f'{thirdMoveSet[0], thirdMoveSet[1]}\n{thirdMoveSet[2], thirdMoveSet[3]}', font = "Helvetica 8 bold")
    canvas.create_text(270, 250, text = f'{fourthMoveSet[0], fourthMoveSet[1]}\n{fourthMoveSet[2], fourthMoveSet[3]}', font = "Helvetica 8 bold")
    canvas.create_text(90, 380, text = f'{fifthMoveSet[0], fifthMoveSet[1]}\n{fifthMoveSet[2], fifthMoveSet[3]}', font = "Helvetica 8 bold")
    canvas.create_text(270, 380, text = f'{sixthMoveSet[0], sixthMoveSet[1]}\n{sixthMoveSet[2], sixthMoveSet[3]}', font = "Helvetica 8 bold")

def keyPressed(app, event):

    if(event.key == 'Up'):
        app.walkStatus = True
        app.upBool = True
        app.downBool = False
        app.gy -= 5
        if(app.gy == 307.5):
            healAll(app,event) #restores users pokemon back to 300 health
            app.aliveIndex = [0,1,2,3,4,5] #the indexes of all pokemon alive for opposing trainer
            app.userDeaths = 0
            app.currOppIndex = 0
            app.trainerIndex = 0 
            app.gymBool = False
            app.battleBool = True
        if(app.gy == 227.5):
            healAll(app,event) #restores users pokemon back to 300 health
            app.aliveIndex = [0,1,2,3,4,5] #resets the opposing trainer's pokemon to all alive
            app.userDeaths = 0
            app.currOppIndex = 0
            app.trainerIndex = 1
            app.gymBool = False
            app.battleBool = True
        if(app.gy == 97.5):
            healAll(app,event) #restores users pokemon back to 300 health
            app.aliveIndex = [0,1,2,3,4,5] #resets the opposing trainer's pokemon to all alive
            app.userDeaths = 0
            app.currOppIndex = 0
            app.trainerIndex = 2
            app.gymBool = False
            app.battleBool = True
    elif(event.key == 'Down'):
        app.walkStatus = True
        app.downBool = True
        app.upBool = False
        app.gy += 5
        if(app.gy > 375):
            app.gy = app.height/2 + 150
        
    #key pressed- app.walkstatus = true / up --> app.cy +1, app.cx + 1
    #key released - app.walkstatus = False
    #redrawAll - if --> if walkstatus - true --> 

def keyReleased(app,event):
    app.walkStatus = False

#Heals the health back to 100 after each battle for the user's party pokemon
def healAll(app, event):
    for pokemon in app.pokeObjList:
        pokemon.heal()

def redrawAll(app, canvas):
    if(app.firstScreen == True):
        canvas.create_image(200,200,image=app.spritePhotoImages[app.spriteCounter])
        drawfirstScreen(app,canvas)
    if(app.instructionScreen == True):
        drawInstructions(app, canvas)
    if(app.partyScreen == True):
        drawBattleSimulator(app,canvas)
    if(app.battleBool == True):
        drawBattleScreen(app,canvas)
    if(app.partyPick == True):
        chooseParty(app,canvas)
    if(app.oneTwelve == True):
        oneTwelveMoveDraw(app,canvas)
    if(app.gymBool == True):
        drawGymScreen(app,canvas)
    if(app.result == True):
        drawResultScreen(app,canvas)


#def drawSwitch(app,canvas):
    #canvas.create_rectangle(5, 320, 345, 390, fill = "white", outline = "black",
        #width = "5")
    #canvas.create_text(app.width/2, 350, text = f'The AI has switched to {opponentTeam[app.currOppIndex]}')

def drawResultScreen(app,canvas):
    canvas.create_rectangle(0, 0, 400, 400, fill = "gold")
    if(app.win == True):
        canvas.create_text(app.width/2, app.height/2, text = "Congrats! You are the champion\nof Pokémon Showdown 112! :)", font = 'Helvetica 18 bold italic ')
    if(app.loss == True):
        canvas.create_text(app.width/2, app.height/2, text = "You have lost... You can try again\nby pressing the button below!", font = 'Helvetica 18 bold italic')
        canvas.create_rectangle(260, 330, 315 ,365, fill = "red")
        canvas.create_text(287.5, 347.5, text = "BACK", font = "Helvetica 12 bold")

def drawGymScreen(app,canvas):
    canvas.create_image(170,195, image = ImageTk.PhotoImage(app.gymImage))
    canvas.create_image(app.width/2, 85, image = ImageTk.PhotoImage(app.gymLeader))
    canvas.create_image(app.width/2, app.height/2 + 10, image = ImageTk.PhotoImage(app.gymTrainerOne))
    canvas.create_image(app.width/2, app.height/2 + 100, image = ImageTk.PhotoImage(app.gymTrainerTwo))
    if(app.upBool == True):
        canvas.create_image(app.gx, app.gy, image = app.userUp[app.userUpCounter])
    if(app.downBool == True):
        canvas.create_image(app.gx, app.gy, image = app.userDown[app.userDownCounter])

def drawfirstScreen(app, canvas):
    canvas.create_text(180, 120, text = "Pokémon Showdown", fill = "yellow"
    , font = "Helvetica 28 bold italic")
    canvas.create_text(180, 150, text = "Click to start!", fill = "black"
    , font = "Helvetica 14 bold italic")
    canvas.create_rectangle(70, 170, 170, 210, fill = "gold")
    canvas.create_text(120, 190, text = "Instructions", 
    font = "Helvetica 16 bold italic", fill = "black")
    canvas.create_rectangle(190, 170, 290, 210, fill = "gold")
    canvas.create_text(240, 190, text = "    Battle \n Simulator", 
    font = "Helvetica 16 bold italic", fill = "black")

def drawInstructions(app, canvas): 
    canvas.create_rectangle(0, 0, 400, 400, fill = "white")
    canvas.create_image(170,195, image = ImageTk.PhotoImage(app.unscaledInstruction))
    canvas.create_text(app.width/2, 50, text = "INSTRUCTIONS:",
    font = "Helvetica 28 bold italic underline")
    canvas.create_text(app.width/2, 90, text = "Welcome to the world of\nPokémon Showdown 112!",
    font = "Helvetica 14 bold italic", fill = "gold")
    canvas.create_text(app.width/2, 140, text = "This game, like typical Pokémon Showdown, gives\nyou a team of 6 randomized pokémon.\nWith your randomized Pokémon Party, you have to\nbattle the other trainer's set of 6 randomized pokémon",
    font = "Helvetica 12 bold", fill = "red")
    canvas.create_text(app.width/2, 190, text = "Modes/Difficulty:",
    font = "Helvetica 18 bold italic underline")
    canvas.create_text(app.width/2, 240, text = "Casual: The AI is less intelligent. They will randomly\npick one move out of their four moves, but they will\nsmartly switch to their other pokemon based\non type effectiveness",
    font = "Helvetica 12 bold", fill = "red")
    canvas.create_text(app.width/2, 300, text = "Competitive: The AI is INTELLIGENT. They will switch\nout their pokemon based on what could inflict the most\ndamage through a series of calculations! Choose this\nmode if you are an experienced Pokémon trainer!",
    font = "Helvetica 12 bold", fill = "red")
    canvas.create_rectangle(260, 330, 315 ,365, fill = "gold")
    canvas.create_text(287.5, 347.5, text = "BACK", font = "Helvetica 12 bold")

#Party Screen that shows all pokemon
def drawBattleSimulator(app,canvas):
    canvas.create_rectangle(0, 0, 1000, 1000, fill = "white")
    canvas.create_image(105, 210, image=ImageTk.PhotoImage(app.battleImage))
    if(app.name == ''):
        canvas.create_text(app.width/2, 18, text = f"Random's Party:",
    font = "Helvetica 18 bold italic", fill = "gold")
    else:
        canvas.create_text(app.width/2, 18, text = f"{app.name}'s Party:",
        font = "Helvetica 18 bold italic", fill = "gold")
    im = app.firstPoke[app.firstCounter]
    canvas.create_image(75, 120, image =im)
    im2 = app.secondPoke[app.secondCounter]
    canvas.create_image(180, 120, image = im2)
    im3 = app.thirdPoke[app.thirdCounter]
    canvas.create_image(290, 120, image = im3)
    im4 = app.fourthPoke[app.fourthCounter]
    canvas.create_image(75, 250, image =im4)
    im5 = app.fifthPoke[app.fifthCounter]
    canvas.create_image(180, 250, image = im5)
    im6 = app.sixthPoke[app.sixthCounter]
    canvas.create_image(290, 250, image =im6)
    canvas.create_rectangle(260, 10, 330 ,45, fill = "gold")
    canvas.create_rectangle(260, 340, 330 ,375, fill = "gold")
    canvas.create_text(295, 27.5, text = "Competitive", 
    font = "Helvetica 12 bold italic", fill = "black")
    canvas.create_text(295, 357.5, text = "Casual", 
    font = "Helvetica 16 bold italic", fill = "black")

def drawBattleScreen(app,canvas):
    canvas.create_rectangle(0, 0, 1000, 1000, fill = "white")
    canvas.create_image(200, 200, image=ImageTk.PhotoImage(app.battleScreen)) #Draws battle background
    #Draws the opponent/AI's pokemon based on which trainer the user is facing
    if(app.trainerIndex == 0):
        if(app.currOppIndex == 0):
            canvas.create_image(280, 180, image = app.oppFirstPoke[app.oppFirstCount])
        if(app.currOppIndex == 1):
            canvas.create_image(280, 180, image = app.oppSecondPoke[app.oppSecondCount])
        if(app.currOppIndex == 2):
            canvas.create_image(280, 180, image = app.oppThirdPoke[app.oppThirdCount])
        if(app.currOppIndex == 3):
            canvas.create_image(280, 180, image = app.oppFourthPoke[app.oppFourthCount])
        if(app.currOppIndex == 4):
            canvas.create_image(280, 180, image = app.oppFifthPoke[app.oppFifthCount])
        if(app.currOppIndex == 5):
            canvas.create_image(280, 180, image = app.oppSixthPoke[app.oppSixthCount])
    elif(app.trainerIndex == 1):
        if(app.currOppIndex == 0):
            canvas.create_image(280, 180, image = app.secondOppFirst[app.secondOppFirstCount])
        if(app.currOppIndex == 1):
            canvas.create_image(280, 180, image = app.secondOppSecond[app.secondOppSecondCount])
        if(app.currOppIndex == 2):
            canvas.create_image(280, 180, image = app.secondOppThird[app.secondOppThirdCount])
        if(app.currOppIndex == 3):
            canvas.create_image(280, 180, image = app.secondOppFourth[app.secondOppFourthCount])
        if(app.currOppIndex == 4):
            canvas.create_image(280, 180, image = app.secondOppFifth[app.secondOppFifthCount])
        if(app.currOppIndex == 5):
            canvas.create_image(280, 180, image = app.secondOppSixth[app.secondOppSixthCount])
    elif(app.trainerIndex == 2):
        if(app.currOppIndex == 0):
            canvas.create_image(280, 180, image = app.leaderFirst[app.leaderFirstCount])
        if(app.currOppIndex == 1):
            canvas.create_image(280, 180, image = app.leaderSecond[app.leaderSecondCount])
        if(app.currOppIndex == 2):
            canvas.create_image(280, 180, image = app.leaderThird[app.leaderThirdCount])
        if(app.currOppIndex == 3):
            canvas.create_image(280, 180, image = app.leaderFourth[app.leaderFourthCount])
        if(app.currOppIndex == 4):
            canvas.create_image(280, 180, image = app.leaderFifth[app.leaderFifthCount])
        if(app.currOppIndex == 5):
            canvas.create_image(280, 180, image = app.leaderSixth[app.leaderSixthCount])
    
    #Draws the user backsprite of the pokemon they are currently usering
    if(app.oneParty == True):
        canvas.create_image(app.width/4, 280, image= ImageTk.PhotoImage(app.firstBattlePoke))
    elif(app.twoParty == True):
        canvas.create_image(app.width/4, 280, image= ImageTk.PhotoImage(app.secondBattlePoke))
    elif(app.threeParty == True):
        canvas.create_image(app.width/4, 280, image= ImageTk.PhotoImage(app.thirdBattlePoke))
    elif(app.fourParty == True):
        canvas.create_image(app.width/4, 280, image= ImageTk.PhotoImage(app.fourthBattlePoke))
    elif(app.fiveParty == True):
        canvas.create_image(app.width/4, 280, image= ImageTk.PhotoImage(app.fifthBattlePoke))
    elif(app.sixParty == True):
        canvas.create_image(app.width/4, 280, image= ImageTk.PhotoImage(app.sixthBattlePoke))
    
    #Draws bottom fight rectangle and moves/party/health bars above Pokemon
    if(app.partyPick != True):
        canvas.create_rectangle(5, 320, 345, 390, fill = "white", outline = "black",
        width = "5")
        canvas.create_line(app.width/2, 320, app.width/2, 390, fill = "black", width = "5")
        canvas.create_text(app.width/4, 355, text = "What will you do?", fill = "black", 
        font = "Helvetica 18 bold italic")
        canvas.create_line(app.width/2, 355, app.width, 355, fill = "black", width = "3")
        canvas.create_text(3*app.width/4, 340, text = "Fight", font = "Helvetica 18 bold")
        canvas.create_text(3*app.width/4, 370, text = "Pokémon Party", font = "Helvetica 18 bold")
    currPokemon = team[app.currUserIndex]
    currOppPokemon = opponentTeam[app.currOppIndex]
    moveSet = getMoves(currPokemon,'KantoPokemon.csv')
    health = app.pokeObjList[app.currUserIndex].getHealth()
    if(app.trainerIndex == 0):
        oppHealth = app.oppPokeObj[app.currOppIndex].getHealth()
    elif(app.trainerIndex == 1):
        oppHealth = app.oppPokeObjTwo[app.currOppIndex].getHealth()
    elif(app.trainerIndex == 2):
        oppHealth = app.oppPokeObjThree[app.currOppIndex].getHealth()
    #user health
    if(health == 300):
        canvas.create_rectangle(80, 200, 150, 210, fill = "lime green", outline = "black",
        width = "1")
    else:
        percent = health/300
        add = 70 * percent
        endGreen = 80 + add
        canvas.create_rectangle(80, 200, endGreen, 210, fill = "lime green", outline = "black",
        width = "1")
        canvas.create_rectangle(endGreen, 200, 150, 210, fill = "black", outline = "black",
        width = "1")
    #AI health
    if(oppHealth == 300):
        canvas.create_rectangle(240, 120, 310, 130, fill = "lime green", outline = "black",
        width = "1")
    else:
        percent = oppHealth/300
        add = 70 * percent
        endGreen = 240 + add
        canvas.create_rectangle(240, 120, endGreen, 130, fill = "lime green", outline = "black",
        width = "1")
        canvas.create_rectangle(endGreen, 120, 310, 130, fill = "black", outline = "black",
        width = "1")
    if(app.movePick == True):
        canvas.create_rectangle(5, 320, 345, 390, fill = "white", outline = "black",
        width = "5")
        canvas.create_line(app.width/2, 320, app.width/2, 390, fill = "black", width = "5")
        canvas.create_line(5, 355, app.width, 355, fill = "black", width = "3")
        canvas.create_text(app.width/4, 340, text = f"{moveSet[0]}", font = "Helvetica 18 bold", fill = "black")
        canvas.create_text(3*app.width/4, 340, text = f"{moveSet[1]}", font = "Helvetica 18 bold", fill = "black")
        canvas.create_text(app.width/4, 370, text = f"{moveSet[2]}", font = "Helvetica 18 bold", fill = "black")
        canvas.create_text(3*app.width/4, 370, text = f"{moveSet[3]}", font = "Helvetica 18 bold", fill = "black")
    if(app.firstMove == True):
        canvas.create_rectangle(5, 320, 345, 390, fill = "white", outline = "black",
        width = "5")
        canvas.create_text(app.width/2, 350, text = f'{currPokemon} used {moveSet[0]}')
    if(app.secondMove == True):
        canvas.create_rectangle(5, 320, 345, 390, fill = "white", outline = "black",
        width = "5")
        canvas.create_text(app.width/2, 350, text = f'{currPokemon} used {moveSet[1]}')
    if(app.thirdMove == True):
        canvas.create_rectangle(5, 320, 345, 390, fill = "white", outline = "black",
        width = "5")
        canvas.create_text(app.width/2, 350, text = f'{currPokemon} used {moveSet[2]}')
    if(app.fourthMove == True):
        canvas.create_rectangle(5, 320, 345, 390, fill = "white", outline = "black",
        width = "5")
        canvas.create_text(app.width/2, 350, text = f'{currPokemon} used {moveSet[3]}')
    if(app.aliveUser == 5):
        canvas.create_rectangle(5, 320, 345, 390, fill = "white", outline = "black",
        width = "5")
        canvas.create_text(app.width/2, 355, text = "112 MOVE! \nClick here!", font = "Helvetica 28 bold italic")

    #UI in progress
    '''if(app.userSwitch == True):
        canvas.create_rectangle(5, 320, 345, 390, fill = "white", outline = "black",
        width = "5")
        canvas.create_text(app.width/2, 355, text = f"The AI has switched to {opponentTeam[app.currOppIndex]}", font = "Helvetica 20 bold italic")
        
    if(app.oppSwitch == True):
        canvas.create_rectangle(5, 320, 345, 390, fill = "white", outline = "black",
        width = "5")
        canvas.create_text(app.width/2, 355, text = f"The AI has switched to {opponentTeam[app.currOppIndex]}", font = "Helvetica 20 bold italic")'''

def randomize(path): #Read file of all Pokemon in #Randomize a team of 6
    with open(path, "rt") as f:
        fileString = f.read()
    team = []
    for line in fileString.splitlines():
        for i in range(6):
            randomNum = random.randint(1,151)
            if(line.startswith(str(randomNum))):
                words = line.split(",")
                if(len(team) == 6):
                    break
                team.append(words[1])
    return team

#I got the csv of Kanto Pokemon and their move sets from https://github.com/christopher-cao/Pokemon-Simulator-in-Python 
team = randomize('KantoPokemon.csv')
opponentTeam = randomize('KantoPokemon.csv')
print(opponentTeam)
oppTeam2 = randomize('KantoPokemon.csv')
print(oppTeam2)
leaderTeam = ['Blastoise', 'Pidgey', 'Onix', 'Bellsprout', 'Pikachu', 'Ponyta']
print(leaderTeam)

def loopSprites(team, directory):
    gifList = []
    lowerList = []
    for pokemon in team:
        lowerList.append(pokemon.lower())
    for lower in lowerList:
        for gif in directory:
            if(lower in gif):
                gifList.append(gif)
    if(len(gifList) > 6):
        for gif2 in gifList:
            compGif = gif2.strip(".gif")
            if(compGif not in lowerList):
                gifList.remove(gif2)
    return gifList

#I got the folder of pokemon sprites from https://github.com/christopher-cao/Pokemon-Simulator-in-Python
directory = os.listdir('/Users/shreyas/Desktop/15-112/Term Project/Gen 1 Sprites')
gifList = loopSprites(team, directory)
oppGifList = loopSprites(opponentTeam, directory)
oppGifList2 = loopSprites(oppTeam2, directory)
oppGifList3 = loopSprites(leaderTeam, directory)

def loopBackSprites(team, directory, path):
    with open(path, "rt") as f:
        fileString = f.read()
    backGifList = []
    numList = []
    for line in fileString.splitlines():
        if(line.startswith("KantoPokemon")):
            continue
        words = line.split(",")
        for pokemon in team:
            if(words[1] == pokemon):
                numList.append(words[0])
    for num in numList:
        for image in directory:
            comp = image.strip(".png")
            if(comp == num):
                backGifList.append(image)
    return backGifList
    

backDirectory = os.listdir('/Users/shreyas/Desktop/15-112/Term Project/BackSprites')
backGifList = loopBackSprites(team, backDirectory, 'KantoPokemon.csv')

def getMoves(pokemon, path): #for Pokemon Class
    moveList = list()
    with open(path, "rt") as f:
        fileString = f.read()
    for line in fileString.splitlines():
        if(line.startswith("KantoPokemon")):
            continue
        words = line.split(",")
        if(pokemon == words[1]):
            moveList.append(words[10])
            moveList.append(words[11])
            moveList.append(words[12])
            moveList.append(words[13])
    return moveList

def getTypes(pokemon, path): #for Pokemon Class
    typeList = list()
    with open(path, "rt") as f:
        fileString = f.read()
    for line in fileString.splitlines():
        if(line.startswith("KantoPokemon")):
            continue
        words = line.split(",")
        if(pokemon == words[1]):
            typeList.append(words[2])
            typeList.append(words[3])
    return typeList

def getAttack(pokemon, path):
    with open(path, "rt") as f:
        fileString = f.read()
    for line in fileString.splitlines():
        if(line.startswith("KantoPokemon")):
            continue
        words = line.split(",")
        if(pokemon == words[1]):
            return words[5]

def getDefense(pokemon, path):
    with open(path, "rt") as f:
        fileString = f.read()
    for line in fileString.splitlines():
        if(line.startswith("KantoPokemon")):
            continue
        words = line.split(",")
        if(pokemon == words[1]):
            return words[6]

def getSpecialAttack(pokemon, path):
    with open(path, "rt") as f:
        fileString = f.read()
    for line in fileString.splitlines():
        if(line.startswith("KantoPokemon")):
            continue
        words = line.split(",")
        if(pokemon == words[1]):
            return words[7]

def getSpecialDefense(pokemon, path):
    with open(path, "rt") as f:
        fileString = f.read()
    for line in fileString.splitlines():
        if(line.startswith("KantoPokemon")):
            continue
        words = line.split(",")
        if(pokemon == words[1]):
            return words[8]

def getMoveType(move, path): #for move Class
    moveType = ""
    with open(path, "rt") as f:
        fileString = f.read()
    for line in fileString.splitlines():
        words = line.split(",")
        if(move == words[0]):
            moveType = words[1]
    return moveType

def getMoveForm(move, path): #for Move Class
    with open(path, "rt") as f:
        fileString = f.read()
    for line in fileString.splitlines():
        words = line.split(",")
        if(move == words[0]):
            if(words[3] == "—"):
                return "Special"
            else:
                return "Physical"

def getMovePower(move, path): #for Move Class
    with open(path, "rt") as f:
        fileString = f.read()
    for line in fileString.splitlines():
        words = line.split(",")
        if(move == words[0]):
            if(words[3] != "—"):
                return words[3]
    return 0

#Move Object Class
class Move:
    def __init__(self, name, type, form, power, ):
        self.name = name
        self.type = type
        self.form = form
        self.power = power

#Pokemon Object Class
class Pokemon(Move): #Pokemon class
    def __init__(self, name, types, moves, health, level, attack, defense, specialAttack, specialDefense):
        self.name = name
        self.type1 = types[0]
        self.type2 = types[1]
        self.move1 = moves[0]
        self.move2 = moves[1]
        self.move3 = moves[2]
        self.move4 = moves[3]
        self.attack = attack
        self.defense = defense
        self.specialAttack = specialAttack
        self.specialDefense = specialDefense
        self.health = health
        self.level = level
    
    def getHealth(self):
        return self.health
    
    def getLevel(self):
        return self.level
    
    def getTypes(self):
        return (self.type1, self.type2)
    
    def heal(self):
        self.health = 300
        return self.health
    
    def getDamage(self, AIPoke, move):
        stab = 1 #part of the equation
        critHit = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1.5] #6.25% chance for a critical hit in pokemon
        if(move.type == self.type1):
            stab *= 1.5
        if(move.type == self.type2):
            stab *= 1.5
        if(move.form == "Physical"):
            #using equation for damage --> Type still needs to be accounted for after this
            damage = ((((22 * float(move.power) * (float(self.attack)/float(AIPoke.defense))) / 50) + 2) * random.choice(critHit)  * stab) 
        else:
            damage = (((22 * float(move.power) * (float(self.attack)/float(AIPoke.defense))) / 50) + 2) * random.choice(critHit) * stab
        #Type effectiveness if statements: (Repetitive)
        damage = typeEffectiveness(damage, move.type, AIPoke.type1, AIPoke.type2)
        damage = round(damage, 0)
        return damage

    def Attack(self, AIPoke, move):
        stab = 1 #part of the equation
        critHit = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1.5] #6.25% chance for a critical hit in pokemon
        death = 0 #If 0 --> Alive, if 1 --> Dead
        if(move.type == self.type1):
            stab *= 1.5
        if(move.type == self.type2):
            stab *= 1.5
        if(move.form == "Physical"):
            #using equation for damage --> Type still needs to be accounted for after this
            damage = ((((22 * float(move.power) * (float(self.attack)/float(AIPoke.defense))) / 50) + 2) * random.choice(critHit)  * stab) 
        else:
            damage = (((22 * float(move.power) * (float(self.attack)/float(AIPoke.defense))) / 50) + 2) * random.choice(critHit) * stab
        #Type effectiveness if statements: (Repetitive)
        damage = typeEffectiveness(damage, move.type, AIPoke.type1, AIPoke.type2)
        damage = round(damage, 0)
        print(f'{self.name} used {move.name}!')
        AIPoke.health -= damage
        print(f"{AIPoke.name} took {damage} damage!")

        #check if AI is dead
        if(AIPoke.health <= 0):
            print(f"{AIPoke.name} has fainted")
            death = 1
            AIPoke.health = 0
        
        return death
    
    def oneTwelveReduce(self):
        self.health //= 2

def typeEffectiveness(damage, movetype, type1, type2):
    if(movetype == "Normal" and type1 == "Ghost"):
        damage *= 0
    if(movetype == "Normal" and type2 == "Ghost"):
        damage *= 0
    if(movetype == "Normal" and (type1 == "Rock" or type2 == "Rock")):
        damage *= .5
    if(movetype == "Fire" and (type1 == "Fire" or type2 == "Fire")):
        damage *= .5
    if(movetype == "Fire" and (type1 == "Water" or type2 == "Water")):
        damage *= .5
    if(movetype == "Fire" and (type1 == "Grass" or type2 == "Grass")):
        damage *= 2
    if(movetype == "Fire" and (type1 == "Ice" or type2 == "Ice")):
        damage *= 2
    if(movetype == "Fire" and (type1 == "Bug" or type2 == "Bug")):
        damage *= 2
    if(movetype == "Fire" and (type1 == "Rock" or type2 == "Rock")):
        damage *= .5
    if(movetype == "Fire" and (type1 == "Dragon" or type2 == "Dragon")):
        damage *= .5 
    if(movetype == "Water" and (type1 == "Fire" or type2 == "Fire")):
        damage *= 2
    if(movetype == "Water" and (type1 == "Water" or type2 == "Water")):
        damage *= .5
    if(movetype == "Water" and (type1 == "Grass" or type2 == "Grass")):
        damage *= .5
    if(movetype == "Water" and (type1 == "Ground" or type2 == "Ground")):
        damage *= 2
    if(movetype == "Water" and (type1 == "Rock" or type2 == "Rock")):
        damage *= 2
    if(movetype == "Water" and (type1 == "Dragon" or type2 == "Dragon")):
        damage *= .5
    if(movetype == "Electric" and (type1 == "Water" or type2 == "Water")):
        damage *= 2
    if(movetype == "Electric" and (type1 == "Electric" or type2 == "Electric")):
        damage *= .5
    if(movetype == "Electric" and (type1 == "Grass" or type2 == "Grass")):
        damage *= .5
    if(movetype == "Electric" and (type1 == "Ground" or type2 == "Ground")):
        damage *= 0
    if(movetype == "Electric" and (type1 == "Flying" or type2 == "Flying")):
        damage *= 2
    if(movetype == "Electric" and (type1 == "Dragon" or type2 == "Dragon")):
        damage *= .5
    if(movetype == "Grass" and (type1 == "Fire" or type2 == "Fire")):
        damage *= .5
    if(movetype == "Grass" and (type1 == "Water" or type2 == "Water")):
        damage *= 2
    if(movetype == "Grass" and (type1 == "Grass" or type2 == "Grass")):
        damage *= .5
    if(movetype == "Grass" and (type1 == "Poison" or type2 == "Poison")):
        damage *= .5
    if(movetype == "Grass" and (type1 == "Ground" or type2 == "Ground")):
        damage *= 2
    if(movetype == "Grass" and (type1 == "Flying" or type2 == "Flying")):
        damage *= .5
    if(movetype == "Grass" and (type1 == "Bug" or type2 == "Bug")):
        damage *= .5
    if(movetype == "Grass" and (type1 == "Rock" or type2 == "Rock")):
        damage *= 2
    if(movetype == "Grass" and (type1 == "Dragon" or type2 == "Dragon")):
        damage *= .5
    if(movetype == "Ice" and (type1 == "Water" or type2 == "Water")):
        damage *= .5
    if(movetype == "Ice" and (type1 == "Grass" or type2 == "Grass")):
        damage *= 2
    if(movetype == "Ice" and (type1 == "Ice" or type2 == "Ice")):
        damage *= .5
    if(movetype == "Ice" and (type1 == "Ground" or type2 == "Ground")):
        damage *= 2
    if(movetype == "Ice" and (type1 == "Flying" or type2 == "Flying")):
        damage *= 2
    if(movetype == "Ice" and (type1 == "Dragon" or type2 == "Dragon")):
        damage *= 2
    if(movetype == "Fighting" and (type1 == "Normal" or type2 == "Normal")):
        damage *= 2
    if(movetype == "Fighting" and (type1 == "Ice" or type2 == "Ice")):
        damage *= 2
    if(movetype == "Fighting" and (type1 == "Poison" or type2 == "Poison")):
        damage *= .5
    if(movetype == "Fighting" and (type1 == "Flying" or type2 == "Flying")):
        damage *= .5
    if(movetype == "Fighting" and (type1 == "Psychic" or type2 == "Psychic")):
        damage *= .5
    if(movetype == "Fighting" and (type1 == "Bug" or type2 == "Bug")):
        damage *= .5
    if(movetype == "Fighting" and (type1 == "Rock" or type2 == "Rock")):
        damage *= 2
    if(movetype == "Fighting" and (type1 == "Ghost" or type2 == "Ghost")):
        damage *= 0
    if(movetype == "Poison" and (type1 == "Grass" or type2 == "Grass")):
        damage *= 2
    if(movetype == "Poison" and (type1 == "Poison" or type2 == "Poison")):
        damage *= .5
    if(movetype == "Poison" and (type1 == "Ground" or type2 == "Ground")):
        damage *= .5
    if(movetype == "Poison" and (type1 == "Bug" or type2 == "Bug")):
        damage *= 2
    if(movetype == "Poison" and (type1 == "Rock" or type2 == "Rock")):
        damage *= .5
    if(movetype == "Poison" and (type1 == "Ghost" or type2 == "Ghost")):
        damage *= .5
    if(movetype == "Ground" and (type1 == "Fire" or type2 == "Fire")):
        damage *= 2
    if(movetype == "Ground" and (type1 == "Electric" or type2 == "Electric")):
        damage *= 2
    if(movetype == "Ground" and (type1 == "Grass" or type2 == "Grass")):
        damage *= .5
    if(movetype == "Ground" and (type1 == "Poison" or type2 == "Poison")):
        damage *= 2
    if(movetype == "Ground" and (type1 == "Flying" or type2 == "Flying")):
        damage *= 0
    if(movetype == "Ground" and (type1 == "Bug" or type2 == "Bug")):
        damage *= .5
    if(movetype == "Ground" and (type1 == "Rock" or type2 == "Rock")):
        damage *= 2
    if(movetype == "Flying" and (type1 == "Electric" or type2 == "Electric")):
        damage *= .5
    if(movetype == "Flying" and (type1 == "Grass" or type2 == "Grass")):
        damage *= 2
    if(movetype == "Flying" and (type1 == "Fighting" or type2 == "Fighting")):
        damage *= 2
    if(movetype == "Flying" and (type1 == "Bug" or type2 == "Bug")):
        damage *= 2
    if(movetype == "Flying" and (type1 == "Rock" or type2 == "Rock")):
        damage *= .5
    if(movetype == "Psychic" and (type1 == "Fighting" or type2 == "Fighting")):
        damage *= 2
    if(movetype == "Psychic" and (type1 == "Poison" or type2 == "Poison")):
        damage *= 2
    if(movetype == "Psychic" and (type1 == "Psychic" or type2 == "Psychic")):
        damage *= .5
    if(movetype == "Bug" and (type1 == "Water" or type2 == "Water")):
        damage *= .5
    if(movetype == "Bug" and (type1 == "Grass" or type2 == "Grass")):
        damage *= 2
    if(movetype == "Bug" and (type1 == "Fighting" or type2 == "Fighting")):
        damage *= .5
    if(movetype == "Bug" and (type1 == "Poison" or type2 == "Poison")):
        damage *= 2
    if(movetype == "Bug" and (type1 == "Flying" or type2 == "Flying")):
        damage *= .5
    if(movetype == "Bug" and (type1 == "Psychic" or type2 == "Psychic")):
        damage *= 2
    if(movetype == "Bug" and (type1 == "Ghost" or type2 == "Ghost")):
        damage *= .5
    if(movetype == "Rock" and (type1 == "Fire" or type2 == "Fire")):
        damage *= 2
    if(movetype == "Rock" and (type1 == "Ice" or type2 == "Ice")):
        damage *= 2
    if(movetype == "Rock" and (type1 == "Fighting" or type2 == "Fighting")):
        damage *= .5
    if(movetype == "Rock" and (type1 == "Ground" or type2 == "Ground")):
        damage *= .5
    if(movetype == "Rock" and (type1 == "Flying" or type2 == "Flying")):
        damage *= 2
    if(movetype == "Rock" and (type1 == "Bug" or type2 == "Bug")):
        damage *= 2
    if(movetype == "Ghost" and (type1 == "Normal" or type2 == "Normal")):
        damage *= 0
    if(movetype == "Ghost" and (type1 == "Psychic" or type2 == "Psychic")):
        damage *= 0
    if(movetype == "Ghost" and (type1 == "Ghost" or type2 == "Ghost")):
        damage *= 2
    if(movetype == "Dragon" and (type1 == "Dragon" or type2 == "Dragon")):
        damage *= 2
    
    return damage


def createPokemon(pokemon):
    moveObjects = []
    moveList = getMoves(pokemon, 'KantoPokemon.csv')
    types = getTypes(pokemon, 'KantoPokemon.csv')
    name = pokemon
    attack = getAttack(pokemon, 'KantoPokemon.csv')
    defense = getDefense(pokemon, 'KantoPokemon.csv')
    specialAttack = getSpecialAttack(pokemon, 'KantoPokemon.csv')
    specialDefense = getSpecialDefense(pokemon, 'KantoPokemon.csv')
    pokeObj = Pokemon(name, types, moveList, 300, random.randint(80,99), attack, defense, specialAttack, specialDefense)
    for move in moveList:
        name = move
        type = getMoveType(move, 'PokemonMoves.csv')
        form = getMoveForm(move, 'PokemonMoves.csv')
        power = getMovePower(move, 'PokemonMoves.csv')
        obj = Move(name, type, form, power)
        moveObjects.append(obj)
    return pokeObj, moveObjects


runApp(width=350, height=395)



