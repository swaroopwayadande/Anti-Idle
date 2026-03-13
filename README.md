# Anti-Idle Script

A simple, lightweight Python script designed to prevent your computer from entering idle mode, going to sleep, or locking the screen due to inactivity. It simulates realistic, human-like activity at random intervals using random mouse movements and harmless key presses.

## Features

- **Random Intervals**: Waits for a random duration between 30 and 90 seconds before taking action, making the activity appear natural.
- **Subtle Mouse Movements**: Moves the mouse pointer by a barely noticeable amount (-5 to 5 pixels) over a short duration.
- **Harmless Key Presses**: Has a 30% chance to press a harmless modifier key (`Shift` or `Ctrl`) that won't interfere with your reading or typing.
- **Fail-Safe Mechanism**: Includes PyAutoGUI's built-in fail-safe feature. Slam your mouse pointer to any of the 4 corners of your screen to immediately stop the script.
- **Graceful Exit**: Easily stop the script at any time by pressing `Ctrl+C` in the terminal.

## Prerequisites

- Python 3.x installed on your system.

## Installation

1. **Clone the repository** (or download the script):
   ```bash
   git clone <repository-url>
   cd anti-idle
   ```

2. **Set up a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   
   # On Windows:
   venv\Scripts\activate
   
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install the required dependencies**:
   Install the dependencies listed in the `requirements.txt` file.
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Open your terminal or command prompt.
2. Navigate to the directory containing `anti_idle.py`.
3. (If using a virtual environment, ensure it is activated.)
4. Run the script:
   ```bash
   python anti_idle.py
   ```

The terminal will print updates about its activity, showing the wait times, mouse movements, and key presses.

### Stopping the Script

- **Normal Stop**: Press `Ctrl+C` in the terminal/command prompt window where the script is running.
- **Emergency Stop (Fail-Safe)**: If you lose control or the script behaves unexpectedly, quickly move your mouse cursor to the very top, bottom, left, or right edge (specifically one of the four corners) of your screen. This will trigger a `FailSafeException` and abort the program.

## Disclaimer

This script is intended for personal convenience and legitimate use cases (e.g., preventing screen locks while reading long documents, rendering video, or running long background tasks). Please adhere to your organization's IT policies regarding idle times and screen locking. Do not use this to bypass security measures or create false activity reports.
