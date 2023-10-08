import os
import time
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

main_Direct = "/Users/Reuel/Downloads"
desti_Folder = "/Users/Reuel/Pictures/Saved Pictures - Copy"

with os.scandir(main_Direct) as entries:
    for entry in entries:
        print(entry.name)



# Define the source folder to monitor
source_folder = main_Direct

# Define the destination folder to move files to
destination_folder = desti_Folder

# Create the destination folder if it doesn't exist
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Define the action to take when a change occurs
def on_change(event):
    if event.is_directory:
        return
    if event.event_type in ('created', 'modified'):
        # Get the full source file path
        source_file = os.path.join(source_folder, event.src_path)

        # Construct the destination file path by joining the destination folder
        # with the filename from the source folder
        destination_file = os.path.join(destination_folder, os.path.basename(source_file))

        # Move the file to the destination folder
        shutil.move(source_file, destination_file)

        print(f"Moved: {source_file} to {destination_file}")

# Create a watchdog observer and attach an event handler
event_handler = FileSystemEventHandler()
event_handler.on_any_event = on_change
observer = Observer()
observer.schedule(event_handler, path=source_folder, recursive=True)

# Start the observer
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()

observer.join()