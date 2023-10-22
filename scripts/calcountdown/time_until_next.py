#!/usr/bin/env python3
import subprocess
from datetime import datetime

def get_next_event_date():
    # Run the AppleScript and get the result
    result = subprocess.check_output(['osascript', 'nextEvent.scpt']).decode('utf-8').strip()

    if "No upcoming events" in result:
        return None
    else:
        # Convert the AppleScript date format to a Python datetime object
        return datetime.strptime(result, '%Y-%m-%d %H:%M:%S')

def time_until_next_event():
    next_event_date = get_next_event_date()

    if next_event_date:
        current_time = datetime.now()
        difference = next_event_date - current_time
        return difference
    else:
        return "No upcoming events"

print(time_until_next_event())

