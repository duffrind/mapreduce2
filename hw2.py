from mrjob.job import MRJob

class prob1(MRJob): # total number of words
    def mapper(self, _, line):
        #yield "chars", len(line)
        yield "words", len(line.split())
        #yield "lines", 1
    def reducer(self, key, values):
        yield key, sum(values)

class prob2(MRJob): # count "the"
    def mapper(self, _, line):
        for word in line.split():
            if word.lower() == 'the':
                yield 'the', 1
    def reducer(self, key, values):
        yield key, sum(values)

class prob3(MRJob): # count n-letter words - I changed this from 3-letter
    def mapper(self, _, line):
        for word in line.split():
            yield len(word), 1
    def reducer(self, key, values):
        yield key, sum(values)

class prob4(MRJob): # number of words that start with each letter
    def mapper(self, _, line):
        for word in line.split():
            yield word[0].lower(), 1
    def reducer(self, key, values):
        yield key, sum(values)

class prob5(MRJob): # average number of vowels for each word length
    def mapper(self, _, line):
        for word in line.split():
            yield len(word), len([v for v in word.lower() if v in 'aieouy'])
    def reducer(self, key, values):
        v = list(values)
        yield key, sum(v)/len(v)

class prob6(MRJob): # average number of vowels for each word length
    def mapper(self, _, line):
        for word in line.split():
            yield len(word), len([v for v in word.lower() if v in 'aieouy'])
    def reducer(self, key, values):
        v = list(values)
        yield key, sum(v)/len(v)


if __name__ == '__main__':
    prob1.run()
    prob2.run()
    prob3.run()
    prob4.run()
    prob5.run()
    prob6.run()
