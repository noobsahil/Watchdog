import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
 
folder_to_track = "C:/Users/sahil/Downloads"
 
 
class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(f"Hey ,{event.src_path} has been created")
        
 
    def on_modified(self, event):
        print(f"Hey there! ,{event.src_path} has been modified")
    
    def on_deleted(self, event):
        print(f"Oops! Someone Deleted {event.src_path}!")
    
    def on_moved(self, event):
        print(f"Someone moved {event.src_path} to {event.dest_path}")
 
 

event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()


try:
    while True:
        time.sleep(1)
        print("running...")
except KeyboardInterrupt:
    print("stopped!")
    observer.stop()
