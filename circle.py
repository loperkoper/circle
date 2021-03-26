#import os
#os.system('cmd /c "cd Desktop && cd chrome signup && qwiklabs.com - Chrome.lnk"')
import pyautogui
from time import sleep
import webbrowser
from pynput.mouse import Button, Controller
mouse = Controller()
from pynput.keyboard import Key, Controller
keyboard = Controller()
import pyautogui
import pyperclip as pc
from time import sleep
import random
import string
sleep(5)
def install_chrome():
	##open edge browser
	mouse.position = (170, 742)
	mouse.click(Button.left, 1)
	sleep(5)
	##click on search bar
	mouse.position = (290, 72)
	mouse.click(Button.left, 1)
	sleep(0.5)
	##remove text
	keyboard.press(Key.ctrl)
	keyboard.press('a')
	keyboard.release('a')
	keyboard.release(Key.ctrl)
	keyboard.press(Key.backspace)
	keyboard.release(Key.backspace)
	sleep(0.2)
	##go to chrome site
	keyboard.type('https://dl.google.com/tag/s/appguid%3D%7B8A69D345-D564-463C-AFF1-A69D9E530F96%7D%26iid%3D%7B0FBDF0EC-4DF6-4765-5C09-45598F7F4281%7D%26lang%3Den%26browser%3D2%26usagestats%3D1%26appname%3DGoogle%2520Chrome%26needsadmin%3Dprefers%26ap%3Dx64-stable-statsdef_1%26brand%3DRXQR%26installdataindex%3Dempty/update2/installers/ChromeSetup.exe')
	keyboard.press(Key.enter)
	keyboard.release(Key.enter)
	sleep(4)
	##naximize
	pyautogui.keyDown("alt")
	pyautogui.keyDown("space")
	pyautogui.press('x')
	pyautogui.keyUp("alt")
	pyautogui.keyUp("space")
	sleep(2)
	##run installer
	mouse.position = (960, 705)
	mouse.click(Button.left, 1)
	sleep(1)
	##close eadge
	mouse.position = (1347, 7)
	mouse.click(Button.left, 1)
	##sleep 
	sleep(25)
	##maximize
	pyautogui.keyDown("alt")
	pyautogui.keyDown("space")
	pyautogui.press('x')
	pyautogui.keyUp("alt")
	pyautogui.keyUp("space")
	mouse.position = (1085, 242)
	mouse.click(Button.left, 1)
	##select search bar
	keyboard.press(Key.ctrl)
	keyboard.press('l')
	keyboard.release('l')
	keyboard.release(Key.ctrl)
	sleep(0.5)
def download_extention():
	##go to site buster varifier
	keyboard.type('https://chrome.google.com/webstore/detail/buster-captcha-solver-for/mpbjkejclgfgadiemmefgebjfooflfhl?hl=en')
	keyboard.press(Key.enter)
	keyboard.release(Key.enter)
	sleep(7)
	##add to chrome
	mouse.position = (1085, 242)
	mouse.click(Button.left, 1)
	sleep(1)
	mouse.position = (722, 273)
	mouse.click(Button.left, 1)
	mouse.click(Button.left, 1)
	sleep(5)
	##New page
	keyboard.press(Key.ctrl)
	keyboard.press('t')
	keyboard.release('t')
	keyboard.release(Key.ctrl)
	sleep(0.5)
	##go to first page and close it
	keyboard.press(Key.ctrl)
	keyboard.press('1')
	keyboard.release('1')
	keyboard.release(Key.ctrl)
	sleep(0.5)
	keyboard.press(Key.ctrl)
	keyboard.press('w')
	keyboard.release('w')
	keyboard.release(Key.ctrl)
	sleep(0.75)
	##select search bar
	keyboard.press(Key.ctrl)
	keyboard.press('l')
	keyboard.release('l')
	keyboard.release(Key.ctrl)
	sleep(0.5)
