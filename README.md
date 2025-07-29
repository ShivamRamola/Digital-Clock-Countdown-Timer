# Digital Clock & Countdown Timer

A simple Python program with two features: digital clock display and countdown timer.

## Features

- **Digital Clock**: Shows the current time in HH:MM:SS format
- **Countdown Timer**: Counts down from a specified number of seconds

## How to Run

1. Make sure you have Python installed
2. Open terminal/command prompt
3. Run the program:
   ```
   python main.py
   ```

## Usage

When you run the program, you'll see:

```
Choose an option (1:Digital Clock, 2:Countdown Timer):
```

### Option 1: Digital Clock

```
Choose an option (1:Digital Clock, 2:Countdown Timer): 1
Digital Clock: 14:30:45
```

The clock updates every second. The display stays on the same line.

### Option 2: Countdown Timer

```
Choose an option (1:Digital Clock, 2:Countdown Timer): 2
Enter the number of seconds to countdown: 10
Countdown Timer started!
Time remaining: 10 seconds
```

The timer will count down to zero, then show "Time's up!"

## Requirements

- Python 3.x
- Standard Python libraries: `time`, `sys`

## Notes

- Press Ctrl+C to stop the clock or exit the program
- Enter a valid number for the countdown timer
- Invalid choices will show "Invalid choice!"

---

Created for learning and practicing Python programming
