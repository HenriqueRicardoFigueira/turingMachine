#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

class Maquina:
	def __init__(self, dados):
		#Conteudo da Fita
		self.contentTape = []
		for x in range(2,(len(dados))):
			aux = dados[x]
			self.contentTape.append(aux)

		#Abre o Arquivo
		arq = open(dados[1],'r')

		self.elements = arq.read().splitlines()
		#ALFABETO_ENTRADA
		self.inputAlpha = self.elements[0].split(" ")
		#ALFABETO_FITA
		self.tapeAlpha = self.elements[1].split(" ")
		#BRANCO
		self.branco = self.elements[2]
		#ESTADOS
		self.states = self.elements[3].split(" ")
		#INICIAL
		self.initialState = self.elements[4].strip()
		#FINAL
		self.finalStates = self.elements[5].split(" ")
		self.qtTape = int(self.elements[6])
		#TRANSIÇÕES
		self.transitionsaux = {}
		self.transitions = {}
		self.transitionsArq = []


		#COMEÇA QUEBRA DE ARQUIVO (modificar essa parte pra começar a indexar por hash e não por posição ""COMFIRMAR"")
		for k in self.elements[7:]:
			self.transitionsArq.append(k)


		for s in self.states:
			aux2 = []
			for t in self.transitionsArq:
				aux = t.split(" ")
				if s == aux[0]:
					aux2.append(aux[1:])
			self.transitionsaux[s]=[aux2]

		for s in self.states:
			aux3 = self.transitionsaux[s]

			auxsimbol = {}
			aux4 = aux3[0]
			
			for tr in aux4:
				if tr[1] in auxsimbol:
					traxx = (tr[0],tr[2],tr[3])
					auxsimbol[tr[1]].append(traxx)
				else:
					traxx = (tr[0],tr[2],tr[3])
					auxsimbol[tr[1]]= [traxx]

			self.transitions[s] = auxsimbol

	def changeCurrentState(self,newcurrent):
		self.currentState = newcurrent

	def isFinal(self,state):
		if state in self.finalStates:
			return True
		else:
			return False

	def isInitial(self,state):
		if str(state) == self.initialState:
			return  True
		else:
			return False

	def getCurrentState(self):
		return str(self.currentState)

	def retorna_transicoesPossiveis(self, iniState):
		if(iniState not in self.transitions):
			return None
		return self.transitions[iniState]

	def print_fitas(self,fitas):
		print("Quantidade de Fitas:" + str(len(fitas)))
		for fita in fitas:
			print("  Fita               :"+str(fitas.index(fita)))
			sys.stdout.write("  Posição da Cabeça  : ")
			for i in range(0,fita.posicao_cabeca): sys.stdout.write(' ')
			print('|')
			print("  Conteudo Atual Fita: "+fita.retorna_fita())
			print("  Estado Atual       : "+str(fita.retorna_estado()))
			print("  Estados Possíves   : "+str(self.retorna_transicoesPossiveis(fita.retorna_estado())))
