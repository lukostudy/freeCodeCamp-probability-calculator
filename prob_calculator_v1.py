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
        balls_qty = self.num_of_balls
        ball_num = random.randint(0,self.max_ball_index)
        print(f">>> {ball_num} out of {balls_qty}")
        return self.contents.pop(ball_num)
    

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    
    num_successes = 0
    experiment = 0    
    while experiment <= num_experiments:
        # number of the experiment starts from 1
        experiment += 1
        print(">>> " + 20 * "-")
        print(f">>> EXPERIMENT number {experiment}")
        # experiment starts here with a fresh copy of the initial hat
        experiment_hat = copy.deepcopy(hat)
        experiment_result = {}
        # draw random balls from the hat
        for draw in range(0,num_balls_drawn):
            drawn_ball = experiment_hat.draw_ball()
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
    
    print(f">>> num of successes: {num_successes} in {num_experiments} trials")
    print(f"probability: {num_successes/num_experiments}")

    return num_successes/num_experiments








if __name__ == "__main__":

    hat = Hat(black=6, red=4, green=3)
    probability = experiment(hat=hat,
                  expected_balls={"red":2,"green":1},
                  num_balls_drawn=5,
                  num_experiments=2000)