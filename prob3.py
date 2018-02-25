from mrjob.job import MRJob
import numpy as np

class prob(MRJob): # Normal Equation
    def mapper(self, _, line):
        try:
            values = line.split(',')
            area = int(values[3])
            pop = int(values[4])
            yield 'data', ((1, area), pop)
        except:
            pass
    def reducer(self, key, values):
        v = list(values)
        X, Y = zip(*v)
        X = np.array(X)
        Y = np.array(Y)
        Y.shape = (52,1)
        betas = np.dot(np.linalg.inv(np.dot(X.T, X)), np.dot(X.T, Y))
        yield 'alpha', betas[0][0]
        yield 'beta', betas[1][0]

if __name__ == '__main__':
    prob.run()
