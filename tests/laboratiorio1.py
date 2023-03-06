from aigyminsper.search.SearchAlgorithms import BuscaLargura
from aigyminsper.search.SearchAlgorithms import BuscaProfundidade
from aigyminsper.search.SearchAlgorithms import BuscaProfundidadeIterativa
from aigyminsper.search.Graph import State
from datetime import datetime

class SumOne(State):

    def __init__(self, n, op, g):
        self.operator = op
        self.number = n
        self.goal = g

    def sucessors(self):
        sucessors = []
        sucessors.append(SumOne(self.number+1, "+1 ", self.goal))
        sucessors.append(SumOne(self.number+2, "+2 ", self.goal))
        return sucessors

    def is_goal(self):
        if self.goal == self.number:
            return True
        return False

    def description(self):
        return "Este é um agente simples que sabe somar 1 e 2"

    def cost(self):
        return 1

    def env(self):
        return self.number

def main():

    # objetivo = int(input('Digite o valor objetivo: '))

    print('')
    print('Algoritimo: BuscaProfundidade - m=50')
    print('')
    # algorithm = BuscaLargura()
    algorithm = BuscaProfundidade()
    # algorithm = BuscaProfundidadeIterativa()

    depth = 50

    # Start at 1, else it will try to find 0
    for objetivo in range(40, 45):
        state = SumOne(1, '', objetivo)

        start_time = datetime.now()
        result = algorithm.search(state, depth)
        end_time = datetime.now()

        if result != None:
            print(f'{objetivo} - Tempo = {end_time - start_time}')
        else:
            print('Nao achou solucao')

if __name__ == '__main__':
    main()