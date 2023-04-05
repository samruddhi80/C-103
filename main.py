import sys
import time
import random
import os
import shutil

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

from_dir = "C:\Users\Admin\Downloads"


# Event Hanlder Class 
class FileEventHandler(FileSystemEventHandler):

    def on_created(self,event):
        print(f"hey, {event.src_path} has been created!")

    def on_modified(self,event):
        print(f"hey, {event.src_path} has modified!")

    def on_moved(self,event):
        print(f"hey, {event.src_path} has been moved!")
    

    def on_deleted(self,event):
        print(f"Oops! Someone deleted {event.src_path}!")
# Initialize Event Handler Class
event_handler = FileSystemEventHandler()
# Initialize Observer
observer = Observer()
# Schesule the  Observer
observer.schedule(event_handler , from_dir, recursive =True)
# Start the  Observer
observer.start()

try:
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print("stopped!")        
    observer.stop()
