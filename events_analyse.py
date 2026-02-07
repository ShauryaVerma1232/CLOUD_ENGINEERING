# first we have to read the vents stored in events.txt then break them down to analyse repetitions and other operations \
# we will use a dictionary to store the events and their counts
import os

script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, "events.txt.txt")

with open(file_path, "r") as f:
    lines = f.readlines()
THRESHOLD = 3 # we will use this threshold to filter out events that occur less than this number of times
events_counts = {}
for line in lines:
    event = line.strip()
    event_type = event.split(":")[0]
    if event_type in events_counts:
        events_counts[event_type] += 1
    else:
        events_counts[event_type] = 1
print(events_counts)
print("\nAlerts:")
for event_type, count in events_counts.items():
    if count > THRESHOLD:
        print(f"[ALERT] Event '{event_type}' occurred {count} times (threshold: {THRESHOLD})")
        