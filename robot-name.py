import random
import string
class Robot(object):
    
    robot_names = set()
    
    def __init__(self):
        self.reset()
        
    def generate_name(self):
        while True:
            new_name = self.random_name()
            if new_name not in self.robot_names:
                return new_name
    
    def random_name(self):
        return (random.choice(string.ascii_uppercase) +
                random.choice(string.ascii_uppercase) +
                str(random.randrange(0,9)) +
                str(random.randrange(0,9))  +
                str(random.randrange(0,9)))
    
    def reset(self):
        self.name = self.generate_name()
        self.robot_names.add(self.name)
