import position as Position
from labyManager import LabyManager
from constantes import *


class Perso:
	def __init__(self, pos, hasEther=False, hasTube=False, hasNeedle=False, alive=True):
		self.pos = pos
		self.alive = alive
		self.hasEther = hasEther
		self.hasTube = hasTube
		self.hasNeedle = hasNeedle



	def __str__(self):
		description = "Perso position:\n" + str(self.pos) + "\n"
		description += "alive: " + str(self.alive) + '\n'
		description += "has needle: " + str(self.hasNeedle) + '\n'
		description += "has ether: " + str(self.hasEther) + '\n'
		description += "has tube: " + str(self.hasTube) + '\n'
		return description


	def goLeft(self, labyManager):
		goingToPos = Position.Position(self.pos.line, self.pos.column - 1)
		self.willStepOnObject(goingToPos, labyManager)
		if labyManager.charAtPosition(goingToPos) != "*" and self.pos.column > 0:
			labyManager.updatePersoPositionInLaby(self.pos, goingToPos)
			self.pos = goingToPos
		else:
			pass
    	

	def goRight(self, labyManager):
		goingToPos = Position.Position(self.pos.line, self.pos.column + 1)
		self.willStepOnObject(goingToPos, labyManager)
		if labyManager.charAtPosition(goingToPos) != "*" and self.pos.column < len(labyManager.laby[self.pos.line]) - 1:
			labyManager.updatePersoPositionInLaby(self.pos, goingToPos)
			self.pos = goingToPos
		else:
			pass
    	

	def goUp(self, labyManager):
		goingToPos = Position.Position(self.pos.line - 1, self.pos.column)
		self.willStepOnObject(goingToPos, labyManager)
		if labyManager.charAtPosition(goingToPos) != "*" and self.pos.line > 0:
			labyManager.updatePersoPositionInLaby(self.pos, goingToPos)
			self.pos = goingToPos
		else:
			pass
    	

	def goDown(self, labyManager):
		goingToPos = Position.Position(self.pos.line + 1, self.pos.column)
		self.willStepOnObject(goingToPos, labyManager)
		if labyManager.charAtPosition(goingToPos) != "*" and self.pos.line < len(labyManager.laby) - 1:
			labyManager.updatePersoPositionInLaby(self.pos, goingToPos)
			self.pos = goingToPos
		else:
			pass

	def willStepOnObject(self, pos, labyManager):
		if labyManager.charAtPosition(pos) == 'N':
			self.hasNeedle = True
		elif labyManager.charAtPosition(pos) == 'E':
			self.hasEther = True
		elif labyManager.charAtPosition(pos) == 'T':
			self.hasTube = True
		elif labyManager.charAtPosition(pos) == 'X':
			if not self.hasAllObjects():
				self.alive = False
	

	def hasAllObjects(self):
		return self.hasNeedle and self.hasTube and self.hasEther


	
