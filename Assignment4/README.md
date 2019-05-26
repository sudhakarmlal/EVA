
## Architectural Basics
This is regarding

We have considered many many points in our last 4 lectures. Some of these we have covered directly and some indirectly. They are:
How many layers,
MaxPooling,
1x1 Convolutions,
3x3 Convolutions,
Receptive Field,
SoftMax,
Learning Rate,
Kernels and how do we decide the number of kernels?
Batch Normalization,
Image Normalization,
Position of MaxPooling,
Concept of Transition Layers,
Position of Transition Layer,
Number of Epochs and when to increase them,
DropOut
When do we introduce DropOut, or when do we know we have some overfitting
The distance of MaxPooling from Prediction,
The distance of Batch Normalization from Prediction,
When do we stop convolutions and go ahead with a larger kernel or some other alternative (which we have not yet covered)
How do we know our network is not going well, comparatively, very early
Batch Size, and effects of batch size
When to add validation checks
LR schedule and concept behind it
Adam vs SGD
etc (you can add more if we missed it here)





#### How many layers

We need to first decide on the number of layers based on the no of and type of the images we are processing.We can re-look on the no of layers later if we haven't achieved the required accuracy.


#### Kernels and how do we decide the number of kernels?

After we dcide on the number of layers based on the no of and type of the images we are processing.We can think of kernels to be used in each layer and how many of them.Again based on the accuracy the no of kernels and type of kernels(1 * 1 or 3 *3  should be relooked)

#### 3 * 3 Convolutions

3 * 3  is proven  convolution for image processing and hence its a default convolution to go for.This should be one of the first point to be considered for the Neural Network Architecture


####  1 * 1 Convolutions

1 * 1 convolution would be useful to reduce the number of parameters and can be looked into after model has learned the basic stuff e.g Gradient,textures,colors and edges.1 * 1 convolution helps in reducing the number of parameters and also useful to combine various features e.g edges to make a curve. 



#### Receptive Field,
Once we decide on the number of layers and the convolutions used we would have a fair idea on the receptive field after the last layer convolution.The receptive field(the global receptive field) usually should be same as the size of the image if the object size is equal to image size.In case the object size is less than the image size we should stop at a lesser receptive field which is equal to size of the object

#### Softmax

Whether to use softmax or not should be decided much earlier as in case of a multiclass classification. Softmax is the output probabilities range. The range will 0 to 1, and the sum of all the probabilities will be equal to one. If the softmax function used for multi-classification model it returns the probabilities of each class and the target class will have the high probability.


#### Number of Epochs and when to increase them,

With the above minimum information ie No of Layers,Kernels used,Receptive Field ,Softmax we can build up a plain vanilla model.
At this point we can decide  the number of epochs to be run.If the model shows some increasing trend in validation accuracy we can decide to  increasing the number of epochs.

#### When to add validation checks

It's good to have the validation checks in place before fine tuning the model.Validation checks saves the best model when we run the model for multiple epochs.We can decide to have the validation checks in place before attempting any optimization techniques for the model.


#### MaxPooling

Max pooling is one of the useful technique to reduce the number of layers and hence the computation.It reduces the output size of the layer to half hence helps in reducing the number of layers.The initial decision on the **Number of Layers**can be relooked once we have max pooling in place.


#### Position of MaxPooling

#### The distance of MaxPooling from Prediction

#### Image Normalization,

#### Batch Normalization

#### The distance of Batch Normalization from Prediction,

#### we stop convolutions and go ahead with a larger kernel or some other alternative (which we have not yet covered)

#### DropOut

##### When do we introduce DropOut, or when do we know we have some overfitting



#### How do we know our network is not going well, comparatively, very early



#### LR schedule and concept behind it

#### Adam vs SGD

#### Concept of Transition Layers,

#### Position of Transition Layer,



#### Learning Rate

#### Batch Size, and effects of batch size
