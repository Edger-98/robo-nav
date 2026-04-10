

import gymnasium as gym
from gymnasium import spaces 
import numpy as np

class RexEnv (gym.Env):

    def __init__(self, grid_size= 10, render_mode= None):

        super().__init__() # call mandatory clasess


        self.grid_size =grid_size
        self.render_mode= render_mode

        self.home = np.array([grid_size//2 , grid_size//2])

        self.action_space = spaces.Discrete(4)

        self.observation_space=  spaces.Box(
            low = 0,
            high = grid_size, 
            shape = (4, ), 
            dtype= np.float32
        )

        self.steps = 0
        self.rex_pos = None 
        self.max_steps = 200

    def reset(self, seed= None , options = None):

        super().reset(seed=seed)

        while True:
            self.rex_pos= self.np_random.integers(0, self.grid_size, size=2)

            if self.rex_pos != self.home:
                break
        
        self.steps= 0
        

    def _get_obs(self):

        return np.array([self.rex_pos[0], 
        self.rex_pos[1],
        self.home[0] - self.rex_pos[0],
         self.home[1] - self.rex_pos[1]
        
        ], dtype=np.float32)





        



        





