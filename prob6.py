from mrjob.job import MRJob
from mrjob.step import MRStep
from random import randint

i = 0
j = 50

class prob(MRJob):
    def steps(self):
        return [MRStep(mapper=self.mapper,
                   reducer=self.reducer1),
                MRStep(reducer=self.reducer2)]
    def mapper(self, _, line):
        global i, j
        try:
            school = line.split(',')[0]
            schooltype = int(line.split(',')[2])
            if schooltype == 1:
                yield str(i), school
                i = (i+1) % 50
            else:
                yield str(j), school
                j = ((j+1) % 50) + 50
        except:
            pass
    def reducer1(self, key, values):
        v = list(values)
        yield 'school', v[randint(0, len(v)-1)]
    def reducer2(self, key, values):
        yield 'schools', values

if __name__ == '__main__':
    prob.run()
