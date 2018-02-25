from mrjob.job import MRJob

class prob(MRJob): # Normal Equation
    def mapper(self, _, line):
        try:
            values = line.split(',')
            pop = int(values[-1])
            area = int(values[])
            yield 'state', population
        except:
            pass
    def reducer(self, key, values):
        v = list(values)
        yield 'smallest', min(v)
        yield 'largest', max(v)
        yield 'averagest', sum(v)/len(v)

if __name__ == '__main__':
    prob.run()