def signup():
	##go to site circleci
	keyboard.type('https://circleci.com/vcs-authorize/')
	keyboard.press(Key.enter)
	keyboard.release(Key.enter)
	##New page
	keyboard.press(Key.ctrl)
	keyboard.press('t')
	keyboard.release('t')
	keyboard.release(Key.ctrl)
	sleep(0.5)
	##select search bar
	keyboard.press(Key.ctrl)
	keyboard.press('l')
	keyboard.release('l')
	keyboard.release(Key.ctrl)
	sleep(0.5)
	##Go to bitbucket signup
	keyboard.type('https://id.atlassian.com/signup?application=bitbucket&continue=https%3A//bitbucket.org/account/signin/%3Foptintocst%3D1%26next%3D/%3Faidsignup%3D1')
	keyboard.press(Key.enter)
	keyboard.release(Key.enter)
	##New page
	keyboard.press(Key.ctrl)
	keyboard.press('t')
	keyboard.release('t')
	keyboard.release(Key.ctrl)
	sleep(0.5)
	##select search bar
	keyboard.press(Key.ctrl)
	keyboard.press('l')
	keyboard.release('l')
	keyboard.release(Key.ctrl)
	sleep(0.5)
	##go to emailondeck
	keyboard.type('https://www.emailondeck.com/')
	keyboard.press(Key.enter)
	keyboard.release(Key.enter)
	sleep(4)
	##click in recaptcha
	mouse.position = (387, 699)
	mouse.click(Button.left, 1)
	sleep(2)
	##click on solver
	mouse.position = (532, 704)
	mouse.click(Button.left, 1)
	sleep(7)
	##click on refresh
	mouse.position = (441, 700)
	mouse.click(Button.left, 1)
	sleep(3)
	##click on solver
	mouse.position = (532, 704)
	mouse.click(Button.left, 1)
	sleep(8)
	##click on refresh
	mouse.position = (441, 700)
	mouse.click(Button.left, 1)
	sleep(2)
	##click on solver
	mouse.position = (532, 704)
	mouse.click(Button.left, 1)
	sleep(7)
	##click on login
	mouse.position = (835, 677)
	mouse.click(Button.left, 1)
	sleep(3)
	##copy email
	mouse.position = (790, 181)
	mouse.click(Button.left, 1)
	keyboard.press(Key.ctrl)
	keyboard.press('a')
	keyboard.release('a')
	keyboard.release(Key.ctrl)
	keyboard.press(Key.ctrl)
	keyboard.press('c')
	keyboard.release('c')
	keyboard.release(Key.ctrl)
	##back to bitbucket
	keyboard.press(Key.ctrl)
	keyboard.press('2')
	keyboard.release('2')
	keyboard.release(Key.ctrl)
	sleep(0.5)
	##paste email
	mouse.position = (629, 288)
	mouse.click(Button.left, 1)
	keyboard.press(Key.ctrl)
	keyboard.press('v')
	keyboard.release('v')
	keyboard.release(Key.ctrl)
	##write full name
	keyboard.press(Key.tab)
	keyboard.release(Key.tab)
	keyboard.type('Alex Musk')
	##write pass
	keyboard.press(Key.tab)
	keyboard.release(Key.tab)
	keyboard.type('boboltala1$$')
	##click enter
	keyboard.press(Key.enter)
	keyboard.release(Key.enter)
	sleep(4)
	##click on solver
	mouse.position = (597, 685)
	mouse.click(Button.left, 1)
	sleep(5)
	##make site small 4 times
	keyboard.press(Key.ctrl)
	keyboard.press('-')
	keyboard.release('-')
	keyboard.release(Key.ctrl)
	keyboard.press(Key.ctrl)
	keyboard.press('-')
	keyboard.release('-')
	keyboard.release(Key.ctrl)
	keyboard.press(Key.ctrl)
	keyboard.press('-')
	keyboard.release('-')
	keyboard.release(Key.ctrl)
	keyboard.press(Key.ctrl)
	keyboard.press('-')
	keyboard.release('-')
	keyboard.release(Key.ctrl)
	sleep(2)
	##click on refresh
	mouse.position = (375, 434)
	mouse.click(Button.left, 1)
	sleep(2)
	##resize the page
	keyboard.press(Key.ctrl)
	keyboard.press('=')
	keyboard.release('=')
	keyboard.release(Key.ctrl)
	keyboard.press(Key.ctrl)
	keyboard.press('=')
	keyboard.release('=')
	keyboard.release(Key.ctrl)
	keyboard.press(Key.ctrl)
	keyboard.press('=')
	keyboard.release('=')
	keyboard.release(Key.ctrl)
	keyboard.press(Key.ctrl)
	keyboard.press('=')
	keyboard.release('=')
	keyboard.release(Key.ctrl)
	sleep(2)
	##click on solver
	mouse.position = (1011, 598)
	mouse.click(Button.left, 1)
	sleep(5)
	##make site small 4 times
	keyboard.press(Key.ctrl)
	keyboard.press('-')
	keyboard.release('-')
	keyboard.release(Key.ctrl)
	keyboard.press(Key.ctrl)
	keyboard.press('-')
	keyboard.release('-')
	keyboard.release(Key.ctrl)
	keyboard.press(Key.ctrl)
	keyboard.press('-')
	keyboard.release('-')
	keyboard.release(Key.ctrl)
	keyboard.press(Key.ctrl)
	keyboard.press('-')
	keyboard.release('-')
	keyboard.release(Key.ctrl)
	sleep(2)
	##click on refresh
	mouse.position = (373, 425)
	mouse.click(Button.left, 1)
	sleep(2)
	##resize the page
	keyboard.press(Key.ctrl)
	keyboard.press('=')
	keyboard.release('=')
	keyboard.release(Key.ctrl)
	keyboard.press(Key.ctrl)
	keyboard.press('=')
	keyboard.release('=')
	keyboard.release(Key.ctrl)
	keyboard.press(Key.ctrl)
	keyboard.press('=')
	keyboard.release('=')
	keyboard.release(Key.ctrl)
	keyboard.press(Key.ctrl)
	keyboard.press('=')
	keyboard.release('=')
	keyboard.release(Key.ctrl)
	sleep(2)
	##click on solver
	mouse.position = (1011, 598)
	mouse.click(Button.left, 1)
	sleep(3)
	##go to email page
	keyboard.press(Key.ctrl)
	keyboard.press('3')
	keyboard.release('3')
	keyboard.release(Key.ctrl)
	sleep(5)
	##refresh inbox
	mouse.position = (956, 188)
	mouse.click(Button.left, 1)
	mouse.position = (374, 308)
	mouse.click(Button.left, 1)
	sleep(3)
	##click on email from bitbucket
	mouse.position = (450, 408)
	mouse.click(Button.left, 1)
	sleep(3)
	##scroll down 12 times 
	mouse.position = (1390, 719)
	mouse.click(Button.left, 12)
	sleep(1)
	##scroll down again
	mouse.position = (1179, 509)
	mouse.click(Button.left, 10)
	sleep(2)
	##click on varify
	mouse.position = (559, 234)
	mouse.click(Button.right, 1)
	sleep(0.5)
	mouse.position = (612, 251)
	mouse.click(Button.left, 1)
	keyboard.press(Key.ctrl)
	keyboard.press('9')
	keyboard.release('9')
	keyboard.release(Key.ctrl)
	sleep(10)
	##write username
	mouse.position = (618, 374)
	mouse.click(Button.left, 1)
	####### printing lowercase
	letters = string.ascii_lowercase
	a = ''.join(random.choice(letters) for i in range(8))
	####### printing digits
	letters = string.digits
	b = ''.join(random.choice(letters) for i in range(6)) 
	keyboard.type(a+b)
	##click enter
	keyboard.press(Key.enter)
	keyboard.release(Key.enter)
	sleep(4)
	##click on skip
	mouse.position = (674, 565)
	mouse.click(Button.left, 1)
	sleep(4)
	##creat repositiry
	mouse.position = (711, 269)
	mouse.click(Button.left, 1)
	sleep(4)
	##write new
	mouse.position = (695, 266)
	mouse.click(Button.left, 2)
	sleep(1)
	keyboard.type('test')
	sleep(0.5)
	keyboard.press(Key.tab)
	keyboard.release(Key.tab)
	sleep(0.5)
	keyboard.type('new')
	keyboard.press(Key.enter)
	keyboard.release(Key.enter)
	sleep(2)
	## go to first page
	keyboard.press(Key.ctrl)
	keyboard.press('1')
	keyboard.release('1')
	keyboard.release(Key.ctrl)
	##select bitbucket for loggin
	mouse.position = (997, 383)
	mouse.click(Button.left, 1)
	mouse.click(Button.left, 1)
	sleep(3)
	##click on solver
	mouse.position = (598, 630)
	mouse.click(Button.left, 1)
	sleep(7)
	##click on refresh
	mouse.position = (565, 342)
	mouse.click(Button.left, 1)
	sleep(2)
	##click on solver
	mouse.position = (659, 346)
	mouse.click(Button.left, 1)
	sleep(8)
	##click on refresh
	mouse.position = (565, 342)
	mouse.click(Button.left, 1)
	sleep(2)
	##click on solver
	mouse.position = (659, 346)
	mouse.click(Button.left, 1)
	sleep(7)
	##click on refresh
	mouse.position = (569, 381)
	mouse.click(Button.left, 1)
	sleep(2)
	##click on solver
	mouse.position = (659, 346)
	mouse.click(Button.left, 1)
	sleep(8)
	##click on refresh
	mouse.position = (565, 342)
	mouse.click(Button.left, 1)
	sleep(2)
	##click on solver
	mouse.position = (659, 346)
	mouse.click(Button.left, 1)
	sleep(8)
	##click on access
	mouse.position = (863, 584)
	mouse.click(Button.left, 1)
	sleep(15)
	##check the list
	mouse.position = (484, 347)
	mouse.click(Button.left, 1)
	##scroll down 5 times
	mouse.position = (911, 527)
	mouse.click(Button.left, 5)
	##check box
	mouse.position = (485, 357)
	mouse.click(Button.left, 1)
	##scroll down 5 times
	mouse.position = (911, 527)
	mouse.click(Button.left, 5)
	##check box
	mouse.position = (488, 387)
	mouse.click(Button.left, 1)
	##click on lets go
	mouse.position = (850, 580)
	mouse.click(Button.left, 1)
	sleep(2)
	##select account
	mouse.position = (636, 365)
	mouse.click(Button.left, 1)
	##New page
	keyboard.press(Key.ctrl)
	keyboard.press('t')
	keyboard.release('t')
	keyboard.release(Key.ctrl)
	sleep(0.5)
	##select search bar
	keyboard.press(Key.ctrl)
	keyboard.press('l')
	keyboard.release('l')
	keyboard.release(Key.ctrl)
	sleep(0.5)
	##go to sourcecode page
	keyboard.type('https://raw.githubusercontent.com/loperkoper/rdp/main/rdp')
	keyboard.press(Key.enter)
	keyboard.release(Key.enter)
	sleep(1)
	##select on screen
	mouse.position = (934, 399)
	mouse.click(Button.left, 1)
	sleep(0.5)
	##copy
	keyboard.press(Key.ctrl)
	keyboard.press('a')
	keyboard.release('a')
	keyboard.release(Key.ctrl)
	keyboard.press(Key.ctrl)
	keyboard.press('c')
	keyboard.release('c')
	keyboard.release(Key.ctrl)
	sleep(0.5)
	##back to circle ci
	keyboard.press(Key.ctrl)
	keyboard.press('1')
	keyboard.release('1')
	keyboard.release(Key.ctrl)
	sleep(1)
	##set up project
	mouse.position = (934, 399)
	mouse.click(Button.left, 2)
	sleep(3)
	##close add
	mouse.position = (1223, 549)
	mouse.click(Button.left, 1)
	mouse.position = (1062, 165)
	mouse.click(Button.left, 1)
	sleep(1)
	##click on screen
	mouse.position = (877, 586)
	mouse.click(Button.left, 1)
	##remove
	keyboard.press(Key.ctrl)
	keyboard.press('a')
	keyboard.release('a')
	keyboard.release(Key.ctrl)
	keyboard.press(Key.backspace)
	keyboard.release(Key.backspace)
	sleep(0.2)
	##paste
	keyboard.press(Key.ctrl)
	keyboard.press('v')
	keyboard.release('v')
	keyboard.release(Key.ctrl)
	sleep(0.5)
	##New page
	keyboard.press(Key.ctrl)
	keyboard.press('t')
	keyboard.release('t')
	keyboard.release(Key.ctrl)
	sleep(0.5)
	##select search bar
	keyboard.press(Key.ctrl)
	keyboard.press('l')
	keyboard.release('l')
	keyboard.release(Key.ctrl)
	sleep(0.5)
	##go to ngrock
	keyboard.type('https://dashboard.ngrok.com/signup')
	keyboard.press(Key.enter)
	keyboard.release(Key.enter)
	sleep(2)
	##click on name
	mouse.position = (627, 368)
	mouse.click(Button.left, 1)
	##write name
	keyboard.type('alex')
	##write email
	keyboard.press(Key.tab)
	keyboard.release(Key.tab)
	####### printing lowercase
	letters = string.ascii_lowercase
	a = ''.join(random.choice(letters) for i in range(8))
	####### printing digits
	letters = string.digits
	b = ''.join(random.choice(letters) for i in range(6)) 
	c = '@gmail.com'
	keyboard.type(a+b+c)
	##write pass
	keyboard.press(Key.tab)
	keyboard.release(Key.tab)
	keyboard.type('boboltala1$$')
	##click in recaptcha
	mouse.position = (557, 573)
	mouse.click(Button.left, 1)
	sleep(2)
	##click on solver
	mouse.position = (703, 689)
	mouse.click(Button.left, 1)
	sleep(7)
	##click on refresh
	mouse.position = (610, 693)
	mouse.click(Button.left, 1)
	sleep(2)
	##click on solver
	mouse.position = (702, 695)
	mouse.click(Button.left, 1)
	sleep(8)
	##click on refresh
	mouse.position = (610, 693)
	mouse.click(Button.left, 1)
	sleep(2)
	##click on solver
	mouse.position = (702, 695)
	mouse.click(Button.left, 1)
	sleep(7)
	##click on login
	mouse.position = (679, 648)
	mouse.click(Button.left, 1)
	sleep(3)
	##click on authtoken
	mouse.position = (119, 230)
	mouse.click(Button.left, 1)
	sleep(1)
	##click and copy
	mouse.position = (592, 338)
	mouse.click(Button.left, 1)
	keyboard.press(Key.ctrl)
	keyboard.press('a')
	keyboard.release('a')
	keyboard.release(Key.ctrl)
	keyboard.press(Key.ctrl)
	keyboard.press('c')
	keyboard.release('c')
	keyboard.release(Key.ctrl)
	##back to circle ci
	keyboard.press(Key.ctrl)
	keyboard.press('1')
	keyboard.release('1')
	keyboard.release(Key.ctrl)
	sleep(0.5)
	##paste authtoken
	mouse.position = (657, 693)
	mouse.click(Button.left, 2)
	keyboard.press(Key.backspace)
	keyboard.release(Key.backspace)
	keyboard.press(Key.ctrl)
	keyboard.press('v')
	keyboard.release('v')
	keyboard.release(Key.ctrl)
	##commit and run
	mouse.position = (927, 353)
	mouse.click(Button.left, 1)
	##go to ngrok
	keyboard.press(Key.ctrl)
	keyboard.press('9')
	keyboard.release('9')
	keyboard.release(Key.ctrl)
	sleep(0.5)
	##click on endpoint
	mouse.position = (105, 297)
	mouse.click(Button.left, 1)
	sleep(1)
	##status
	mouse.position = (172, 323)
	mouse.click(Button.left, 1)
	sleep(110)
	##refresh page
	keyboard.press(Key.ctrl)
	keyboard.press('r')
	keyboard.release('r')
	keyboard.release(Key.ctrl)
	sleep(3)
	##copy URL
	mouse.position = (566, 393)
	mouse.click(Button.left, 3)
	keyboard.press(Key.ctrl)
	keyboard.press('c')
	keyboard.release('c')
	keyboard.release(Key.ctrl)
	##clear cookies
	pyautogui.keyDown("ctrl")
	pyautogui.keyDown("shift")
	pyautogui.press('del')
	pyautogui.keyUp("ctrl")
	pyautogui.keyUp("shift")
	sleep(2)
	##click on delet
	mouse.position = (873, 602)
	mouse.click(Button.left, 1)
	sleep(1)
	##close chrome
	mouse.position = (1343, 14)
	mouse.click(Button.left, 1)
