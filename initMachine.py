#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import copy
import fita

tape = []
element = []
inputAlpha = []
tapeAlpha = []
blank = ""
argsFitas = []
states = []
initialState = ""
finalStates = []
contentTape = []
transitions = {}
transitionsArq = []
currentState = ""

name = sys.argv[1]

#LEITURA_ARQUIVO/ CRIAÇÃO DE LISTAS
for x in range(2,(len(sys.argv))):
    aux = sys.argv[x]
    contentTape.append(aux)

arq = open(name,'r')

elements = arq.read().splitlines()

#ALFABETO_ENTRADA
inputAlpha = elements[0].split(" ")

#ALFABETO_FITA
tapeAlpha = elements[1].split(" ")

#BRANCO
branco = elements[2]

#ESTADOS
states = elements[3].split(" ")

#INICIAL
initialState = elements[4].strip()

#FINAL
finalStates = elements[5].split(" ")


qtTape = int(elements[6])

transitionsaux = {}

transitions = {}

#TRASIÇÕES
for k in elements[7:]:
    transitionsArq.append(k)


for s in states:
    aux2 = []
    for t in transitionsArq:
        aux = t.split(" ")
        if s == aux[0]:
            aux2.append(aux[1:])
    transitionsaux[s]=[aux2]

for s in states:
    aux3 = transitionsaux[s]
    aux4 = aux3[0]

    auxft = []
    auxsimbol = {}
    
    for tr in aux4:
        if tr[1] in auxsimbol:
            traxx = (tr[0],tr[2],tr[3])
            auxsimbol[tr[1]].append(traxx)
        else:
            traxx = (tr[0],tr[2],tr[3])
            auxsimbol[tr[1]]= [traxx]

    transitions[s] = auxsimbol


def main():
    global states
    global finalStates
    global branco
    global tapeAlpha
    global contentTape
    global transitions
    changeCurrentState(initialState)
    tape = Tape(contentTape, inputAlpha, tapeAlpha, branco)
    ntxState =  transition(initialState,tape)
    x = True
    while(x == True):
        ntxState = transition(ntxState[0],tape)
        if getCurrentState() in finalStates:
                print "aceito"
                x = False
                return 0
        if ntxState == None:
            print "não aceito"
            return 1

main()
