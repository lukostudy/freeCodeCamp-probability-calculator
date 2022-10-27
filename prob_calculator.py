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
        """
        Draw one ball and remove it from the hat

        Returns
        -------
            str
                Name of the color of the drawn ball
            None
                if the hat is empty - nothing can be drawn
        """
        if self.num_of_balls == 0: return None
        return self.contents.pop(random.randint(0,self.max_ball_index))


    def draw(self, n):
        """
        Draw n balls and remove them from the hat

        Parameters
        ----------
            n : int
                Number of balls to be drawn
        
        Returns
        -------
            list of str
                Drawn balls as a list of color names e.g. ["red", "blue", "blue", "black"]
        """
        num_balls_to_draw = min(n, self.num_of_balls)
        return [self.draw_ball() for i in range(num_balls_to_draw)]



def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    """
    Run probabilistic experiment of drawing n balls from a hat.

    Parameters
    ----------
        hat : <class: Hat>
            an object which imlements a hat with balls
        
        expected_balls: dict
            expected number of particular balls colors
            e.g.: {"red": 1, "blue": 3, "black": 1}
        
        num_balls_drawn : int
            number of balls to be drawn from the hat
        
        num_experiments :  int
            Number of repetitions of the experiment
    
    Returns
    -------
        number
            Probability calcultated as number of successes / number of the repetitions.
            As success is considered every event that meets min expected numbers of balls colors.
    """
    num_successes = 0
    experiment = 1      # number of the experiment starts from 1
    
    while experiment <= num_experiments:
        # experiment repetition starts with a fresh copy of the initial hat
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
        
        # next experiment repetition number
        experiment += 1
    
    return num_successes/num_experiments