def remote_desktop():
		##go to new window on windows
		keyboard.press(Key.cmd)
		keyboard.press(Key.ctrl)
		keyboard.press('d')
		keyboard.release(Key.cmd)
		keyboard.release(Key.ctrl)
		keyboard.release('d')
		sleep(1)
		##click on search bar
		mouse.position = (72, 745)
		mouse.click(Button.left, 1)
		sleep(1)
		##type remote
		keyboard.type('remote')
		sleep(2)
		##click on remote desktop
		mouse.position = (259, 203)
		mouse.click(Button.left, 1)
		sleep(1.5)
		##click on option
		mouse.position = (501, 350)
		mouse.click(Button.left, 1)
		sleep(0.5)
		##click on URL bar
		mouse.position = (659, 311)
		mouse.click(Button.left, 1)
		keyboard.press(Key.ctrl)
		keyboard.press('a')
		keyboard.release('a')
		keyboard.release(Key.ctrl)
		keyboard.press(Key.backspace)
		keyboard.release(Key.backspace)
		sleep(0.2)
		##paste the URL
		keyboard.press(Key.ctrl)
		keyboard.press('v')
		keyboard.release('v')
		keyboard.release(Key.ctrl)
		sleep(0.5)
		##select on type bar
		mouse.position = (803, 312)
		mouse.click(Button.left, 1)
		sleep(0.5)
		##30 times pageleft
		def page_left():
		    i = 0
		    while i<30:	
		        keyboard.press(Key.left) 
		        keyboard.release(Key.left)
		        i = i+1
		page_left()
		sleep(0.5)
		##6 times page right
		def page_right():
		    i = 0
		    while i<6:	
		        keyboard.press(Key.right) 
		        keyboard.release(Key.right)
		        i = i+1
		page_right()
		sleep(0.6)
		##backspace 6 times
		keyboard.press(Key.backspace)
		keyboard.release(Key.backspace)
		keyboard.press(Key.backspace)
		keyboard.release(Key.backspace)
		keyboard.press(Key.backspace)
		keyboard.release(Key.backspace)
		keyboard.press(Key.backspace)
		keyboard.release(Key.backspace)
		keyboard.press(Key.backspace)
		keyboard.release(Key.backspace)
		keyboard.press(Key.backspace)
		keyboard.release(Key.backspace)
		sleep(0.5)
		##select on type bar
		mouse.position = (803, 312)
		mouse.click(Button.left, 1)
		sleep(0.5)
		keyboard.press(Key.backspace)
		keyboard.release(Key.backspace)
		sleep(0.25)
		##click on USER NAME
		mouse.position = (662, 344)
		mouse.click(Button.left, 1)
		sleep(1)
		keyboard.press(Key.ctrl)
		keyboard.press('a')
		keyboard.release('a')
		keyboard.release(Key.ctrl)
		keyboard.press(Key.backspace)
		keyboard.release(Key.backspace)
		sleep(0.2)
		keyboard.type('Administrator')
		##Enter
		keyboard.press(Key.enter)
		keyboard.release(Key.enter)
		##sleep(2)
		sleep(2)
		##type PASS
		keyboard.type('Mvusic@123')
		keyboard.press(Key.enter)
		keyboard.release(Key.enter)
		sleep(2)
		##click on YES
		mouse.position = (742, 529)
		mouse.click(Button.left, 1)
		sleep(20)
		##close pages
		mouse.position = (714, 421)
		mouse.click(Button.left, 1)
		sleep(2)
		mouse.position = (1338, 12)
		mouse.click(Button.left, 1)
		sleep(2)
