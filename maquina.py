#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, copy, random
from fita import Fita

class Maquina:
	def __init__(self, dados):
		#Conteudo da Fita
		self.contentTape = []
		for x in range(2,(len(dados))):
			aux = dados[x]
			self.contentTape.append(aux)

		#Abre o Arquivo
		arq = open(dados[1],'r')

		self.linhasArq = arq.read().splitlines()

		#variaveis
		self.alfaEntrada = self.linhasArq[0].split(" ")
		self.alfaFita = self.linhasArq[1].split(" ")
		self.branco = self.linhasArq[2]
		self.estados = self.linhasArq[3].split(" ")
		self.estadoFinal = self.linhasArq[5].split(" ")
		self.tamanhoFita = int(self.linhasArq[6])
		self.transicoes = {}
		self.fitas = []

		#inicializa maquina
		self.carrega_maquinaArquivo()
		self.cria_fitaInicial(self.linhasArq[4].strip())

	def cria_fitaInicial(self, estadoInicial):
		self.adiciona_fita(Fita(self.contentTape, self.alfaEntrada, self.alfaFita, self.branco, estadoInicial))

	def carrega_maquinaArquivo(self):
		#COMEÇA QUEBRA DE ARQUIVO (modificar essa parte pra começar a indexar por hash e não por posição ""COMFIRMAR"")
		self.transicoes = self.grava_transicoesEstadosDestino(self.grava_transicoesEstadosOrigem())

	def grava_transicoesEstadosOrigem(self):
		transicoesArq = []
		transicoesOrigem = {}

		for k in self.linhasArq[7:]:
			transicoesArq.append(k)

		for s in self.estados:
			aux2 = []
			for t in transicoesArq:
				aux = t.split(" ")
				if s == aux[0]:
					aux2.append(aux[1:])
			transicoesOrigem[s]=[aux2]
		
		return transicoesOrigem

	def grava_transicoesEstadosDestino(self, transicoesOrigem):
		transicoesDestino= {}
		for estado in self.estados:
			transiDest = {}
			
			for transicao in transicoesOrigem[estado][0]:
				if transicao[1] in transiDest:
					estadoDest = (transicao[0],transicao[2],transicao[3])
					transiDest[transicao[1]].append(estadoDest)
				else:
					estadoDest = (transicao[0],transicao[2],transicao[3])
					transiDest[transicao[1]]= [estadoDest]

			transicoesDestino[estado] = transiDest

		return transicoesDestino

	def verifica_estadoFinal(self, fita):
		if fita.retorna_estado() in self.estadoFinal:
			print "\nResultado: Palavra Aceita."
			return True
		else:
			return False

	def retorna_transicoesPossiveis(self, iniState):
		if(iniState not in self.transicoes):
			return None
		return self.transicoes[iniState]

	def print_fitas(self):
		print("\nQuantidade de Fitas: " + str(len(self.fitas))+"\n")
		for fita in self.fitas:
			print("    Fita: "+str(self.fitas.index(fita)))
			sys.stdout.write("    Posição da Cabeça  : ")
			sys.stdout.write(' '*fita.posicao_cabeca)
			print('|')
			print("    Conteudo Atual Fita: "+fita.retorna_fita())
			print("    Estado Atual       : "+str(fita.retorna_estado()))
			print("    Estados Possíves   : "+str(self.retorna_transicoesPossiveis(fita.retorna_estado())))
			sys.stdout.write("    ")
			print("_"* 146)
		print("_"* 150)
	
	def adiciona_fita(self,fita):
		self.fitas.append(fita)

	def remove_fita(self,fita):
		self.fitas.remove(fita)
	
	def clonar_unicaFita(self,fita):
		return copy.deepcopy(fita)
	
	def clonar_todasFitas(self):
		return copy.deepcopy(self.fitas)

	def transicao(self, fita): #colocar essa função dentro da maquina também
		stateTransitions = self.transicoes[fita.retorna_estado()]
		currentHead = fita.ler_fita()
		if currentHead in stateTransitions:
			transi = stateTransitions[currentHead]
			if len(transi) == 0:
				if(len(self.fitas)>1):
					print("\nNão há Estados Possíveis Para fita "+str(self.fitas.index(fita))+'.')
					return 1

				else:
					print("\nPalavra Rejeitada")
					exit(1)

			elif len(transi) == 1:
				fita.escrever_fita(transi[0][1])
				fita.move_cabeca(transi[0][2])
				fita.mudar_estado(transi[0][0])

				return None 

			elif len(transi) > 1:
				novasFitas = []
				for i in transi:
					fita2 = self.clonar_unicaFita(fita)
					fita2.escrever_fita(i[1])
					fita2.move_cabeca(i[2])
					fita2.mudar_estado(i[0])
					novasFitas.append(fita2)
					#cria a copia de uam fita, movimenta para as possiveis transações e anexa a fita a uma nova lista removendo a si mesma da lista anterior
					# a lista anterior recebe as novas fitas menos a original

				self.remove_fita(fita)
				return novasFitas

			else:
				return None
		else:
			if(len(self.fitas)>1):
				print("\nNão há Estados Possíveis Para fita "+str(self.fitas.index(fita))+'.')
				return 1

			else:
				print("\nPalavra Rejeitada.")
				exit(1)
