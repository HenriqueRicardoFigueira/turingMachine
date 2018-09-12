#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, random
from maquina import Maquina

class Turing:

    #tudo no fim acho que vira maquina
    def __main__(self):
        #aqui só para debbug
        modo = raw_input("Selecione o modo que deseja executar a Máquina e Aperte Enter.\nA - Automático\nM - Manual (Passo a Passo)\n")

        #cria a Maquina e a Fita Inicial
        maquina = Maquina(sys.argv)
        while(True):
            #aqui de debbug tb
            maquina.print_fitas()
            if modo.capitalize() == "M".capitalize(): tst = raw_input("\nAperte Enter Para Prosseguir.")

            novasFitas = []
            #correr as fitas ver se o estado das fitas algum deles é o final
            for fita in maquina.fitas:
                #verifica o ofim da máquina ou não
                if maquina.verifica_estadoFinal(fita):
                    exit(0)
                
                #movimenta a maquina
                ret = maquina.transicao(fita)

                #caso haja novas fitas remover a fita de origem
                if type(ret) is list:
                    novasFitas+=ret
                
                if type(ret) is int:
                    maquina.print_fitas()
                    maquina.remove_fita(fita)
                    if modo.capitalize() == "M".capitalize(): tst = raw_input("\nAperte Enter Para Prosseguir.")

            #se houverem novas fitas..
            if(novasFitas != None):
                for newFita in novasFitas:
                    maquina.adiciona_fita(newFita)

Turing().__main__()
