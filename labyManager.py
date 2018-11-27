from random import randint
import position as Position
import pygame
from constantes import*
import perso as Perso

"""laby means the maze, as we have to know"""

class LabyManager:
	def __init__(self):
		self.laby = [] # Necessary because must be known from several methods of instance (in a logic of continuity).
		#self.positionList = [] (Not necessary in attribute because used inside a single method of instance).
		self.initPosition = (0,0)
		self.exitPosition = (0,0)
		self.availableCases = [] 
		#self.gameObjetList = []
		

	@staticmethod
	def replace(inputStrinng, i, char):
	    outputString = inputStrinng[:i] + char + inputStrinng[i + 1:]
	    return outputString


	def loadLABY(self):
		"""for the open file, read the lines, close the file"""
		with open('./maps/laby03.txt') as file:
			"""nb: readlines () will add, on each line, a 16th and last character: '\ n' (= line break in the txt)"""
			self.laby = file.readlines()
			"""an item in this list (laby = []) is a complete line"""
		file.close()
		self.removeEndOfLineChar()

		
	def removeEndOfLineChar(self):
		"""for each line of the laby in charge of the lm instance"""
		for line in self.laby:
			"""indexOfLastChar = on the line, the last and 16th position numbered 15 (i.e. 0 ... 15 and len (line) = 16)"""
			indexOfLastChar = len(line) - 1
			if line[indexOfLastChar] == '\n':
				"""if this 16th and last character (in position # 15) is equal to \ n '(i.e. following line in the loaded txt) then:"""
				indexOfCurrentLine = self.laby.index(line)
				"""index () function with indexOfCurrentLine the number of the line on which we are"""
				line = self.replace(line, indexOfLastChar, '')
				"""this line = this line with the implementation of emptiness on the last character"""
				self.laby[indexOfCurrentLine] = line
				"""inserting this modified line instead of the old line that had \ n"""


	def buildAvailPositionList(self):
		positionList = []
		for line in self.laby:
			for x in range(0, len(line)):
				"""we run a range (i, j) = [i, ..., j-1], here len (line) = 15 is range = [0, ... 14] or 15 possible positions following the withdrawal of \ n : OK"""
				if line[x] == " ":
					"""if the position (i.e. n ° column) traveled on the line is empty"""
					indexOfCurrentLine = self.laby.index(line)
					"""index () function with indexOfCurrentLine the number of the line on which we are"""
					positionList.append(Position.Position(indexOfCurrentLine, x)) #rem. hors contexte** : un .append d'1 instance sur 1'attr. de classe update ce dernier "chez" ttes les instances.
					"""one adds to positionList: ALL the traversed positions (n ​​° line, n ° column) via a call of the module Position then of the class Position"""
		return positionList #positionList une var. (liste d'instances "position") de la méthode d'instance, non un attribut de classe, ni une instance d'où le hors contexte** de la rem..

		
	def generateInGameObjets(self):
		for x in range(1, 4):
			"""range (1, 4) = [1, 2, 3] else range (0, 4) = [0, 1, 2, 3]"""
			availableCasesCount = len(self.availableCases)
			"""aCasesCount = len(availabCases (attr. of instance)) = len("positionList") returned by buildAvailPositionList(), cf. initializeGame()"""
			index = (randint(0, availableCasesCount))
			"""taken at random between the 1st and the last possibility of positions"""
			if index < availableCasesCount:
				"""if 15 aCC index 15 will be out of range ==> range (0,15) = [0, ... 14]"""
				position = self.availableCases[index]
				"""Ccl °: position = one of the positions taken at random in the availableCases positions"""
				if x == 1:
					"""if it is the 1st pass i.e 1st created object = N"""
					self.laby[position.line] = self.replace(self.laby[position.line], position.column, "N") #N=NEEDLE
					"""the line (attribute) of the position = the line of the position where the vacuum is replaced by an "N" on the column (attr) of the position"""
				elif x == 2:
					self.laby[position.line] = self.replace(self.laby[position.line], position.column, "E") #E=ETHER
					"""2nd pass: same as position is an instance of the class Position all as other availableCases positions"""
				else:
					self.laby[position.line] = self.replace(self.laby[position.line], position.column, "T") #T=TUBE
				self.availableCases.pop(index)
				"""the position used is removed from the positions and the loop resumes (avoid putting N and E in the same position"""


	def findExitPosition(self):
		for line in self.laby:
			for x in line:
				"""the X is the guardian"""
				if x == 'X':
					return Position.Position(self.laby.index(line), line.index(x))
					"""exitPosition here becomes an instance of position (column, line)"""
					

	def findInitPosition(self):
		for line in self.laby:
			for x in line:
				if x == '8':
					"""the 8 it's Macgyver"""
					return Position.Position(self.laby.index(line), line.index(x))

		
		
	def initializeGame(self):
		self.loadLABY() 
		"""Loading the maze attribute"""
		self.availableCases = self.buildAvailPositionList() 
		"""detection of laby's free positions"""
		self.generateInGameObjets() 
		"""random creation of objects on laby's free positions"""
		self.initPosition = self.findInitPosition()
		"""determining the starting position and the starting position"""
		self.exitPosition = self.findExitPosition()



	
	def displayLaby(self, shadow):
		wall = pygame.image.load('./images/wallm.png').convert_alpha()
		"""loading wall picture"""
		
		mac = pygame.image.load('./images/macgyver1.png').convert()
		mac_b = pygame.transform.scale(mac, (30, 30))
		"""adjusting the size of the loaded mac image"""

		needle = pygame.image.load('./images/needle1.png').convert_alpha()
		needle_b = pygame.transform.scale(needle, (30, 30))

		ether = pygame.image.load('./images/ether.png').convert_alpha()
		ether_b = pygame.transform.scale(ether, (30, 30))

		tube = pygame.image.load('./images/tube.png').convert_alpha()
		"""_alpha () makes the background of the image transparent"""
		tube_b = pygame.transform.scale(tube, (30, 30))

		guard = pygame.image.load('./images/guard.png').convert_alpha()
	
		space = pygame.image.load('./images/space.png').convert_alpha()
		
		num_line = 0
		for line in self.laby:
			num_column = 0
			for sprite in line:
				x = num_column * taille_sprite
				y = num_line * taille_sprite
				if sprite == '*':
					shadow.blit(wall,(x,y))
					"""the * are replaced by the image wall, the coordinates of * are modified"""
				elif sprite == "N":
					shadow.blit(needle_b,(x,y))
					"""(1,1) becomes (30,30) for example and so on (scaling up)"""
				elif sprite == "T":
					shadow.blit(tube_b,(x,y))
				elif sprite == "E":
					shadow.blit(ether_b,(x,y))
				elif sprite == "8":
					shadow.blit(mac_b,(x,y))
				elif sprite == "X":
					shadow.blit(guard,(x,y))
				elif sprite == " ":
					shadow.blit(space,(x,y))
				num_column += 1
				"""next column on the line traveled"""
			num_line += 1
			"""once the line has been crossed, go to the next line"""


	def updatePersoPositionInLaby(self, oldPos, newPosition):
		"""on the old line of the perso (8 i.e. mac), one puts vacuum at the level of the column of the position"""
		self.laby[oldPos.line] = self.replace(self.laby[oldPos.line], oldPos.column, " ")
		"""on the new line of the perso ("", object or guardian), one puts the 8 (i.e.) mac, on the level. of the collar. of the position"""
		self.laby[newPosition.line] = self.replace(self.laby[newPosition.line], newPosition.column, "8")

	
	def nbInGameObjets(self):
		"""called in the caption (see game_loop (): title, counter and direction mode)"""
		gameObjetList = []
		for line in self.laby:
			for i in range(0, len(line)):
				if line[i] != "*" and line[i] != "X" and line[i] !=" " and line[i] != "8":
					"""for each column of each line if character = E, N or T then:"""
					indexOfCurrentLine = self.laby.index(line)
					gameObjetList.append(Position.Position(indexOfCurrentLine, i))
					"""we add this position to the list of object positions present in the maze"""
		return str(3-len(gameObjetList))
		"""we display (3-the number of objects) in the title of the laby (i.e. dc 2 if an object picked up and 2 objects remaining)"""

		
	def charAtPosition(self, pos):
		"""return the position (line, column) inside the maze (i.e. laby)"""
		return self.laby[pos.line][pos.column]
	
		
	def message_display(self, text, shadow):
		"""Def not used. ps: would return a message in the pygame screen"""
		myfont = pygame.font.SysFont("Comic Sans MS", 30)
		label = myfont.render(text, 1, (0, 255, 0))
		shadow.blit(label, (50, 215))
		"""position of message at screen"""


	

