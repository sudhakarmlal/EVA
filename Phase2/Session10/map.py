# Self Driving Car

# Importing the libraries
import numpy as np
from random import random, randint
import matplotlib.pyplot as plt
import time
import random

# Importing the Kivy packages
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Color, Ellipse, Line
from kivy.config import Config
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.core.image import Image as CoreImage
from PIL import Image as PILImage
from kivy.graphics.texture import Texture

# Importing the Dqn object from our AI in ai.py
from ai import T3DN
from ai import  ReplayBuffer
#from ai import evaluate_policy

# Adding this line if we don't want the right click to put a red point
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
Config.set('graphics', 'resizable', False)
Config.set('graphics', 'width', '1429')
Config.set('graphics', 'height', '660')

# Introducing last_x and last_y, used to keep the last point in memory when we draw the sand on the map
last_x = 0
last_y = 0
n_points = 0
length = 0
random_itr = 0

# Getting our AI, which we call "brain", and that contains our neural network that represents our Q-function
#brain = T3DN(100,1,5)
action2rotation = [0,5,-5]
last_reward = 0
scores = []
im = CoreImage("./images/MASK1.png")

# textureMask = CoreImage(source="./kivytest/simplemask1.png")


#brain = Dqn(5,3,0.9)
policy = T3DN(1600, 1, 1)



replay_buffer = ReplayBuffer()


seed = 0 # Random seed number
start_timesteps = 1e4 # Number of iterations/timesteps before which the model randomly chooses an action, and after which it starts to use the policy network
eval_freq = 5e3 # How often the evaluation step is performed (after how many timesteps)
max_timesteps = 5e5 # Total number of iterations/timesteps
save_models = True # Boolean checker whether or not to save the pre-trained model
expl_noise = 0.1 # Exploration noise - STD value of exploration Gaussian noise
batch_size = 100 # Size of the batch
discount = 0.99 # Discount factor gamma, used in the calculation of the total discounted reward
tau = 0.005 # Target network update rate
policy_noise = 0.2 # STD of Gaussian noise added to the actions for the exploration purposes
noise_clip = 0.5 # Maximum value of the Gaussian noise added to the actions (policy)
policy_freq = 2 # Number of iterations to wait before the policy network (Actor model) is updated



# Initializing the map
first_update = True
def init():
    global sand
    global goal_x
    global goal_y
    global first_update
    sand = np.zeros((longueur,largeur))
    img = PILImage.open("./images/mask.png").convert('L')
    sand = np.asarray(img)/255
    goal_x = 1420
    goal_y = 622
    first_update = False
    random_itr = 0
    global swap
    swap = 0


# Initializing the last distance
last_distance = 0

# Creating the car class

class Car(Widget):
    
    angle = NumericProperty(0)
    rotation = NumericProperty(0)
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)
    #sensor1_x = NumericProperty(0)
    #sensor1_y = NumericProperty(0)
    #sensor1 = ReferenceListProperty(sensor1_x, sensor1_y)
    #sensor2_x = NumericProperty(0)
    #sensor2_y = NumericProperty(0)
    #sensor2 = ReferenceListProperty(sensor2_x, sensor2_y)
    #sensor3_x = NumericProperty(0)
    #sensor3_y = NumericProperty(0)
    #sensor3 = ReferenceListProperty(sensor3_x, sensor3_y)
    #signal1 = NumericProperty(0)
    #signal2 = NumericProperty(0)
    #signal3 = NumericProperty(0)
    #signal = NumericProperty(0)

    def move(self, rotation):
        print("Inside Move......")
        self.pos = Vector(*self.velocity) + self.pos
        print("Rotation is",rotation)
        self.rotation = rotation
        self.angle = self.angle + self.rotation
        #self.sensor1 = Vector(30, 0).rotate(self.angle) + self.pos
        #self.sensor2 = Vector(30, 0).rotate((self.angle+30)%360) + self.pos
        #self.sensor3 = Vector(30, 0).rotate((self.angle-30)%360) + self.pos
        #self.signal = int(np.sum(sand[int(self.sensor1_x)-10:int(self.sensor1_x)+10, int(self.sensor1_y)-10:int(self.sensor1_y)+10]))/400.
        #self.signal2 = int(np.sum(sand[int(self.sensor2_x)-10:int(self.sensor2_x)+10, int(self.sensor2_y)-10:int(self.sensor2_y)+10]))/400.
        #self.signal3 = int(np.sum(sand[int(self.sensor3_x)-10:int(self.sensor3_x)+10, int(self.sensor3_y)-10:int(self.sensor3_y)+10]))/400.
        #if self.sensor1_x>longueur-10 or self.sensor1_x<10 or self.sensor1_y>largeur-10 or self.sensor1_y<10:
            #self.signal1 = 10.
        #if self.sensor2_x>longueur-10 or self.sensor2_x<10 or self.sensor2_y>largeur-10 or self.sensor2_y<10:
            #self.signal2 = 10.
        #if self.sensor3_x>longueur-10 or self.sensor3_x<10 or self.sensor3_y>largeur-10 or self.sensor3_y<10:
            #self.signal3 = 10.
        

#class Ball1(Widget):
    #pass
#class Ball2(Widget):
    #pass
#class Ball3(Widget):
    #pass

# Creating the game class

