#!/usr/bin/python3 
import webbrowser
import time
import subprocess
option='''
Press 1 to start your vlc media player :
Press 2 to play your fav song in youtube :  
Press 3 to search something on google   :  
Press 4 to send whatsapp message to your fav number  :  
Press 5 to check current time and date  :
press 6 to reboot your machine  : 
'''
print(option)

#  taking input from user  
#  1 st
choice=input()
#  input function will take input in str  format 
#   conditional state
if choice == '5':
    #   to connect our BIOS time 
    current_time=time.ctime()
    print(current_time)

elif choice == '1':
    #   to connect os level application we use subprocess 
    subprocess.getoutput('vlc')

elif choice == '3':
    data=input("type your search :--->  ")
    webbrowser.open_new_tab('https://www.google.com/search?q='+data)

elif choice == '2':
    data=input("type your fav song :--->  ")
    webbrowser.open_new_tab('https://www.youtube.com/results?search_query='+data)


elif choice == '4':
    #webbrowser.open_new_tab('https://wa.me/+919511537588')
    webbrowser.open_new_tab('https://api.whatsapp.com/send?phone=919511537588&text=Hello%20there')

elif choice == '6':
    cmdCommand = "shutdown -h now"
    process = subprocess.Popen(cmdCommand.split(), stdout=subprocess.PIPE)

else : 
  print("hiii")

