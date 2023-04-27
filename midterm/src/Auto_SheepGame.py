#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import pyautogui, time

pyautogui.FAILSAFE = True #改數字編號 將易搞錯的分開
iconDICT = { 'gear': 0, 'book': 0, 'computer': 0, 'rainbow': 0, 'tiger': 0,   'palette': 0} #'chicken': 0, 'panda': 0, 'clover' : 0, 'sheep': 0}
slotDICT = { 'gear': 0, 'book': 0, 'computer': 0, 'rainbow': 0, 'tiger': 0,   'palette': 0} #'chicken': 0, 'panda': 0, 'clover' : 0, 'sheep': 0}

time.sleep(3)

while True:
    for key in iconDICT.keys():
        print("now looking for {}".format(key))
        locOBJ = pyautogui.locateAllOnScreen('../media/{}.png'.format(key), confidence=0.9475, grayscale=False, region=(580,200,770,710))
        if locOBJ != None:
            iconDICT[key] = len(list(locOBJ))
            print(list(locOBJ))
            print('key : {}, items : {}'.format(key, len(list(locOBJ))))
            time.sleep(0.2)
        else:
            time.sleep(0.2)
            continue
    print(iconDICT)
    target = max(iconDICT, key=iconDICT.get)
    for key in iconDICT.keys():
        iconDICT[key] = 0
    time.sleep(0.2)    
    print('now clicking :  {}'.format(target))
    targetLIST =  list(pyautogui.locateAllOnScreen('../media/{}.png'.format(target), confidence=0.9475, grayscale=False, region=(580,200,770,710)))
    print(targetLIST)
    for loc_i in targetLIST:
        center = pyautogui.center(loc_i)
        time.sleep(0.2)
        pyautogui.click(center)
        time.sleep(0.5)
    pyautogui.scroll(clicks=-90)
    time.sleep(0.2)
    for key in slotDICT.keys():
        print("checking slot {}".format(key))
        slotOBJ = pyautogui.locateAllOnScreen('../media/{}.png'.format(key), confidence=0.94, grayscale=False, region=(600,810,680,210))
        if slotOBJ != None:
            slotDICT[key] = len(list(slotOBJ))
            print(list(slotOBJ))
            print('key : {}, items : {}'.format(key, len(list(slotOBJ))))
            time.sleep(0.2)
        else:            
            time.sleep(0.2)
            continue
    print(slotDICT)
    pyautogui.scroll(clicks=110)
    time.sleep(0.2)    
    if all(value <= 1 for value in slotDICT.values()) == False:
        target = max(slotDICT, key=slotDICT.get)
        print('slot most : {}'.format(target))
        print('now clicking :  {}'.format(target))
        loc_i = pyautogui.locateOnScreen('../media/{}.png'.format(target), confidence=0.9475, grayscale=False, region=(580,200,770,710))
        if loc_i != None:
            print(loc_i)
            center = pyautogui.center(loc_i)
            time.sleep(0.5)
            pyautogui.click(center)
            for key in slotDICT.keys():
                slotDICT[key] = 0
        else:
            for key in slotDICT.keys():
                slotDICT[key] = 0            
            time.sleep(0.2)
            continue
    else:
        for key in slotDICT.keys():
                slotDICT[key] = 0
        time.sleep(0.2)
        continue
        
    