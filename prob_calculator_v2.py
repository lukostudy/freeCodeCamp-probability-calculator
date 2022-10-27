"""
This is pre-final version. All tests passed.

The code must be cleaned now:
- remove test printouts
- add some beaty to the style ;-)
"""


import copy
import random
# Consider using the modules imported above.

class Hat:

    def __init__(self, **balls):
        self.contents = []
        for color, qty in balls.items():
            self.contents.extend([color for i in range(0,qty)])
    
    @property
    def num_of_balls(self):
        return len(self.contents)
    
    @property
    def max_ball_index(self):
        return self.num_of_balls - 1


    def draw_ball(self):
        """Draw one ball and remove it from the hat

        Returns
        -------
            name of the color of the drawn ball
        """
        balls_qty = self.num_of_balls
        if balls_qty == 0: return None
        # print(f">>> will draw a random number of the balls from the range: 0 ... {self.max_ball_index}")
        ball_num = random.randint(0,self.max_ball_index)
        # print(f">>> {ball_num} out of {balls_qty}")
        ball_color = self.contents.pop(ball_num)
        # print(f">>> color: {ball_color}")
        return ball_color


    def draw(self, n):
        """Draw n balls from the hat and remove them from the hat

        Parameters       ----------
            n : int
                number of balls to be drawn
        
        Return
        ------
            list of str
                Drawn balls as a list of color names e.g. ["red","blue","blue", "black"]
        """
        num_balls_to_draw = min(n,self.num_of_balls)
        return [self.draw_ball() for i in range(num_balls_to_draw)]

    

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    
    num_successes = 0
    experiment = 1      # number of the experiment starts from 1
    while experiment <= num_experiments:
        print(">>> " + 20 * "-")
        print(f">>> EXPERIMENT number {experiment}")
        # experiment starts here with a fresh copy of the initial hat
        experiment_hat = copy.deepcopy(hat)
        experiment_result = {}
        # draw random balls from the hat
                
        drawn_balls = experiment_hat.draw(num_balls_drawn)
        for drawn_ball in drawn_balls:
            experiment_result[drawn_ball] = experiment_result.get(drawn_ball, 0) + 1
        
        # check the result ... assume result success and verify the assumption
        success = True
        for color, expected_num in expected_balls.items():
            success = experiment_result.get(color,0) >= expected_num and success
        num_successes += int(success)

        print(f">>> experiment expected: {expected_balls}")
        print(f">>> experiment result  : {experiment_result}")
        print(f">>> experint success: {success}")
        print()
        
        # next experiment number
        experiment += 1
    
    # print(f">>> num of successes: {num_successes} in {num_experiments} trials")
    # print(f"probability: {num_successes/num_experiments}")

    return num_successes/num_experiments








if __name__ == "__main__":

    hat = Hat(blue=3,red=2,green=6)
    probability = experiment(hat=hat, expected_balls={"blue":2,"green":1}, num_balls_drawn=4, num_experiments=2000)
    actual = probability
    expected = 0.272
    print(f"RESULT: expected {expected} ... actual: {actual}")
    
    # hat = Hat(yellow=5,red=1,green=3,blue=9,test=1)
    # probability = experiment(hat=hat, expected_balls={"yellow":2,"blue":3,"test":1}, num_balls_drawn=20, num_experiments=3)
    # actual = probability
    # expected = 1.0
    # print(f"RESULT: expected {expected} ... actual: {actual}")