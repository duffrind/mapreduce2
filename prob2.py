from mrjob.job import MRJob

class prob(MRJob): # variance of price
    def mapper(self, _, line):
        try:
            price = float(line.split(',')[-1])
            yield 'x', price
        except:
            pass
    def reducer(self, key, values):
        v = list(values)
        average = sum(v)/len(v)
        expected = sum([(val - average)**2 for val in v])
        yield 'variance', expected/(len(v)-1)

if __name__ == '__main__':
    prob.run()
