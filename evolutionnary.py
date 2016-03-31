import random


class Solution:

    def __init__(self, inst):
        """
        constructs a random solution for an instance
        :param inst: instance of a problem
        """
        self.n = inst.nb_var
        self.inst = inst
        self.vector = []
        for i in range(self.n):
            self.vector.append(True if random.random() <= 0.5 else False)

    def __repr__(self):
        return ' '.join(['0' if i else '1' for i in self.vector])

    def evaluate(self):
        """
        Compute the number of conflicts for the current solution
        :return:
        """
        res = 0
        for i in self.inst.constraints:
            nb_ok = 0
            for j in i:
                if (j > 0 and self.vector[j-1]) or (j < 0 and not self.vector[-j-1]):
                    nb_ok += 1
            if nb_ok == 0:
                res += 1

        return res

    def mutate(self, mutation_threshold=0.1, mutation_factor=0.5):
        """
        mutates the solution
        :param mutation_threshold: probability to have a mutation
        :param mutation_factor: probability to mute a given variable in solution
            when the mutation occurs
        """
        if random.random() < mutation_threshold:
            for i, a in enumerate(self.vector):
                if random.random() < mutation_factor:
                    self.vector[i] = not a
        return self


def reproduce(*solution_list):
    """
    creates a new solution from
    :param solution_list:
    :return: a new solution combination of solution_list for parents
    """
    l = len(solution_list)
    new_vector = []
    for i, _ in enumerate(solution_list[0].vector):
        new_vector.append(solution_list[int(random.random()*l)].vector[i])
    res = Solution(solution_list[0].inst)
    res.vector = new_vector
    return res
