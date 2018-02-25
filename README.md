# mapreduce2

Homework 2 for Distributed Computing (Python + MrJob)

To run:

`python prob1.py states.csv > output1.txt`

`python prob2.py electricity.csv > output2.txt`

`python prob3.py states.csv > output3.txt`

`python prob4.py electricity.csv states.csv > output4.txt`

`python prob5.py colleges.csv > output5.txt`

`python prob6.py colleges.csv > output6.txt`

1. Calculate the largest, smallest, and average (mean) population for the states.

2. Calculate the variance in electricity prices among the states.

3. Use linear regression to fit the following simple model
Population = Area * <alpha> + <beta>
That is, find <alpha> and <beta> that minimize the squared residuals when the state data is represented using this model

4. Which of the following linear models is a better fit for the electricity data
Electricity Price = Area * <alpha> + <beta>
Or
Electricity Price = Population * <alpha> + <beta>

5. Obtain a random sample of approximately 100 colleges, in which each college is equally likely to appear in the sample.

6. Obtain a random sample of approximately 100 colleges, in which:
Each public college is equally likely to be sampled and each private college is equally likely to be sampled.
The sample is weighted so that in expectation there are the same number of public and private colleges in the sample
