class configMachine:

	def changeCurrentState(newcurrent):
    		global currentState
    		currentState = newcurrent

	def currentState():
    		global currentState
    		return str(currentState)

	def isFinal(state):
    		if state in finalStates:
        		return True
   		 else:
        		return False

	def isInitial(state):
    		if str(state) == initialState:
        		return  True
    		else:
        		return False

	def getCurrentState():
    		return currentState

	def transition(iniState,tape):
    		runing = True
    		global finalStates
    		global blank
    		global transitions
    		stateTransitions = transitions[iniState]
    		currentHead = tape.read()
    		print getCurrentState()
    		if currentHead in stateTransitions:
        		transi = stateTransitions[currentHead]
        	if len(transi) == 0:
            		return 1
        	elif len(transi) == 1:
            		aux = transi[0]
            		tape.write(aux[1])
            		tape.move_head(aux[2])
            		changeCurrentState(aux[0])
            		return aux   
        	elif len(transi) > 1:
            		return transi
        	else:
            		return None
   	 	else:
        		return None