class Game(Widget):

    car = ObjectProperty(None)
    #ball1 = ObjectProperty(None)
    #ball2 = ObjectProperty(None)
    #ball3 = ObjectProperty(None)

    def serve_car(self):
        self.car.center = self.center
        self.car.velocity = Vector(6, 0)

    def moveandtrain(self, dt):

        #global brain
        global last_reward
        global scores
        global last_distance
        global goal_x
        global goal_y
        global longueur
        global largeur
        global swap
        global random_itr
        

        longueur = self.width
        largeur = self.height
        print("Width",longueur)
        print("Height",largeur)
        
        if first_update:
            init()
        print("Calling Self Update................",random_itr)    
        xx = goal_x - self.car.x
        yy = goal_y - self.car.y
        print("XX",xx)
        print("YY",yy)
        print("Self X" , self.car.x)
        print("Self Y",self.car.y)
        orientation = Vector(*self.car.velocity).angle((xx,yy))/180.
        print("Orientation",orientation)
        #last_signal = [self.car.signal1, self.car.signal2, self.car.signal3, orientation, -orientation]
        #last_signal = [self.car.signal, orientation, -orientation]
        #action = policy.update(last_reward, last_signal)
        #print("LastReward",last_reward)
        #scores.append(brain.score())
        #rotation = action2rotation[action]
        #for i in range(10000):
        rotation=random.randint(-5, 5)
        print("Rotation",rotation)
        #obs = np.array(sand[int(self.car.x)+40:int(self.car.y)+40])
        obs=sand[int(self.car.x)-20:int(self.car.x)+20, int(self.car.y)-20:int(self.car.y)+20]
        #print("Obs shape",obs.shape)
        self.car.move(rotation)
        #new_obs = np.array(sand[int(self.car.x)+40:int(self.car.y)+40])
        new_obs=sand[int(self.car.x)-20:int(self.car.x)+20, int(self.car.y)-20:int(self.car.y)+20]
        distance = np.sqrt((self.car.x - goal_x)**2 + (self.car.y - goal_y)**2)
        #self.ball1.pos = self.car.sensor1
        #self.ball2.pos = self.car.sensor2
        #self.ball3.pos = self.car.sensor3

        if sand[int(self.car.x),int(self.car.y)] > 0:
            self.car.velocity = Vector(0.5, 0).rotate(self.car.angle)
            print(1, goal_x, goal_y, distance, int(self.car.x),int(self.car.y), im.read_pixel(int(self.car.x),int(self.car.y)))
            
            last_reward = -1
        else: # otherwise
            self.car.velocity = Vector(2, 0).rotate(self.car.angle)
            last_reward = -0.2
            print(0, goal_x, goal_y, distance, int(self.car.x),int(self.car.y), im.read_pixel(int(self.car.x),int(self.car.y)))
            if distance < last_distance:
                last_reward = 0.1
            # else:
            #     last_reward = last_reward +(-0.2)

        if self.car.x < 5:
            self.car.x = 5
            last_reward = -1
        if self.car.x > self.width - 5:
            self.car.x = self.width - 5
            last_reward = -1
        if self.car.y < 5:
            self.car.y = 5
            last_reward = -1
        if self.car.y > self.height - 5:
            self.car.y = self.height - 5
            last_reward = -1

        if distance < 25:
            if swap == 1:
                goal_x = 1420
                goal_y = 622
                swap = 0
            else:
                goal_x = 9
                goal_y = 85
                swap = 1
        last_distance = distance
        
        replay_buffer.add((obs, new_obs, rotation, last_reward, 0))
        random_itr = random_itr +1
        if random_itr == 10000:
            policy.train(replay_buffer,1000)
            
# Adding the painting tools

class MyPaintWidget(Widget):

    def on_touch_down(self, touch):
        print("On touch down....")
        global length, n_points, last_x, last_y
        with self.canvas:
            Color(0.8,0.7,0)
            d = 10.
            touch.ud['line'] = Line(points = (touch.x, touch.y), width = 10)
            last_x = int(touch.x)
            last_y = int(touch.y)
            n_points = 0
            length = 0
            sand[int(touch.x),int(touch.y)] = 1
            img = PILImage.fromarray(sand.astype("uint8")*255)
            img.save("./images/sand.jpg")

    def on_touch_move(self, touch):
        print("On touch move....")
        global length, n_points, last_x, last_y
        if touch.button == 'left':
            touch.ud['line'].points += [touch.x, touch.y]
            x = int(touch.x)
            y = int(touch.y)
            length += np.sqrt(max((x - last_x)**2 + (y - last_y)**2, 2))
            n_points += 1.
            density = n_points/(length)
            touch.ud['line'].width = int(20 * density + 1)
            sand[int(touch.x) - 10 : int(touch.x) + 10, int(touch.y) - 10 : int(touch.y) + 10] = 1

            
            last_x = x
            last_y = y

# Adding the API Buttons (clear, save and load)

class CarApp(App):

    def build(self):
        parent = Game()
        parent.serve_car()
        Clock.schedule_interval(parent.moveandtrain, 1.0/60.0)
        self.painter = MyPaintWidget()
        clearbtn = Button(text = 'clear')
        savebtn = Button(text = 'save', pos = (parent.width, 0))
        loadbtn = Button(text = 'load', pos = (2 * parent.width, 0))
        clearbtn.bind(on_release = self.clear_canvas)
        savebtn.bind(on_release = self.save)
        loadbtn.bind(on_release = self.load)
        parent.add_widget(self.painter)
        parent.add_widget(clearbtn)
        parent.add_widget(savebtn)
        parent.add_widget(loadbtn)
        return parent

    def clear_canvas(self, obj):
        global sand
        self.painter.canvas.clear()
        sand = np.zeros((longueur,largeur))

    def save(self, obj):
        print("saving brain...")
        brain.save()
        plt.plot(scores)
        plt.show()

    def load(self, obj):
        print("loading last saved brain...")
        brain.load()

# Running the whole thing
if __name__ == '__main__':
    CarApp().run()
