#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, os, copy
from fita import Fita
from maquina import Maquina

def main():
    #aqui só para debbug
    os.system('cls' if os.name == 'nt' else 'clear')
    modo = raw_input("Selecione o modo que deseja executar a Máquina e Aperte Enter.\nA - Automático\nM - Manual (Passo a Passo)\n")

    #inicializa a Maquina e a Fita
    maquina = Maquina(sys.argv)
    maquina.changeCurrentState(maquina.initialState)
    fita = Fita( maquina.contentTape, maquina.inputAlpha, maquina.tapeAlpha, maquina.branco)

    #aqui só para debbug
    os.system('cls' if os.name == 'nt' else 'clear')
    print "Estado Atual Fita: "+fita.retorna_fita()
    print "Possíveis Estados: "+str(maquina.retorna_estadosPossiveis(maquina.initialState))
    if modo.capitalize() == "M".capitalize(): tst = raw_input("Aperte Enter Para Prosseguir.")

    #pega os estados possiveis
    ntxState =  maquina.transition(maquina.initialState,fita)
    
    x = True
    while(x == True):
        #aqui só para debbug
        os.system('cls' if os.name == 'nt' else 'clear')
        print "Estado Atual Fita: "+fita.retorna_fita()
        print "Possíveis Estados: "+str(maquina.retorna_estadosPossiveis(ntxState[0]))
        if modo.capitalize() == "M".capitalize(): tst = raw_input("Aperte Enter Para Prosseguir.")

        #pega os estados possiveis
        ntxState = maquina.transition(ntxState[0],fita)

        #verifica o ofim da máquina ou não
        if maquina.getCurrentState() in maquina.finalStates:
            print "\nResultado: Palavra Aceita"
            x = False
            return 0
        if ntxState == None:
            print "\nResultado: Palavra Rejeitada"
            return 1

main()
