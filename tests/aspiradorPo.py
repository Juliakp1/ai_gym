from aigyminsper.search.SearchAlgorithms import BuscaProfundidade
from aigyminsper.search.Graph import State
import copy

class AspiradorPo(State):

    def __init__(self, op, posRob, dirtyList):

        self.operator = op      # You must use this name for the operator!
        
        self.pos = posRob       # Index of the dirty list 
        self.dirty = dirtyList  # List of rooms (1 is dirty, 0 is clean)
    
    # ----------------------------------- #

    def sucessors(self):
        sucessors = []

        currentPos = copy.deepcopy(self.pos)
        currentRooms = copy.deepcopy(self.dirty)
        print(currentPos, self.dirty)

        # Go left
        leftPos = max(currentPos - 1, 0)                                # Biggest value between one to the left and the first room
        sucessors.append(AspiradorPo('Left', leftPos, self.dirty))

        # Go right
        rightPos = min(currentPos + 1, len(currentRooms)-1)             # Lowest value between one to the right and the last room
        sucessors.append(AspiradorPo('Right', rightPos, self.dirty))
        
        # Clean
        currentRooms[currentPos] = 0
        sucessors.append(AspiradorPo('Clean', currentPos, currentRooms))

        print(leftPos, rightPos, currentRooms)
        print('--------------')

        return sucessors
    
    # ----------------------------------- #
    
    def show_selves(self):
        print(self.pos , self.dirty)
    
    # ----------------------------------- #

    def is_goal(self):
        for room in self.dirty:
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
    state = AspiradorPo('Start', 0, [1, 1, 1, 1, 1, 1])
    algorithm = BuscaProfundidade()
    depth = 11
    result = algorithm.search(state, depth)
    if result != None:
        print('Achou!')
        print(result.show_path())
    else:
        print('Nao achou solucao')

if __name__ == '__main__':
    main()