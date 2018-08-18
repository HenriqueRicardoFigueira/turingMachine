# Linha 1: alfabeto de entrada
# Linha 2: alfabeto da fita
# Linha 3: simbolo que representa um espaco em branco na fita
# Linha 4: estado inicial
# Linha 5: conjunto de estados finais
# Linha 6: quantidade de fitas
# Linhas 7 em diante: transicoes, uma por linha, no formato estado atual, novo estado e, para cada fita, o respectivo simbolo atual, novo simbolo, direcao para mover a cabeca

from xml.etree import ElementTree as ET
import csv
import sys

class Transition(object):
	def __init__(self):
		self.currentState = None
		self.newState = None
		self.tapeMovements = []

	def __lt__(self, other):
		if self.currentState < other.currentState:
			return True
		elif self.currentState > other.currentState:
			return False
		elif self.newState < other.newState:
			return True
		elif self.newState > other.newState:
			return False
		else:
			return self.newState < other.newState

class TapeMovement(object):
	def __init__(self):
		self.tape = 1
		self.currentTapeSymbol = None
		self.newTapeSymbol = None
		self.headDirection = None

	def __lt__(self, other):
		if self.currentTapeSymbol < other.currentTapeSymbol:
			return True
		elif self.currentTapeSymbol > other.currentTapeSymbol:
			return False
		elif self.newTapeSymbol < other.newTapeSymbol:
			return True
		elif self.newTapeSymbol > other.newTapeSymbol:
			return False
		else:
			return self.headDirection < other.headDirection

class Jflap2Utfpr(object):
	def __init__(self):
		self.alphabet = set()
		self.states = set()
		self.tapeSymbols = set()
		self.tapes = 1
		self.initialState = None
		self.finalStates = set()
		self.transitions = set()
		self.singleTape = False

	def convert(self, inputFile, outputFile, blankSymbol = 'B', alphabet = None):
		self.blankSymbol = blankSymbol
		self.tapeSymbols.add(self.blankSymbol)

		xmldoc = ET.parse(inputFile)
		root = xmldoc.getroot()
		if root.find('tapes') == None:
			self.singleTape = True
			self.tapes = 1
		else:
			self.tapes = int(root.find('tapes').text)

		tm = root.find('automaton')
		stateElementName = 'block'
		if tm == None:  # Old JFLAP format
			tm = root
			stateElementName = 'state'
			
		for s in tm.findall(stateElementName):
			state = s.attrib['id']
			self.states.add(state)
			if s.find('initial') is not None:
				self.initialState = state
			if s.find('final') is not None:
				self.finalStates.add(state)

		for t in tm.findall('transition'):
			transition = Transition()
			self.transitions.add(transition)
			transition.currentState = t.find('from').text
			transition.newState = t.find('to').text
			tapeXPath = ''
			for i in range(1, self.tapes + 1):
				movement = TapeMovement()
				transition.tapeMovements.append(movement)
				movement.tape = i
				if not self.singleTape: # Workaround for handling single and multitape Turing machines
					tapeXPath = "[@tape='" + str(i) + "']"
				if t.find("read" + tapeXPath).text is not None:
					movement.currentTapeSymbol = t.find("read" + tapeXPath).text
					self.tapeSymbols.add(movement.currentTapeSymbol)
				else:
					movement.currentTapeSymbol = blankSymbol
				if t.find("write" + tapeXPath).text is not None:
					movement.newTapeSymbol = t.find("write" + tapeXPath).text
					self.tapeSymbols.add(movement.newTapeSymbol)
				else:
					movement.newTapeSymbol = blankSymbol
				movement.headDirection = t.find("move" + tapeXPath).text

		if alphabet is None:
			self.alphabet = self.tapeSymbols.copy()
			self.alphabet.remove(self.blankSymbol)
		else:
			self.alphabet = alphabet
		
		with open(outputFile, 'w') as csvfile:
			writer = csv.writer(csvfile, delimiter=' ', lineterminator='\n')
			writer.writerow(sorted(self.alphabet))
			writer.writerow(sorted(self.tapeSymbols))
			writer.writerow([self.blankSymbol])
			writer.writerow(sorted(self.states))
			writer.writerow(self.initialState)
			writer.writerow(sorted(self.finalStates))
			writer.writerow([self.tapes])
			for transition in sorted(self.transitions):
				transitionDescription = []
				transitionDescription.append(transition.currentState)
				transitionDescription.append(transition.newState)
				for i in range(1, self.tapes+1):
					for movement in sorted(transition.tapeMovements):
						if movement.tape == i:
							transitionDescription.append(movement.currentTapeSymbol)
							transitionDescription.append(movement.newTapeSymbol)
							transitionDescription.append(movement.headDirection)
				writer.writerow(transitionDescription)

if __name__ == "__main__":
	if len(sys.argv) != 3:
		print("Parametros insuficientes. Informe o nome de arquivo de entrada e o nome do arquivo de saida")
		sys.exit(1)
	converter = Jflap2Utfpr()
	converter.convert(sys.argv[1], sys.argv[2])

