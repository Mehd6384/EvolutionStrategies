import numpy as np 
import matplotlib.pyplot as plt 
from utils import eval_rastrigin, plot_rastrigin
from tqdm import tqdm 

np.set_printoptions(formatter={'float':'{:0.2f}'.format})


class SimpleES: 

    def __init__(self, pop_size = 50, mean = None,  std = None): 

        self.pop_size = pop_size
        self.mean = mean.reshape(-1)
        self.std = std.reshape(-1)

    def ask(self): 

        self.solutions = np.random.normal(self.mean, self.std, (self.pop_size, self.mean.shape[0]))
        return self.solutions.copy() 

    def tell(self, fitness):
 
        best = np.argmax(fitness.reshape(-1))
        self.mean = self.solutions[best].reshape(-1)




reso =200 
lim = 5.

initial_pos = np.random.uniform(-lim,lim, (2))
solver = SimpleES(pop_size = 20, mean = initial_pos, std = np.ones((2))*0.3)

x = solver.ask()

f, ax = plt.subplots()

its = 200
for it in tqdm(range(its)):

    ax.clear()
    ax.set_xlim(-lim,lim)
    ax.set_ylim(-lim,lim)
    solutions = solver.ask()
    fitness = 1./eval_rastrigin(solutions)
    solver.tell(fitness)


    best = np.argmax(fitness.reshape(-1))
    plot_rastrigin(ax,reso, lim = lim) 

    ax.scatter(solutions[:,0], solutions[:,1], alpha = 0.5)
    ax.scatter(solutions[best,0], solutions[best,1], color = ((0.3,0.8,0)))
    ax.set_title('Epoch: {} Best: {}'.format(it, solutions[best]))
    plt.pause(0.1)



plt.plot()