def open_chrome():
		sleep(3)
		##go to new window on windows
		keyboard.press(Key.cmd)
		keyboard.press(Key.ctrl)
		keyboard.press('d')
		keyboard.release(Key.cmd)
		keyboard.release(Key.ctrl)
		keyboard.release('d')
		sleep(1)
		## open chrome
		#webbrowser.get("C:\Program Files\Google\Chrome\Application\chrome.exe").open_new('https://www.qwiklabs.com/users/sign_up')
		#sleep(2)
		x = 64
		y = 743
		pyautogui.moveTo( x , y , duration = 0.1)
		sleep(0.5)
		pyautogui.click(button = "left", clicks = 1 , interval = 0.1)
		sleep(5)
		pyautogui.typewrite("chrome", interval = 0.02)
		sleep(4)
		x = 379
		y = 212
		pyautogui.moveTo( x , y , duration = 0.1)
		sleep(0.5)
		pyautogui.click(button = "left", clicks = 1 , interval = 0.1)
		sleep(3)
		pyautogui.keyDown("alt")
		pyautogui.keyDown("space")
		pyautogui.press('x')
		pyautogui.keyUp("alt")
		pyautogui.keyUp("space")
		sleep(3)
def circleci():
		sleep(3)
		x = 64
		y = 743
		pyautogui.moveTo( x , y , duration = 0.1)
		sleep(0.5)
		pyautogui.click(button = "left", clicks = 1 , interval = 0.1)
		sleep(5)
		pyautogui.typewrite("cmd", interval = 0.02)
		sleep(4)
		x = 379
		y = 212
		pyautogui.moveTo( x , y , duration = 0.1)
		sleep(0.5)
		pyautogui.click(button = "left", clicks = 1 , interval = 0.1)
		sleep(3)
		command = '''pip install pynput && pip install pyautogui && pip install pyperclip && powershell -c "Invoke-WebRequest -Uri 'https://raw.githubusercontent.com/loperkoper/circle/main/circle.py' -OutFile 'C:/Users/Administrator/Desktop/circleci.py'" && timeout 5 && cd /Users/Administrator/Desktop && python circleci.py'''
		# copying text to clipboard
		pc.copy(command)
		x = 742
		y = 271
		pyautogui.moveTo( x , y , duration = 0.1)
		sleep(0.5)
		pyautogui.click(button = "right", clicks = 1 , interval = 0.1)
		sleep(1)
		keyboard.press(Key.enter)
		keyboard.release(Key.enter)
