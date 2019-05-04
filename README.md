# Project1

## Question1: Filters and Channels

## Filters
Filters or Kernels in the world of Computer vision  are the feature extractors .We can have multiple features of a image e.g gradient,edge,colour,texture etc.

We can use  kernel for each of the feature e.g: We would use the 1st Kernel for extracting edges,the 2nd one for extracting gradients,the third for extracting texture and so on...

The below example show how different features e.g Identity, EdgeDetection, Sharpen are extracted out of the image.


![](https://ujwlkarn.files.wordpress.com/2016/08/screen-shot-2016-08-05-at-11-03-00-pm.png)



Consider kernel(feature extractor) as detecting edges.The Edge Detector Kernel when traverse over the image  would generate the output something like below.



![](https://www.owlnet.rice.edu/~elec539/Projects97/morphjrks/kfig2.jpg)



We can also think of having separate kernel each for one types of edges e.g Vertical Edge kernel and Horizontal Edge kernel

The way the kernels extract features is by convoluting over the  image.Each time a Kernel convolute over the image it  would generate a feature 

The various Kernel sizes used for image processing considering the CPU/GPU limitations of the convolution operation is 3 * 3  or 1*1.  

## Channel

A Channel is the output generated  out of kernel convolution  over the image.As shown in the figure below each time the kernel slides over the image,  3*3 matrix multiplication happens which generates a single output(which is the summation of all 3 * 3 matrix multiplication).Since there are 9 slides possible for a  3*3 kernel over 5 *5 image a total of  9 outputs would be generated which is nothing but the *Channel*


![](https://cdn-images-1.medium.com/max/1200/1*VVvdh-BUKFh2pwDD0kPeRA@2x.gif)


Kernel extracting edges when convolve over an image would generate a Channel of edges

A gradient Kernel convolution would result in Channel of gradients.

Similarly, a texture Kernel would generate a Channel of textures and so on 

Edge,gradient,texture could be first layer of channels .More complex channels  can be derived out of the first layer of channelds e.g we can combine edges and gradients to get arcs as channelds in the second layer  of CNN and multiple channels of arcs  can be combined to form an *Eye* in the third layer of CNN and so on.. 

The below diagram shows channels at various CNN layers.

![](https://cdn-images-1.medium.com/max/1200/1*OHifHVQLIIumP865ASipXA.png)


## Question2: Why should we only (well mostly) use 3x3 Kernels?

We can use any odd size Kernels for convolution ie 3x3 or 5x5 or 7x7. The kernel doesn't need to be odd though. It's perfectly possible to define an even-sized kernel. When the kernel size is even, it is less obvious which of the pixels should be at the origin, but this is not a problem. You have seen mostly odd-sized filter kernels because they are symmetric around the origin, which is a good property.

We typically go with 3x3 convolution and not other odd sized kernels 5x5 or 7x7 or 11x11.The idea of going with 3 x 3  is its less compute intensive as there are a total of 9 multiplications at a particular point of time  as compared to 25,49,121 multiplications in   5x5 , 7x7 , 11x11 respectively.

The diagram below  shows a 3x3 Convolution over a 5x5 image.Each time a 3x3 Kernel convolves over the image it reduces the size of the image by 2.For example in the case below,when a 3x3  kernel is run over a   5x5 image,the output feature Map generated would be 3x3

![](https://icecreamlabs.com/wp-content/uploads/2018/08/33-con.gif)

Similarly a 7x7 image would be reduced to 5x5,11x11 would be reduced to 9x9.

 ## Below are are examples of performance  gain because of less number of parameters and hence less computations.
 
 
Example1:For a 7x7 image if we have do a convolution with  7x7 filter we would 49 parameters

However if we have to use 3x3 filter for a 7x7 image 3 times we can have the same effect with just 9+9+9 ie 27 parameters.

Example2:For a 9x9 image if we have do a convolution with  9x9 filter we would 81 parameters

However if we have to use 3x3 filter for a 9x9 image 4 times we can have the same effect with just 9+9+9+9 ie 36 parameters

Example2:For a 11x11 image if we have do a convolution with  11x11 filter we would 121 parameters

However if we have to use 3x3 filter for a 11x11 image 5 times we can have the same effect with just 9+9+9+9+9 ie 45 parameters


## Question 3:How many times do we need to perform 3x3 convolution operation to reach 1x1 from 199x199 (show calculations)

When we convolve 199x199 with 3x3  once we reduce each dimension by 2 pixels hence would get 197*197

So,  199x199 to  197x197 (in 1st 3x3 convolution)
197x197 to 195x195 (in the 2nd 3x3 convolution)
195x195 to 193x193 (in the 3rd 3x3 convolution)

Since the reduction of  6 dimensions  i.e from 199 to 193 needs  6/2 i.e 3 iterations.

reduction of 199 to  1 i.e 198 dimensions would require  198/2 i.e 99 iterations.

## Hence we need to perform 99 times 3x3 convolutions to reduce 199x199 to 1x1




