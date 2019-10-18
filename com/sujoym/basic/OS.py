import os

CurDir = os.getcwd();
print(CurDir);

os.mkdir('NewOS');

import time
time.sleep(3);
os.rename('NewOS','NewOS2');
time.sleep(3);
os.rmdir('NewOS2');

Test= os.listdir('C:\Movies');
print(Test);

