# -*- encoding=utf8 -*-
__author__ = "Noemi"
from airtest.core.api import * 

auto_setup(__file__) 

import time
from poco.drivers.unity3d import UnityPoco 
from poco.drivers.unity3d.device import UnityEditorWindow 

dev=UnityEditorWindow()  
addr = ('', 5001) 
poco = UnityPoco(addr, device=dev) 
#note: use device=UnityEditorWindow() to test in unity  
# dev = connect_device('Android:///<serialno>') to test in Android 

vr = poco.vr 
poco = poco() 
position = poco('Door').attr('position') 
vr.rotateObject(-10, 0, 0, 'XRig', 'Camera Offset', 0.5) 
vr.objectLookAt('Door', 'XRig', 'Camera Offset', 5) 
count = 0 
while(vr.checkIfUnityFinished() == False and count < 10): 
    time.sleep(2) 
    count = count + 1 
poco.click() 
assert poco('Door').attr('position')!= position 