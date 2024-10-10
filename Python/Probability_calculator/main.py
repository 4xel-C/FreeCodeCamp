import copy
import random

class Hat:
    def __init__(self, **args):
        self.args = args
        self.contents = [color for color, number in self.args.items() for _ in range(number)]

#draw "number" balls from the hat
    def draw(self, number):
        drawed_colors = []
        if number > len(self.contents):
            drawed_colors = self.contents[:]
            self.contents = []
        else:
            for i in range(number):
                indice = random.randint(0, len(self.contents)-1)
                drawed_colors.append(self.contents.pop(indice))
        return drawed_colors

#Copy needed because draw change the contents of the class.
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    M = 0
    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        expected_list = [color for color, number in expected_balls.items() for _ in range(number)]
        drawed_list = hat_copy.draw(num_balls_drawn)
        while expected_list:
            if expected_list[0] in drawed_list:
                drawed_list.remove(expected_list[0])
                expected_list.remove(expected_list[0])
            else: 
                break
        if len(expected_list) == 0:
            M += 1
    return M/num_experiments



hat = Hat(black=6, red=4, green=3)

probability = experiment(hat=hat,
                  expected_balls={"red":2,"green":1},
                  num_balls_drawn=5,
                  num_experiments=2000)


print(probability)
