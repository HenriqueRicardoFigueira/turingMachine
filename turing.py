#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, random
from maquina import Maquina

class Turing:

    #tudo no fim acho que vira maquina
    def __main__(self):
        #aqui só para debbug
        modo = raw_input("Selecione o modo que deseja executar a Máquina e Aperte Enter.\nA - Automático\nM - Manual (Passo a Passo)\n")

        #inicializa a Maquina e a Fita
        maquina = Maquina(sys.argv)

        while(True):
            #aqui de debbug tb
            maquina.print_fitas()
            if modo.capitalize() == "M".capitalize(): tst = raw_input("\nAperte Enter Para Prosseguir.")
            print("\n")

            #correr as fitas ver se o estado das fitas algum deles é o final
            for fita in maquina.fitas:
            #verifica o ofim da máquina ou não
                if maquina.verifica_estadoFinal(fita):
                    exit(0)

                maquina.transicao(fita)

turing = Turing()
turing.__main__()
