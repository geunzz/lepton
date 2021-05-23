import sys
import os
import platform
import clr #pip install pythonnet
import time
import numpy as np
import cv2
import colormap_lepton
from scipy.ndimage import rotate

#directory for saving images
img_save_path = 'PATH/TO/IMG/SAVE/'
class_name = 'FACE'

bits, name = platform.architecture()

if bits == "64bit":
    clr.AddReference("/dll/x64/LeptonUVC")
    clr.AddReference("/dll/x64/ManagedIR16Filters")
else:
    clr.AddReference("/dll/x86/LeptonUVC")
    clr.AddReference("/dll/x86/ManagedIR16Filters")

#after dll files load, then import libraries related with lepton
from Lepton import CCI
from IR16Filters import IR16Capture, NewIR16FrameEvent, NewBytesFrameEvent

def getFrameRaw(arr, width, height):
    global numpyArr #numpyArr 변수를 global로 선언해야 에러 발생하지 않음
    numpyArr = np.fromiter(arr, dtype="uint16").reshape(height, width)

def raw_to_8bit(data):
    cv2.normalize(data, data, 0, 65535, cv2.NORM_MINMAX)
    np.right_shift(data, 8, data)
    return cv2.cvtColor(np.uint8(data), cv2.COLOR_GRAY2BGR)

def captureFrame(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        img_path = img_save_path + class_name
        if not os.path.isdir(img_path):
            os.mkdir(img_path)
        _, _, files = next(os.walk(img_path))
        file_count = len(files)
        file_name_01 = img_path + '/' + class_name + '_map_' + str(int(file_count/3)+1) + '.jpg'
        file_name_02 = img_path + '/' + class_name + '_origin_' + str(int(file_count/3)+1) + '.jpg'
        file_name_03 = img_path + '/' + class_name + '_gray_' + str(int(file_count/3)+1) + '.jpg'
        cv2.imwrite(file_name_01, map_lepton)
        cv2.imwrite(file_name_02, image_lepton)
        gray_image = cv2.imread(file_name_01, cv2.IMREAD_GRAYSCALE)
        cv2.imwrite(file_name_03, gray_image)
        print('image saved')
    
numpyArr = None

if CCI.GetDevices() == []:
    print("check the thermal sensor connection.")
    sys.exit()

lep, = (dev.Open()
        for dev in CCI.GetDevices())

#Build an IR16 caputure device
capture = IR16Capture()
capture.SetupGraphWithBytesCallback(NewBytesFrameEvent(getFrameRaw))
capture.RunGraph()

while numpyArr is None:
    time.sleep(1)

color_map = colormap_lepton.generate_color_map()

cv2.namedWindow('lepton')
cv2.setMouseCallback('lepton', captureFrame)

while True:
    image_lepton = cv2.flip(numpyArr, 1)
    image_lepton = raw_to_8bit(image_lepton)
    # image_lepton = cv2.resize(image_lepton, dsize=(320, 240), interpolation=cv2.INTER_LINEAR)
    image_lepton = rotate(image_lepton, 270)
    map_lepton = cv2.LUT(image_lepton, color_map)
    cv2.imshow("lepton", map_lepton)
    
    if cv2.waitKey(10) == '27':
        break

cv2.destroyAllWindows()
