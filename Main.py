
import sl4a
import android
import os

droid2 = android.Android()
droid = sl4a.Android()
cmd = 'random string'

def Android_control_welcome():
   title = 'Android control'
   message = 'Welcome to Android control'
   droid.dialogCreateAlert(title, message)
   droid.dialogSetPositiveButtonText('Continue')
   droid.dialogShow()
    
   
Android_control_welcome()

def sms():
   command = 'redifine me please'
   while command != 'end':
      command = input(">>>")
      if command == 'send':
         number = input("Number >>>")
         message = input("Message >>>")
         droid2.smsSend(number,message)
      if command == 'inbox':
        SMSmsgs = droid.smsGetMessages(False, 'inbox')[1]
           for message in SMSmsgs:
           print (msg)

def wifi():
   wifi = input(">>>").lower()
   
   if wifi == 'on' or 'y':
      droid.toggleWifiState(True)
   
   if wifi == 'off' or 'n':
      droid.toggleWifiState(False)
   
   else:
      pass
 #  title = '                       Wifi'
 #  message = '                     On or Off?'
 #  droid.dialogCreateAlert(title, message)
 #  droid.dialogSetPositiveButtonText('on')
 #  droid.dialogSetNegativeButtonText('off')
 #  droid.dialogSetNuteralButtonText('Cancel')
 #  droid.dialogShow()
 #  response = droid.dialogGetResponse().result
 #  if response == positive:
 #     droid.toggleWifiState(True)
 #  else:
 #     droid.toggleWifiState(False)

def wifi_on():
   droid.toggleWifiState(True)
   
def bluetooth_on():
   droid.toggleBluetoothState(True)
 
def bluetooth_off():
   droid.toggleBluetoothState(False) 
 
def wifi_off():
   droid.toggleWifiState(False)

def ringer_volume():
   get_result = droid.getRingerVolume()
   print(get_result)
  
def clipboard():
   previous = droid.getClipboard()
   print("Current Clipboard:", previous)
   yorn = input("Would you like to set a new one?[Y/N]>>>").lower()
  
   if yorn == 'y':
      msg = input(">>>")
      droid.setClipboard(msg)
   else:
      pass
      
def speak():
   word = 'hello'
   while word != 'end':
      word = input(">>>")
      droid.ttsSpeak(word)

def photo():
   photo_path = input("Where do you want to save it to?>>>")
   name = input("What is the name of the photo?(leave blank if it dosent matter)>>>")
   if len(name) < 0:
      name == UnNamed
   droid.cameraInteractiveCapturePicture('/{}'.format(photo_path) + '/{}'.format(name) + '.jpg')

def twitter():
   droid2.startActivity("android.intent.action.MAIN', None, None, None, False,'com.twitter.android','com.twitter.android.StartActivity'")
   	   
def qphoto():
   droid.cameraInteractiveCapturePicture('sdcard/qphoto.jpg')

print("\nThis is a tool to easily control you android device from a terminal\n")

while cmd != 'exit':

    cmd = input("localhost@android/~$ ")
    tools = 'end, photo, twitter, qphoto, vibrate, clipboard, battery, speak, wifi on, wifi off, bluetooth on, bluetooth off, wifi, sms '
    if cmd == 'end':
       exit()
    if cmd == 'photo':
       photo()
    if cmd == 'twitter':
       twitter()
    if cmd == 'qphoto':
       qphoto()
    if cmd == 'vibrate':
       droid.vibrate()
    if cmd == 'clipboard':
       clipboard()
    if cmd == 'battery':
       battery()
    if cmd == 'speak':
       speak()
    if cmd == 'ringer volume':
       ringer_volume()
    if cmd == 'wifi on':
       wifi_on()
    if cmd == 'wifi off':
       wifi_off()
    if cmd == 'bluetooth on':
       bluetooth_on()
    if cmd == 'bluetooth off':
       bluetooth_off()
    if cmd == 'wifi':
       wifi()  
    if cmd == 'sms':
       sms()   
    
    if cmd not in tools:
       os.system(cmd)
