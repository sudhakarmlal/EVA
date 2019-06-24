Receptive field is calcuated for for the GoogleNet Architecture. Since it is a grouped convolution channels with multiple receptive fields so have shown the calculations for minimum receptive field RF_Min( considering 1 * 1 convolutions in each inception block) and maximum receptive field RF_Max ( considering 5 * 5 convolutions in each inception block)

```
              Operation                             RF_Max               RF_Min                      JumpIN

              Start1                                 1                     1                             1

   (7x7,0,2)  Conv                                   7                     7                             1
   (3x3,0,2)  MaxPool                                11                    11                            2

   	1X1
   		
   (3x3,0,1)   Conv                                  19                    19                            4

 (3x3,0,2)     MaxPool                               27                    27                            4

Incep(3a)
               1X1                                                          27                           8
   		
(3x3,0,1)       1X1 -> Conv                           43                     43                           8	
   	   
(5x5,0,1)       1X1 -> Conv                           59                     59                           8	

(3x3,0,1)       MaxPool -> 1X1                        43                     43                           8

Incep(3b)
                1X1                                                         27                           8
   		
(3x3,0,1)       1X1 -> Conv                          43                      43                           8	
   	
(5x5,0,1)       1X1 -> Conv                          59                      59                           8	

(3x3,0,1)       MaxPool -> 1X1                       43                      43                           8

(3x3,0,2)       MaxPool                              107                     43                           8			

Incep(4a)
     1X1                                                                    43                           16
   		
(3x3,0,1)	1X1 -> Conv			     139	             75			         16	
   	
(5x5,0,1)	1X1 -> Conv			     171		     107			 16	

(3x3,0,1)	MaxPool -> 1X1		             139		     75			         16




Incep(4b)

               1X1                                                           43                         16
   		
(3x3,0,1)	1X1 -> Conv			    139			      75			 16	
   	
(5x5,0,1)	1X1 -> Conv			    171			      107			 16	

(3x3,0,1)	MaxPool -> 1X1		            139			      75			 16	



Incep(4c)

               1X1                                                           43                          16
   		
(3x3,0,1)	1X1 -> Conv			    139			      75			  16
   		
(5x5,0,1)	1X1 -> Conv			    171			      107			  16	

(3x3,0,1)	MaxPool -> 1X1		            139			      75			  16


Incep(4d)

               1X1                                                           43                           16
   		
(3x3,0,1)	1X1 -> Conv			    139			      75			   16		
   
(5x5,0,1)	1X1 -> Conv			    171			      107			   16	

(3x3,0,1)	MaxPool -> 1X1		            139			      75			   16



Incep(4e)

               1X1                                                           43                           16
   		
(3x3,0,1)	1X1 -> Conv			    139			      75			   16
   		
(5x5,0,1)	1X1 -> Conv			    171			      107			   16	

(3x3,0,1)	MaxPool -> 1X1		            139			      75			   16



(3x3,0,2)	MaxPool				    459		              75			   16			



Incep(5a)

               1X1                                                           75                            32
   		
(3x3,0,1)	1X1 -> Conv		           523			      139			    32	
   	
(5x5,0,1)	1X1 -> Conv			   587			      203		            32	

(3x3,0,1)	MaxPool -> 1X1		           523		              139			    32


Incep(5b)

               1X1                                                           75                            32
   		
(3x3,0,1)	1X1 -> Conv			   651			      139			    32	
   	
(5x5,0,1)	1X1 -> Conv			   715			      203			    32	

(3x3,0,1)	MaxPool -> 1X1		           651			      139			    32

(7x7,0,1)	AvgPool				   907			      267			    32	
```