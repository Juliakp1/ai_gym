from aigyminsper.search.SearchAlgorithms import BuscaLargura, BuscaProfundidadeIterativa, BuscaProfundidade, BuscaCustoUniforme
from aigyminsper.search.Graph import State
from datetime import datetime
import json

class BetweenPoints(State):

    def __init__(self, op, startCity, endCity, dist, map):
        self.operator = op
        self.pos = startCity
        self.end = endCity
        self.dist = dist
        self.map = map

    def sucessors(self):
        sucessors = []
        
        newPosOptions = self.map[self.pos]
        for newPos in newPosOptions:
            pos = newPos[1]
            dist = newPos[0]
            sucessors.append(BetweenPoints(pos, pos, self.end, dist, self.map))

        return sucessors

    def is_goal(self):
        if (self.pos == self.end):
            return True
        return False

    def description(self):
        return "Finds the shortest path between two cities, using a json as a map"

    def cost(self):
        return self.dist

    def env(self):
        return self.dist

def main(city1, city2):

    print('\nRunning! \n')

    with open('cities\map.json', 'r') as arquivo_json:
        mapJson = arquivo_json.read()
    map = json.loads(mapJson)

    state = BetweenPoints('', city1, city2, 0, map)
    algorithm = BuscaCustoUniforme()
    result = algorithm.search(state)

    if result != None:
        print('Found it!')
        print(f'Cost: {result.g}')
        print(result.show_path())
    else:
        print('Oops! no solution :/')


if __name__ == '__main__':
    main('i', 'x')

#   BuscaCustoUniforme
# Cost: 8 -- e ; d ; c ; o
# Cost: 9 -- h ; g ; c ; o
# Cost: 12 - h ; k ; n ; m ; x