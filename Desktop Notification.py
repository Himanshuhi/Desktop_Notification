from datetime import datetime, timedelta
from plyer import notification

title = input("Enter the title of the notification: ")
message = input("Enter the message body of the notification: ")
duration = int(input("Enter the duration of the notification (in seconds): "))


hours = int(input("Enter the hour at which the notification should be displayed (0-23): "))
minutes = int(input("Enter the minute at which the notification should be displayed (0-59): "))
notify_time = datetime.now().replace(hour=hours, minute=minutes)


while datetime.now() < notify_time:
    pass

notification.notify(
    title=title,
    message=message,
    app_name='Python Notification Demo',
    timeout=duration
)

