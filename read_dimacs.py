import argparse


class Instance:
    """
    Represents an instance for 3-SAT problem
    """

    def __init__(self, nb_var, constraints):
        self.nb_var = nb_var
        self.constraints = constraints

    def __repr__(self):
        s = 'nb Var : {} nb Const {}\n\n'.format(self.nb_var, len(self.constraints))
        for i in self.constraints:
            s += ' '.join([str(j) for j in i])+'\n'
        return s


def read_dimacs(filename):
    """
    reads a dimacs format file and return an instance of 3SAT problem
    :param filename: input file
    :return: Instance of problem in filename
    """

    with open(filename, 'r') as f:
        n, m, c = None, None, []
        nb_read = 0
        for l in f.readlines():
            if l[0] != 'c':
                if n is None:
                    # in this case, fill n et m
                    n, m = [int(i) for i in l.split()[2:4]]
                elif nb_read < m:
                    c.append([int(i) for i in l.split()[:-1]])
                    nb_read += 1
    return Instance(n, c)


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Generates instance object with a dimacs format file.')
    parser.add_argument('filename', metavar='F', type=str, help='dimacs filename')
    args = parser.parse_args()
    print(read_dimacs(args.filename))
