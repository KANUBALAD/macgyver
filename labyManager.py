from random import randint
import position as Position
import pygame
from constantes import*
import perso as Perso


class LabyManager:
	def __init__(self):
		self.laby = []
		self.positionList = []
		self.initPosition = (0,0)
		self.exitPosition = (0,0)
		self.availableCases = []
		

	@staticmethod
	def replace(inputStrinng, i, char):
	    outputString = inputStrinng[:i] + char + inputStrinng[i + 1:]
	    return outputString


	def loadLABY(self):
		with open('./maps/laby03.txt') as file:
			self.laby = file.readlines()
		file.close()
		self.removeEndOfLineChar()

		
	def removeEndOfLineChar(self):
		for line in self.laby:
			indexOfLastChar = len(line) - 1
			if line[indexOfLastChar] == '\n':
				indexOfCurrentLine = self.laby.index(line)
				line = self.replace(line, indexOfLastChar, '')
				self.laby[indexOfCurrentLine] = line


	def buildAvailPositionList(self):
		positionList = []
		for line in self.laby:
			for x in range(0, len(line)):
				if line[x] == " ":
					indexOfCurrentLine = self.laby.index(line)
					positionList.append(Position.Position(indexOfCurrentLine, x))
		return positionList

		
	def generateInGameObjets(self):
		for x in range(1, 4):
			availableCasesCount = len(self.availableCases)
			index = (randint(0, availableCasesCount))
			if index < availableCasesCount:
				position = self.availableCases[index]
				if x == 1:
					self.laby[position.line] = self.replace(self.laby[position.line], position.column, "N") #N=NEEDLE
				elif x == 2:
					self.laby[position.line] = self.replace(self.laby[position.line], position.column, "E") #E=ETHER
				else:
					self.laby[position.line] = self.replace(self.laby[position.line], position.column, "T") #T=TUBE
				self.availableCases.pop(index)


	def findExitPosition(self):
		for line in self.laby:
			for x in line:
				if x == 'X':
					return Position.Position(self.laby.index(line), line.index(x))
					

	def findInitPosition(self):
		for line in self.laby:
			for x in line:
				if x == '8':
					return Position.Position(self.laby.index(line), line.index(x))


	def initializeGame(self):
		self.loadLABY()
		self.availableCases = self.buildAvailPositionList()
		self.generateInGameObjets()
		self.initPosition = self.findInitPosition()
		self.exitPosition = self.findExitPosition()



	def displayLaby(self, shadow):
		wall = pygame.image.load('./images/wallm.png').convert_alpha()
		
		mac = pygame.image.load('./images/macgyver1.png').convert()
		mac_b = pygame.transform.scale(mac, (30, 30))

		needle = pygame.image.load('./images/needle1.png').convert_alpha()
		needle_b = pygame.transform.scale(needle, (30, 30))

		ether = pygame.image.load('./images/ether.png').convert_alpha()
		ether_b = pygame.transform.scale(ether, (30, 30))

		tube = pygame.image.load('./images/tube.png').convert_alpha()
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
				elif sprite == "N":
					shadow.blit(needle_b,(x,y))
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
			num_line += 1


	def updatePersoPositionInLaby(self, oldPos, newPosition):
		self.laby[oldPos.line] = self.replace(self.laby[oldPos.line], oldPos.column, " ")
		self.laby[newPosition.line] = self.replace(self.laby[newPosition.line], newPosition.column, "8")

	
	def nbInGameObjets(self):
		gameObjetList = []
		for line in self.laby:
			for i in range(0, len(line)):
				if line[i] != "*" and line[i] != "X" and line[i] !=" " and line[i] != "8":
					indexOfCurrentLine = self.laby.index(line)
					gameObjetList.append(Position.Position(indexOfCurrentLine, i))
		return str(3-len(gameObjetList))

		
	def charAtPosition(self, pos):
		return self.laby[pos.line][pos.column]
	
		
	def message_display(self, text, shadow):
		myfont = pygame.font.SysFont("Comic Sans MS", 30)
		label = myfont.render(text, 1, (0, 255, 0))
		shadow.blit(label, (50, 215))


	

