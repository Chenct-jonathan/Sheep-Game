#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import pyautogui, time

pyautogui.FAILSAFE = True #改數字編號 將易搞錯的分開
iconDICT = { 'gear': 0, 'rainbow': 0, 'book': 0 , 'chicken': 0, 'computer': 0, 'tiger': 0,   'palette': 0} # 'panda': 0, 'clover' : 0, 'sheep': 0}
slotDICT = { 'gear': 0, 'rainbow': 0, 'book': 0 , 'chicken': 0, 'computer': 0, 'tiger': 0,   'palette': 0} #'chicken': 0, 'panda': 0, 'clover' : 0, 'sheep': 0}

time.sleep(3)

def navigateIcon(iconDICT):
    for key in iconDICT.keys():
        print('now looking for {}'.format(key))
        locOBJ = pyautogui.locateOnScreen('../media/{}.png'.format(key), confidence=0.9477, grayscale=False, region=(580,200,770,710))
        if locOBJ != None:
            iconDICT[key] = len(list(locOBJ))
            print(list(locOBJ))
            print('key : {}, items : {}'.format(key, len(list(locOBJ))))
            time.sleep(0.1)
        else:
            time.sleep(0.1)
            continue
    print(iconDICT)
    target = max(iconDICT, key=iconDICT.get)
    for key in iconDICT.keys():
        iconDICT[key] = 0    
    time.sleep(0.1)
    return target

def locTarget(target):
    targetLIST =  list(pyautogui.locateAllOnScreen('../media/{}.png'.format(target), confidence=0.9477, grayscale=False, region=(580,200,770,710)))    
    print(targetLIST)
    time.sleep(0.1)
    return targetLIST

def clickIcon(target, targetLIST):
    print('now clicking :  {}'.format(target))
    for loc_i in targetLIST:
        center = pyautogui.center(loc_i)
        time.sleep(0.1)
        pyautogui.click(center)
        time.sleep(0.3)

def navigateSlot(slotDICT):
    pyautogui.scroll(clicks=-90)
    time.sleep(0.2)
    for key in slotDICT.keys():
        print("checking slot {}".format(key))
        slotOBJ = pyautogui.locateAllOnScreen('../media/{}.png'.format(key), confidence=0.94, grayscale=False, region=(600,810,680,210))
        if slotOBJ != None:
            slotDICT[key] = len(list(slotOBJ))
            print(list(slotOBJ))
            print('key : {}, items : {}'.format(key, len(list(slotOBJ))))
            time.sleep(0.1)
        else:            
            time.sleep(0.1)
            continue
    print(slotDICT)
    pyautogui.scroll(clicks=110)
    time.sleep(0.1)
    return slotDICT

def checkSlot(slotDICT):
    if all(value <= 1 for value in slotDICT.values()) == False:
        target = max(slotDICT, key=slotDICT.get)
        for key in slotDICT.keys():
            slotDICT[key] = 0        
        print('slot most : {}'.format(target))
        return target
    else:
        for key in slotDICT.keys():
            slotDICT[key] = 0
        time.sleep(0.1)
        return None

def clickRest(target):
    if target != None:
        print('now clicking :  {}'.format(target))
        loc_i = pyautogui.locateOnScreen('../media/{}.png'.format(target), minSearchTime=0.5, confidence=0.9477, grayscale=False, region=(580,200,770,710))
        if loc_i != None:
            print(loc_i)
            center = pyautogui.center(loc_i)
            time.sleep(0.1)
            pyautogui.click(center)
            #for key in slotDICT.keys():
                #slotDICT[key] = 0
            return 1
        else:
            #for key in slotDICT.keys():
                #slotDICT[key] = 0            
            time.sleep(0.1)
            return 0
    else:
        #for key in slotDICT.keys():
                #slotDICT[key] = 0
        time.sleep(0.1)
        return 0
    
if __name__ == '__main__':
    while True:
        target = navigateIcon(iconDICT)
        targetLIST = locTarget(target)
        clickIcon(target,targetLIST)
        slotDICT = navigateSlot(slotDICT)
        target = checkSlot(slotDICT)
        status = clickRest(target)
        if status == 1:
            print('status : found and restart')
        else:
            print('status : not found')