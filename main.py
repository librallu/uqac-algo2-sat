import argparse
import random
from read_dimacs import *
from evolutionnary import *
import functools


def choice(population, nb=2):
    """
    return an element within the population
    :param population: population
    :return: element to return
    """
    l = random.sample(population, nb)
    evaluation = [i.evaluate() for i in l]
    remaining = []
    best = min(evaluation)
    for i, a in enumerate(l):
        if evaluation[i] == best:
            remaining.append(a)
    return random.sample(remaining, 1)[0]


def select(population, n=100):
    """

    :param population:
    :param n:
    :return:
    """
    if len(population) <= n:
        return population
    else:
        selected = []
        for _ in range(n):
            s = choice(population)
            selected.append(s)
            population.remove(s)
        return selected


def mutate(population):
    """
    mutate the entiere population
    :param population: population to mutate
    :return: mutated population
    """
    return [i.mutate() for i in population]


def select_reproduction(population, choice_fct=choice):
    """
    selects two parents and return their child
    :param population: current population
    :return: child of two parents chosen by choice function
    """
    return reproduce(choice_fct(population), choice_fct(population))



def solve(inst, n=100, max_steps=25):
    """
    solve problem
    :param inst: instance to solve
    :param n: length of population
    :return: best solution found
    """

    # initiate population
    pop = []
    for i in range(n):
        pop.append(Solution(inst))

    best = min([i.evaluate() for i in pop])

    nb_steps = 0
    while nb_steps < max_steps and best > 0:  # continue until feasible solution is found

        # individual selection
        pop = select(pop, n)

        # reproduction
        for _ in range(n):
            pop.append(select_reproduction(pop))

        # mutation
        pop = mutate(pop)

        # best update
        best = min([i.evaluate() for i in pop])
        nb_steps += 1

    return best




if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Generates instance object with a dimacs format file.')
    parser.add_argument('filename', metavar='F', type=str, help='dimacs filename')
    args = parser.parse_args()
    inst = read_dimacs(args.filename)

    l = []
    for _ in range(10):
        tmp = float(solve(inst, n=100))
        print(tmp)
        l.append(tmp)

    print("mean: {}".format(functools.reduce(lambda x, y: x+y, l)/len(l)))
