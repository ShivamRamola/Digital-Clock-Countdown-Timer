import time

def digital_clock():
    """
    Displays a digital clock in HH:MM:SS format.
    Press Ctrl+C to stop the clock.
    """
    print("Digital Clock started! Press Ctrl+C to stop.")
    try:
        while True:
            current_time = time.strftime("%H:%M:%S", time.localtime())
            print("\rDigital Clock: " + current_time, end='')
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nClock stopped!")

def countdown_timer(seconds):
    """
    Counts down from a given number of seconds.
    Example: countdown_timer(5) will count: 5,4,3,2,1,Time's up!
    """
    try:
        # Convert input to integer and check if it's positive
        seconds = int(seconds)
        if seconds <= 0:
            print("Please enter a positive number!")
            return
            
        print("Countdown Timer started!")
        while seconds > 0:
            print(f"\rTime remaining: {seconds} seconds", end='')
            time.sleep(1)
            seconds -= 1
        print("\nTime's up! 🔔")
        
    except ValueError:
        print("Please enter a valid number!")

def main():
    """
    Main program that lets user choose between clock and timer.
    Press Ctrl+C to exit the program.
    """
    print("Welcome to Digital Clock & Countdown Timer!")
    
    while True:
        try:
            print("\nOptions:")
            print("1: Digital Clock")
            print("2: Countdown Timer")
            print("Press Ctrl+C to exit")
            
            choice = input("\nEnter your choice (1 or 2): ")
            
            if choice == "1":
                digital_clock()
            elif choice == "2":
                seconds = input("Enter the number of seconds to countdown: ")
                countdown_timer(seconds)
            else:
                print("Please enter 1 or 2!")
                
        except KeyboardInterrupt:
            print("\n\nGoodbye! Thanks for using the program.")
            break

if __name__ == '__main__':
    main()