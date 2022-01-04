from pymouse import PyMouse
import time
import sys

k = ('leftclick','rightclick','middleclick')
m = PyMouse()
t = int(input('Click how many times?（0=infinite）：'))
if (t < 0):
    print('Invalid input')
    sys.exit()
elif (t == 0):
	print('infinite!')
d = float(input('Interval of each click (s)：'))
p = int(input('click?（1=left，2=right，3=middle）：'))
print('You have 5 seconds to move the cursor!')
for i in range(5):
	print('Coming',5-i,'S')
	time.sleep(1)
print('[I]Start to click.')
s = time.time()
i = 0
while(i < t or t == 0):
	m.click(m.position()[0],m.position()[1],p)
	i=i+1
	time.sleep(d)
e = time.time()
print('Finished! Total time: ',round(e-s,2),'s, click per second:',round(t/(e-s),2),'times。')