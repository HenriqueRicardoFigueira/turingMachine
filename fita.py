#!/usr/bin/python
# -*- coding: utf-8 -*-

class Fita:
    def __init__(self, palavra, alfaEntrada, alfaFita, branco, estadoInicial):
        self.alfabeto = ''.join(alfaFita) #atribui o alfabeto de entrada
        self.alfabeto = self.alfabeto + branco
        self.branco = branco #atribui o simbolo branco
        self.alfabetoFita = alfaFita #atribui o alfabeto completo da fita (X, B, 0, 1, etc)
        
        self.incializa_fita(''.join(palavra))#atribui a palavra de entrada
        self.posicao_cabeca = 1
        self.estado = estadoInicial

    def incializa_fita(self, palavras): #inicializa o conteúdo da fita
        self._fita = self.branco
        for char in (c for c in palavras if c in self.alfabeto):
            self._fita += char
        self._fita += self.branco
        self._fita = list(self._fita)

    def retorna_estado(self):
        return str(self.estado)
        
    def mudar_estado(self, novoEstado):
        self.estado = novoEstado

    def escrever_fita(self, char):#escreve na fita
        ultima_pos_fita = len(self._fita) - 1

        if char not in self.alfabetoFita:
            return

        if self.posicao_cabeca < 1: #estende a esquerda
            aux = char + ("".join(self._fita[1:]))
            aux = self.branco + aux
            self._fita = list(aux)
            self.posicao_cabeca += 1
        
        if self.posicao_cabeca >= 1:#estende a direita
            self._fita[self.posicao_cabeca] = char
            ultima_pos_fita = len(self._fita) - 1
            if self.posicao_cabeca == ultima_pos_fita:
                self._fita += self.branco

       # if self.posicao_cabeca == ultima_pos_fita:
        #        self._fita += self.branco

    def ler_fita(self):#retorna elemento da fita na posicao que a cabeca aponta 
        if((self.posicao_cabeca < 0) or (self.posicao_cabeca > len(self._fita) - 1)):#valida
            return 
        return self._fita[self.posicao_cabeca]

    def retorna_fita(self):#retorna a fita
        self.remove_brancos() 
        return ''.join(self._fita)

    def remove_brancos(self):
        for i in range(len(self._fita) - 1, 1, -1):
            if self._fita[i] == self.branco and self._fita[i-1] == self.branco:
                del self._fita[-1:]
            else:
                break

    def move_cabeca(self, direcao):
        if direcao == 'R':
            self.posicao_cabeca += 1
        elif direcao == 'L':
            self.posicao_cabeca -= 1

        if self.posicao_cabeca > len(self._fita) - 1:
            self._fita += self.branco
        if self.posicao_cabeca < 0:
            self.posicao_cabeca = 0

    def retorna_tamanho(self):
        return len(self._fita)