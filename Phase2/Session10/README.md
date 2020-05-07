# Flow chart Session10-END GAME

Below is the flow chart explaining END GAME.Following are the steps explained in detail.

![](https://github.com/sudhakarmlal/EVA/blob/master/Phase2/Session10/images/FlowChartTD3N.JPG)



**STEP1**

Change the Car.png to  Nav.png in car.kv.The Nav.png to be used during training

The below is the code which should be changed to replace the Car image with the Nav3.png in car.kv

![](https://github.com/sudhakarmlal/EVA/blob/master/Phase2/Session10/images/T3DNStep1.JPG)


The image used for Navigation is as shown below


![](https://github.com/sudhakarmlal/EVA/blob/master/Phase2/Session10/images/StepT3DN1-2.JPG)

Note:The Navigation image to be used for the training would go through the convolution.The convolution would predict the rotation of the car based on the action decided,the car would take the next step







**STEP2**

In the car.kv,the below code has to be removed as we would not be using Sensors any more.


![](https://github.com/sudhakarmlal/EVA/blob/master/Phase2/Session10/images/Step2TD3N.JPG)


In the map.py,all the sensors related code has to be removed from the Car class.Also remove sensor related code in the move function used in the Car class 


![](https://github.com/sudhakarmlal/EVA/blob/master/Phase2/Session10/images/T3Step2-Mod.JPG)



![](https://github.com/sudhakarmlal/EVA/blob/master/Phase2/Session10/images/Step2-Mod2.JPG)


There is ball related information in the Game class as well which has to be removed.

![](https://github.com/sudhakarmlal/EVA/blob/master/Phase2/Session10/images/Step2-4T3DN.JPG)




![](https://github.com/sudhakarmlal/EVA/blob/master/Phase2/Session10/images/Step2-5TD3N.JPG)


**STEP3**

Create an Actor a CNN model that takes the Nav3.png(pixels) as input and outputs the action.Action could be the rotation of the car.
This actor model has to be created in ai.py

![](https://github.com/sudhakarmlal/EVA/blob/master/Phase2/Session10/images/ActionModelTD3N.JPG)

**STEP4**

Create a Critic which takes both action and state as input .
This Critic model has to be created in ai.py

![](https://github.com/sudhakarmlal/EVA/blob/master/Phase2/Session10/images/Step4-TD3N.JPG)


**STEP5**

Create a TD3N Class which has this Actor and Critic Model and the code for Training the Model
The TD3N Class has to be created in ai.py.
It will have following functions:

1.Init:To initialize the Actor and Critic models.

2.Selection action:To select the next action

3.Train:To train the Actor and Critic Models.

4.Load the Model

5.Save the Model


![](https://github.com/sudhakarmlal/EVA/blob/master/Phase2/Session10/images/Step5-TD3N.JPG)




![](https://github.com/sudhakarmlal/EVA/blob/master/Phase2/Session10/images/Step5-3TD3N.JPG)

![](https://github.com/sudhakarmlal/EVA/blob/master/Phase2/Session10/images/STEP5-4TD3N.JPG)





![](https://github.com/sudhakarmlal/EVA/blob/master/Phase2/Session10/images/Step5-5TD3N.JPG)


**STEP6**

Create a policy by invoking this TD3N instead of DQN from  map.py

![](https://github.com/sudhakarmlal/EVA/blob/master/Phase2/Session10/images/Step6-TD3N.JPG)









**STEP7**

While invoking TD3N.Send the state as the state dimension as the Car(Nav.png).
Action Dimensions as 1(ie rotation) and Max_action as 1(it could be 5 degree)
This has to be invoked from map.py

![](https://github.com/sudhakarmlal/EVA/blob/master/Phase2/Session10/images/Step7TD3N.JPG)






**STEP8**

Based on the action  i.e rotation move the car in that in that direction by calling 
self.car.move(rotation)

Below are the changes to the move function in map.py

![](https://github.com/sudhakarmlal/EVA/blob/master/Phase2/Session10/images/Step8-TD3N.JPG)

![](https://github.com/sudhakarmlal/EVA/blob/master/Phase2/Session10/images/Step8-1TD3N.JPG)




**STEP9**

Based on the car moved decide how much the car is on the sand/road.The velocity and reward for the car would set accordingly
Following are the changes for the same in ai.py

![](https://github.com/sudhakarmlal/EVA/blob/master/Phase2/Session10/images/Step9-TD3N.JPG)



![](https://github.com/sudhakarmlal/EVA/blob/master/Phase2/Session10/images/Step9-1TD3N.JPG)

**STEP10**

Store the new_state(after car has moved),done(1 or 0),previous state (before care moved) and the action taken in the replay buffer memory

![](https://github.com/sudhakarmlal/EVA/blob/master/Phase2/Session10/images/Step10-TD3N.JPG)

Repeat the step7-Step10 and  fill up the memory buffer.After 10,000  random steps once the TD3N model is train.Let Model decide which action to be taken

**STEP11**
![](https://github.com/sudhakarmlal/EVA/blob/master/Phase2/Session10/images/Step11-TD3N.JPG)









