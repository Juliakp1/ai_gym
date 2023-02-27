from aigyminsper.search.SearchAlgorithms import BuscaProfundidadeIterativa
from aigyminsper.search.Graph import State
import copy

class AspiradorPo10x10(State):

    def __init__(self, op, posRob, rotation, dirtyList):

        self.operator = op      # You must use this name for the operator!
        
        self.pos = posRob       # Index of the dirty list (x,y)
        self.rot = rotation     # Rotation, compass based 
        self.dirty = dirtyList  # List of rooms (1 is dirty, 0 is clean)

    # ----------------------------------- #
    
    def turn_compass(self, offset, currentSide):
        rose = ['n', 'e', 's', 'w']             # Like a compass, clockwise starting at 12
        index = rose.index(currentSide)
        newIndex = index + offset
        if newIndex < 0:
            newIndex = 3
        elif newIndex >= 4:
            newIndex = 0
        return rose[newIndex]
    
    # ----------------------------------- #

    def go_fowards(self, pos, rot, lenList):
        if rot == 'n':
            newPos = [ max(pos[0] - 1, 0) , pos[1]]
        elif rot == 's':
            newPos = [ min(pos[0] + 1, lenList), pos[1]]
        elif rot == 'e':
            newPos = [pos[0], min(pos[1] + 1, lenList)]
        elif rot == 'w':
            newPos = [pos[0], max(pos[1] - 1, 0)]
        return newPos

    # ----------------------------------- #

    def sucessors(self):
        sucessors = []

        currentPos = copy.deepcopy(self.pos)
        currentRotation = copy.deepcopy(self.rot)
        currentRooms = copy.deepcopy(self.dirty)

        # Turn left
        newRotLeft = self.turn_compass(-1, currentRotation)                              
        sucessors.append(AspiradorPo10x10('Turn left', currentPos, newRotLeft, self.dirty))

        # Turn right
        newRotRight = self.turn_compass(1, currentRotation)                               
        sucessors.append(AspiradorPo10x10('Turn right', currentPos, newRotRight, self.dirty))

        # Go foward
        newPos = self.go_fowards(currentPos, currentRotation, (len(self.dirty)-1))
        sucessors.append(AspiradorPo10x10('Fowards', newPos, currentRotation, self.dirty))
        
        # Clean
        currentRooms[currentPos[0]][currentPos[1]] = 0
        sucessors.append(AspiradorPo10x10('Clean', currentPos, currentRotation, currentRooms))

        return sucessors
    
    # ----------------------------------- #

    def is_goal(self):
        for row in self.dirty:
            for room in row:
                if room != 0:       # AKA the room is not clean (not 0)
                    return False
        return True

    # ----------------------------------- #
    
    def description(self):
        return "Descrição do problema"

    # ----------------------------------- #
    
    def cost(self):
        return 1

    # ----------------------------------- #
    
    def env(self):
        #
        # IMPORTANTE: este método não deve apenas retornar uma descrição do environment, mas 
        # deve também retornar um valor que descreva aquele nodo em específico. Pois 
        # esta representação é utilizada para verificar se um nodo deve ou ser adicionado 
        # na lista de abertos.
        #
        # Exemplos de especificações adequadas: 
        # - para o problema do soma 1 e 2: return str(self.number)+"#"+str(self.cost)
        # - para o problema das cidades: return self.city+"#"+str(self.cost())
        #
        # Exemplos de especificações NÃO adequadas: 
        # - para o problema do soma 1 e 2: return str(self.number)
        # - para o problema das cidades: return self.city
        #
        # return str(self.pos)+'#'+str(self.dirty)
        None

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #

def main():
    print('Busca em profundidade iterativa')

    # ----------------------------------- #

    startingPos = [0, 0]
    #                                        n
    rotation = 'e'              # can be:  w   e            Starts facing east
    #                                        s
    roomsDirty2 = [
        [1, 1],
        [1, 1],
    ]

    roomsDirty10 = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    ]

    # ----------------------------------- #

    state = AspiradorPo10x10('Start', startingPos, rotation, roomsDirty2)
    algorithm = BuscaProfundidadeIterativa()
    result = algorithm.search(state)
    if result != None:
        print('Achou!')
        print(result.show_path())
    else:
        print('Nao achou solucao')

if __name__ == '__main__':
    main()