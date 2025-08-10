import sys
import os
import time
import keyboard
import pyautogui as ag


os.environ['display'] = ':0'
os.environ['XAUTHORITY']='/run/user/1000/gdm/Xauthority'

def click_max_then_ok():
	for i in range(0,2):
		for i in range(0,4):
			time.sleep(0.02)
			ag.press('tab')
		time.sleep(0.02)
		ag.press('enter')


def click_delete():
	for i in range(0,10):
		time.sleep(0.02)
		ag.press('tab')
	time.sleep(0.02)
	ag.press('enter')


def keyboard_thread():
	print("Here")
	while True:
		time.sleep(0.05)
		if keyboard.is_pressed('q'):
			click_max_then_ok()
		if keyboard.is_pressed('w'):
			click_delete()
		if keyboard.is_pressed('p'):
			break
			
			
ag.FAILSAFE = False				
keyboard_thread()
