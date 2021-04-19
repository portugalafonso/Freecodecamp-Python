import random 
import copy

class Hat:
    def __init__(self, **colours):
        #contents - a list of strings containing one item for each ball in the hat
        self.contents = []
        for key in colours:
            for j in range(colours[key]):
                self.contents.append(str(key))
    
    def __str__(self):
        #Test to check if contents is right
        return str(self.contents)

    #method remove balls at random from contentss and return those balls as a list of strings.
    def draw(self, balls_to_draw):
        removed_balls = []
        #If the number of balls to draw exceeds the available quantity, return all the balls.
        if balls_to_draw >= len(self.contents):
            return str(self.contents)
        
        else:
            temp = "" #variable to store the removed ball from contentss and add it to the new list
            for i in range(balls_to_draw):
                temp = random.choice(self.contents)
                self.contents.remove(temp)
                removed_balls.append(temp)
            return removed_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    got_it = 0
    prob = 0


    for i in range(num_experiments):
        copy_hat = copy.deepcopy(hat)

        removed_balls = []
        print(type(removed_balls))
        removed_balls = copy_hat.draw(num_balls_drawn)
        print(type(removed_balls))
        print(removed_balls)
        ###PQ TA TRANSFORMNDO O REMOVEED BALLS EM STRING?????


        removed_balls_dict = {}
        for colour in removed_balls:
            removed_balls_dict[colour] = removed_balls_dict.get(colour, 0) + 1

        check = 0
        for key in expected_balls:
            for key1 in removed_balls_dict:
                if key == key1:
                    if expected_balls[key] <= removed_balls_dict[key1]:
                        check += 1
        if check == len(expected_balls):
            got_it += 1    

    prob = round(got_it/num_experiments, 3)
    return prob
