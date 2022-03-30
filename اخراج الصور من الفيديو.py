import cv2
2
vidcap = cv2.VideoCapture('big_buck_bunny_720p_5mb.mp4')
3
success,image = vidcap.read()
4
count = 0
5
while success:
6
  cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file      
7
  success,image = vidcap.read()
8
  print('Read a new frame: ', success)
9
  count += 1