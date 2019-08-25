This assignment is all about tricks of training a network faster on cipaf10 data. It is quite easy to reach accuracy with higher no of accuracy but we need to tricks if we want to ensure faster training. We have explored

    the requirement for minute customization
    changes in the floating points the importance of profiling our DNN
    importance of moving to formats like tensorflow
    importance of moving augmentations on GPU etc.

Notebook Sumamry

Have three notebook and two of them have been able to run in V100 and another one in 2810.

    Have taken Michael page notebook and further modified the same network. This is explained "PytorchImplementation94Accuracy144Secs2810Machine.ipynb"
    Have taken wide resnet and finetuned further which is explained in "CutOut_widerresnetV100TensorFlow.ipynb". This is still under finetune and can be further finetuned.
    Have taken basemodel from Rohan and have further modified. This is explained in "Cutout8V100TensorFlow.ipynb"
