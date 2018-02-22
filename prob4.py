from mrjob.job import MRJob

class prob(MRJob): # smallest, largest, and averagest population
    def mapper(self, _, line):
        try:
            population = int(line.split(',')[-1])
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
