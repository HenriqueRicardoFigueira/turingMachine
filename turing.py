#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, copy, random
from fita import Fita
from maquina import Maquina

class Turing:

    fitas = [] #passar as fita e a remoção das fitas pra maquina manipular

    def transition(self,iniState,fita, maquina): #colocar essa função dentro da maquina também
        stateTransitions = maquina.transitions[iniState]
        currentHead = fita.ler_fita()
        if currentHead in stateTransitions:
            transi = stateTransitions[currentHead]
            if len(transi) == 0:
                if(len(self.fitas)>1):
                    print("Não há Estados Possíveis Para fita "+str(self.fitas.index(fita))+'.')
                    maquina.print_fitas(self.fitas)
                    print("\n")

                    return None

                else:
                    print("Palavra Rejeitada")
                    exit(1)

            elif len(transi) == 1:
                aux = transi[0]
                fita.escrever_fita(aux[1])
                fita.move_cabeca(aux[2])
                fita.mudar_estado(aux[0])

                return None 

            elif len(transi) > 1:
                newFitas = []

                for i in transi:
                    fita2 = copy.deepcopy(fita)
                    fita2.escrever_fita(i[1])
                    fita2.move_cabeca(i[2])
                    fita2.mudar_estado(i[0])
                    newFitas.append(fita2)
                    #cria a copia de uam fita, movimenta para as possiveis transações e anexa a fita a uma nova lista removendo a si mesma da lista anterior
                    # a lista anterior recebe as novas fitas menos a original

                self.fitas.remove(fita)   

                for i in newFitas:
                    self.fitas.append(i)
  
                #return transi[len(transi)-1]
                return None

            else:
                return None
        else:
            if(len(self.fitas)>1):
                print("Não há Estados Possíveis Para fita "+str(self.fitas.index(fita))+'.')
                maquina.print_fitas(self.fitas)
                print("\n")
                self.fitas.remove(fita)
                return None

            else:
                 print("Palavra Rejeitada")
                 exit(1)
            #return None

    def __main__(self):
        #aqui só para debbug
        modo = raw_input("Selecione o modo que deseja executar a Máquina e Aperte Enter.\nA - Automático\nM - Manual (Passo a Passo)\n")

        #inicializa a Maquina e a Fita
        maquina = Maquina(sys.argv)
        maquina.changeCurrentState(maquina.initialState)

        #INICIALIZAR DENTRO DA MAQUINA MESMO E MANIPULAR POR LA ATRAVEZ DE UMA FUNÇÃO
        fita = Fita(maquina.contentTape, maquina.inputAlpha, maquina.tapeAlpha, maquina.branco) #<- ESSA INICIALIZAR DENTRO DA MAQUINA MESMO E MANIPULAR POR LA
        fita.mudar_estado(maquina.initialState)#<- ESSA INICIALIZAR DENTRO DA MAQUINA MESMO E MANIPULAR POR LA
        self.fitas.append(fita)#<- ESSA INICIALIZAR DENTRO DA MAQUINA MESMO E MANIPULAR POR LA
        

        #aqui só para debbug
        maquina.print_fitas(self.fitas) #<-aqui não precisará passar as fitas pois elas ja estarão dentro da maquina
        if modo.capitalize() == "M".capitalize(): tst = raw_input("\nAperte Enter Para Prosseguir.")
        print("\n")

        #pega as transicoes possiveis iniciais
        self.transition(maquina.initialState,self.fitas[len(self.fitas)-1],maquina)
        
        x = True
        while(x == True):
            #aqui de debbug tb
            maquina.print_fitas(self.fitas)
            if modo.capitalize() == "M".capitalize(): tst = raw_input("\nAperte Enter Para Prosseguir.")
            print("\n")
            
            aux = []
            #correr as fitas ver se o estado das fitas algum deles é o final
            for fit in self.fitas:
                #verifica o ofim da máquina ou não
                if fit.retorna_estado() in maquina.finalStates:  #<- utilizar validação dentro da mauina mesmo
                #há validações dentro da função transition que devem ser melhoradas ou abstraidas para melhor entendimento do codigo
                    print "\nResultado: Palavra Aceita"#<- utilizar validação dentro da mauina mesmo
                    print(len(self.fitas))#<- utilizar validação dentro da mauina mesmo
                    print(fit.retorna_estado())#<- utilizar validação dentro da mauina mesmo
                    x = False#<- utilizar validação dentro da mauina mesmo (retornar aqui o valor booleano com a chamada de uma função )
                    exit(0)

                if(fit not in aux):#<- função pra executar a máquina
                    aux.append(fit)
                    iniState = fit.retorna_estado()
                    self.transition(iniState,fit, maquina)

turing = Turing()
turing.__main__()