def qwiklabs():
		sleep(3)
		x = 64
		y = 743
		pyautogui.moveTo( x , y , duration = 0.1)
		sleep(0.5)
		pyautogui.click(button = "left", clicks = 1 , interval = 0.1)
		sleep(5)
		pyautogui.typewrite("cmd", interval = 0.02)
		sleep(4)
		x = 379
		y = 212
		pyautogui.moveTo( x , y , duration = 0.1)
		sleep(0.5)
		pyautogui.click(button = "left", clicks = 1 , interval = 0.1)
		sleep(3)
		command2 = '''pip install pynput && pip install pyautogui && pip install pyperclip && powershell -c "Invoke-WebRequest -Uri 'https://raw.githubusercontent.com/loperkoper/qwk/main/qwk.py' -OutFile 'C:/Users/Administrator/Desktop/qwiklabs.py'" && timeout 5 && cd /Users/Administrator/Desktop && python qwiklabs.py'''
		# copying text to clipboard
		pc.copy(command2)
		x = 742
		y = 271
		pyautogui.moveTo( x , y , duration = 0.1)
		sleep(0.5)
		pyautogui.click(button = "right", clicks = 1 , interval = 0.1)
		sleep(1)
		keyboard.press(Key.enter)
		keyboard.release(Key.enter)
def minimize():
		sleep(3)
		x = 907
		y = 12
		pyautogui.moveTo( x , y , duration = 0.1)
		sleep(0.5)
		pyautogui.click(button = "left", clicks = 1 , interval = 0.1)

install_chrome()
download_extention()
signup()
if len(z) < 35:
	remote_desktop()
	qwiklabs()
	minimize()
i = 1
while True:
	open_chrome()
	signup()
	z = pc.paste()
	if len(z) < 35:
		remote_desktop()
		if i % 5 == 0:
			circleci()
			minimize() 
		else:
			qwiklabs()
			minimize()
		i = i+1
	else:
		i = i
