# turingMachine

## Get Start
Clone ou faça o Download do projeto em .zip (via terminal/manual) para sua maquina.
- Clone:
  - Execute o camando no Terminal e acessa a pasta do projeto:
    ```
    git clone https://github.com/HenriqueRicardoFigueira/turingMachine.git
    cd turingMachine-master/
    ```
- Download:
  - Execute no Terminal de comando:
    ```
    wget https://github.com/HenriqueRicardoFigueira/turingMachine/archive/master.zip
    ```
  - Descompacte e abra a pasta do projeto:
    ```
    unzip turingMachine-master.zip
    cd turingMachine-master/

### Documentação
  #TURING

    #funcionamento:
        *cria máquina e fita inicial, corre as fitas e verificar se algum estado das fitas é o final, movimenta a maquina. Caso haja novas fitas remove a fita de origem.
    
  
  #MAQUINA
    #Atributos:
        contentTape
        alfaEntrada
        alfaFIta
        branco
        estados
        estadoFinal
        tamanhoFita
        transicoes
        fitas
    
    #Funcionamento:
        Carrega o conteudo da fita, quebra o arquivo em linhas e os carrega nos atributos.
    
    #Métodos:
        - def cria_fitaInicial():
            *cria fita inical da máquina.

        - def carrega_maquinaArquivo():
            *carrega todas as transições para uma lista.

        - def grava_transicoesEstadosOrigem():
            *carrega as transiçoes dos estados de origem para uma lista.

        - def grava_transicoesEstadosDestino():
            *carrega as transições dos estados de destino.

        - def verifica_estadoFinal():
            *verifica se o estado atual é o estado final.

        - def retorna_transicoesPossiveis():
            *dado um estado, retorna as transições que são possiveis para ele.

        - def print_fitas():
            *imprime as fitas.

        - def adiciona_fita():
            *adiciona uma fita a listas de fitas.

        - def remove_fita():
            *remove uma fita da lista de fitas.

        - def clonar_unicaFita():
            *copia uma fita da lista de fitas.

        - def clonar_todasFitas():
            *copia a lista de fitas.
        
        - def transicao():
            *retorna as trasições possiveis de um estado, verifica a posição da cabeça da fita e caso não haja transição rejeita a palavra, se houver transição possivel vai para ela, escreve na fita, move a cabeça e muda o estado.

            #Não determinismo
                *cria a copia de uam fita, movimenta para as possiveis transações e anexa a fita a uma nova lista removendo a si mesma da lista anterior a recebe as novas fitas menos a original.
  #FITA
    #Atributos:
        alfabeto
        branco
        alfabetofita
        inicializa_fita
        posicao_cabeca
        estadoInicial 
        estado

    #Métodos:
        - def inicializa_fita():
             *inicializa o conteúdo da fita.

        - def retorna_estado():
              *retorna o estado atual.

        - def mudar_estado():
              *muda o estado atual.
      
        - def escrever_fita():
              *escreve na fita
                implementado controle para caso estender para a direita ou esquerda.
      
        - def ler_fita():
              *retorna elemento da fita na posicao que a cabeça aponta.
      
        - def retorna_fita():
              *retorna a fita

        - def remove_brancos():
              *remove os brancos
      
        - def move_cabeca():
              *move a cabeca para direita ou esquerda.

        - def retorna_tamanho(): 
              *retorna tamanho da fita.

        - def verifica_estadoInicial():
              *verifica se o estado atual é o estado inicial.


### Passos para Execução:
- Execute o seguinte comando no terminal:
  ```
  python turing.py examples/(NOME DO ARQUIVO DA MAQUINA) "CONTEUDO DA FITA"
  ```
## Observações
Se você ja está perdido a ponto de ter chegado até aqui, vá em frente e se afunde de uma vez! :trollface:
## Autor
[Gabriel Negrão Silva](https://github.com/itsgnegrao). :alien:

[Henrique Ricardo Figueira](https://github.com/HenriqueRicardoFigueira). :alien:
