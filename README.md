Developed the front end for the NeelKavach Kiosk using Kivy library of Python. 

The various steps include: 
* Detection of mask 
* Measuring body temperature 
* Sanitization of hands and lugagge. 

When each of these steps are passed successfully, they are shown in green color, else they are shown in red colour. 

The main challenge faced - 
* For this application, we wanted the webcam to be on during just the detection of mask and the measurement of body temperature. 
  In OpenCV by default, we get a local instance of the camera which will be re instantiated at each screen. 
  To make sure that we have the same camera instance on both the screens, we had to make another global instance of the OpenCV camera. 
  
Snapshots of the how the screen looks like: 

