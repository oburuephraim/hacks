from datetime import datetime
import time

def print_time_every_five_seconds():
    while True:
        # Get the current time
        current_time = datetime.now().strftime("%H:%M:%S")
        print(f"Current time: {current_time}")
        
        # Wait for 5 seconds before the next print
        time.sleep(5)

if __name__ == "__main__":
    print_time_every_five_seconds()
