#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, os, copy
from fita import Fita
from maquina import Maquina

class Turing:

    fitas = []

    def transition(self,iniState,fita, maquina):
        stateTransitions = maquina.transitions[iniState]
        currentHead = fita.ler_fita()
        if currentHead in stateTransitions:
            transi = stateTransitions[currentHead]
            if len(transi) == 0:
                return 1
            elif len(transi) == 1:
                aux = transi[0]
                fita.escrever_fita(aux[1])
                fita.move_cabeca(aux[2])
                maquina.changeCurrentState(aux[0])
                return aux   
            elif len(transi) > 1:
                newFitas = []

                for i in transi:
                    fita2 = copy.deepcopy(fita)
                    fita2.escrever_fita(i[1])
                    fita2.move_cabeca(i[2])
                    newFitas.append(fita2)
                    #cria a copia de uam fita, movimenta para as possiveis transações e anexa a fita a uma nova lista removendo a si mesma da lista anterior
                    # a lista anterior recebe as novas fitas menos a original

                self.fitas.remove(fita)              

                for i in newFitas:
                    self.fitas.append(i)

                return transi[len(transi)-1]

            else:
                return None
        else:
            if(len(self.fitas)>1):
                print("Não há Estados Possíveis Para fita"+str(self.fitas.index(fita)))
                self.fitas.remove(fita)
                #return self.fitas[1]

            else:
                print("Palavra Rejeitada")
                exit(1)

    def __main__(self):
        #aqui só para debbug
        os.system('cls' if os.name == 'nt' else 'clear')
        modo = raw_input("Selecione o modo que deseja executar a Máquina e Aperte Enter.\nA - Automático\nM - Manual (Passo a Passo)\n")

        #inicializa a Maquina e a Fita
        maquina = Maquina(sys.argv)
        maquina.changeCurrentState(maquina.initialState)
        fita = Fita(maquina.contentTape, maquina.inputAlpha, maquina.tapeAlpha, maquina.branco)
        self.fitas.append(fita)

        #aqui só para debbug
        #os.system('cls' if os.name == 'nt' else 'clear')
        for fit in self.fitas:
            print "\n"
            print "Estado Atual Fita: "+str(self.fitas.index(fit))+": "+fit.retorna_fita()
            #print "Possíveis Estados: "+str(maquina.retorna_transicoesPossiveis(maquina.initialState))
        #if modo.capitalize() == "M".capitalize(): tst = raw_input("Aperte Enter Para Prosseguir.")

        #pega as transicoes possiveis
        ntxState =  self.transition(maquina.initialState,self.fitas[len(self.fitas)-1],maquina)
        
        x = True
        while(x == True):
            print("len:" + str(len(ntxState)))
            for fit in self.fitas:
                print "Conteudo Atual Fita: "+str(self.fitas.index(fit))+": "+fit.retorna_fita()
                print(maquina.getCurrentState())
                print "\n"
                #print "Possíveis Estados: "+str(maquina.retorna_transicoesPossiveis(maquina.initialState))
                #print "Possíveis Transicoes: "+str(maquina.retorna_transicoesPossiveis(ntxState[0]))
            #if modo.capitalize() == "M".capitalize(): tst = raw_input("Aperte Enter Para Prosseguir.")


            newNtxState = []
            
            for fit in self.fitas:
                newNtxState.append(self.transition(ntxState[0][0],fit, maquina))
            
            ntxState = newNtxState
            #verifica o ofim da máquina ou não

            #for fit in self.fitas:
             #   print "Estado Atual Fita: "+str(self.fitas.index(fit))+": "+fit.retorna_fita()
              #  print "Possíveis Estados: "+str(maquina.retorna_transicoesPossiveis(maquina.initialState))

            if maquina.getCurrentState() in maquina.finalStates:
                print "\nResultado: Palavra Aceita"
                x = False
                return 0
            if ntxState == None:
                print "\nResultado: Palavra Rejeitada"
                return 1

turing = Turing()
turing.__main__()
