
## Architectural Basics
For the Neural Network architecture the following points should be considered.I have specified the same in order i.e the one to be considered is specified first:


#### 1.How many layers

We need to first decide on the number of layers based on the no of and type of the images we are processing.We can re-look on the no of layers later if we haven't achieved the required accuracy.


#### 2.Kernels and how do we decide the number of kernels?

After we dcide on the number of layers based on the no of and type of the images we are processing.We can think of kernels to be used in each layer and how many of them.Again based on the accuracy the no of kernels and type of kernels(1 * 1 or 3 *3  should be relooked)

#### 3. 3 * 3 Convolutions

3 * 3  is proven  convolution for image processing and hence its a default convolution to go for.This should be one of the first point to be considered for the Neural Network Architecture


####  4. 1 * 1 Convolutions

1 * 1 convolution would be useful to reduce the number of parameters and can be looked into after model has learned the basic stuff e.g Gradient,textures,colors and edges.1 * 1 convolution helps in reducing the number of parameters and also useful to combine various features e.g edges to make a curve. 



#### 5. Receptive Field,
Once we decide on the number of layers and the convolutions used we would have a fair idea on the receptive field after the last layer convolution.The receptive field(the global receptive field) usually should be same as the size of the image if the object size is equal to image size.In case the object size is less than the image size we should stop at a lesser receptive field which is equal to size of the object

#### 6.Softmax

Whether to use softmax or not should be decided much earlier as in case of a multiclass classification. Softmax is the output probabilities range. The range will 0 to 1, and the sum of all the probabilities will be equal to one. If the softmax function used for multi-classification model it returns the probabilities of each class and the target class will have the high probability.


#### 7.Batch Size, and effects of batch size
The batch size is a very important aspect to be considered before running the model.The batch size cannot be lower than the number of classes in the image dataset.This would make sure model has seen all the classes.

We can decide to increase the batch size to a much larger value(much larger  than the number of classes) but this will make the model execution slow as each open has to go through huge number of images.This would require larger computation as well.

Usually the batch size of 32 or 64 is considered to be ideal. 


#### 8. Number of Epochs and when to increase them,

With the above minimum information ie No of Layers,Kernels used,Receptive Field ,Softmax we can build up a plain vanilla model.
At this point we can decide  the number of epochs to be run.If the model shows some increasing trend in validation accuracy we can decide to  increasing the number of epochs.



#### 9.How do we know our network is not going well, comparatively, very early
When there is very less or  no increase in the training accuracy running few epochs.We can decide not to continue with the epochs and re-architect the model 

#### 10.When to add validation checks

It's good to have the validation checks in place before fine tuning the model.Validation checks saves the best model when we run the model for multiple epochs.We can decide to have the validation checks in place before attempting any optimization techniques for the model.


#### 11.MaxPooling

Max pooling is one of the useful technique to reduce the number of layers and hence the computation.It reduces the output size of the layer to half hence helps in reducing the number of layers.The initial decision on the **Number of Layers**can be relooked once we have max pooling in place.


#### 12. Position of MaxPooling

The position of MaxPooling is important.The max pooling should usually be applied after the model has learned some of the basic features i.e edges,gradients,textures etc.Applying maxpooling in the first or second layer would lead to loss of information of the image.Hence should be applied after 3rd or 4th Layer where model would have already learned about most of the features(textures,gradients,edges)


#### 13.The distance of MaxPooling from Prediction

The distance of Maxpooling from prediction should be far e.g 2,3,4 layers before prediction.Having max pooling very near to the prediction where the object has already been detected would lead to wrong prediction.


#### 14.We stop convolutions and go ahead with a larger kernel or some other alternative (which we have not yet covered)

This is one more finetuning aspect to be considered .For a bigger images say 400 * 400 we can stop at a larger kernel of 11 * 11 as it would give a better accuracy if we convolve through a larger kernel  (again this is based on the computational limit as larger kernel will have more number of parameters).For a smaller images we can stop  beyond  11 * 11  e.g to either 3 * 3, 5 *5 or 7 * 7

#### 15.Image Normalization,
Some images are hazy,some are bright,some are sharp.In order for the same kernel to work for all kind if images its a usual practice to  do image normalization for all the images so that the same kernel can convolve over all the images and gives better accuracy as the kernel would be working on a homogenous data.

#### 16.Batch Normalization

The Batch Normalization concept is similiar to image normalization except for the images it would be applied to intermediate output channels as the analogy of image also applies to channels i.e some channels output will have higher impact compared to others on the final accuracy 


#### 17.The distance of Batch Normalization from Prediction,

The batch normalization shouldn't he applied just before prediction since we wouldn't want to change the output values as we are already close to or already detected the object.


#### 18. DropOut

Drop out needs to be introduced when we see a  large gap between training and test accuracy as dropout reduces gap between training and test accuracy

##### 19. When do we introduce DropOut, or when do we know we have some overfitting

We would introduce dropout when the model is learning something specific feature in  a training data which is not there in a test data hence giving less accuracy on test data.Using dropout we can reduce this effect as model won't be overfitting on this specific feature and hence reducing the gap between test and training accuracy. 


#### 20. Learning Rate

After deciding on the Model architecture,we can play with the learning rate.Learning rate is one of the hyper-parameter to be adjusted.For the initial epochs the learning rate should be high since the model is learning.Once the model has learned most of the features and you don't see any more marginal increase in the test/train accuracy or test/train accuracy is not stable and fluctuating.We should think of reducing the learning rate.

#### 21. LR schedule and concept behind it

LR schedule is a way to manage the learning rate automatically rather than we deciding on when to reduce the learning rate manually.
Its a way to reduce the learning rate periodically.




####  22.Adam vs SGD

This would be last thing to be tried after we have decided on the architecture of the model,batch size and learning rate.
This  may/may not have impact on the performance of the model

#### 23. Concept of Transition Layers,

When we go with the state of art architecture e.g DensNet we can think of Transition layers.
DenseNet will have a predefined blocks (each block having multiple layers) and there would be transition blocks in between each dense block.

#### 24. Position of Transition Layer,

The position of the Transition Layer is usually after each dense block in case of a Denset architecture.
Usually the transition layer should be added in between dense blocks and not after the last dense block or before the first dense block. 






