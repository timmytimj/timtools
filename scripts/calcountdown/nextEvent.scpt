tell application "Calendar"
    set currentDate to current date
    set nextEvent to first event of (every calendar) whose start date > currentDate
    if nextEvent exists then
        return start date of nextEvent
    else
        return "No upcoming events"
    end if
end tell

