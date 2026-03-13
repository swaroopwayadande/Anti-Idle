import pyautogui
import time
import random

def prevent_idle():
    print("Anti-idle script started. Press Ctrl+C in the terminal to stop.")
    
    try:
        while True:
            # 1. Wait for a random interval between 30 and 90 seconds
            wait_time = random.randint(30, 90)
            print(f"Waiting for {wait_time} seconds...")
            time.sleep(wait_time)
            
            # 2. Simulate small random mouse movement
            # We use small offsets (-5 to 5 pixels) so the movement is barely noticeable
            x_offset = random.randint(-5, 5)
            y_offset = random.randint(-5, 5)
            
            # Move the mouse relative to its current position over 0.5 seconds for a natural feel
            pyautogui.move(x_offset, y_offset, duration=0.5)
            print(f"Moved mouse by ({x_offset}, {y_offset}).")
            
            # 3. Occasional harmless key press
            # 30% chance to press a key so we don't interfere too heavily if you are reading/watching
            if random.random() < 0.3:
                # Pick a harmless key that won't type characters
                key_to_press = random.choice(['shiftleft', 'ctrlleft'])
                pyautogui.press(key_to_press)
                print(f"Pressed the '{key_to_press}' key.")
                
    except KeyboardInterrupt:
        # Graceful exit when the user presses Ctrl+C
        print("\nProcess interrupted by user. Anti-idle script stopped.")

if __name__ == "__main__":
    # Safety feature: If you ever lose control, slamming your mouse pointer
    # to any of the 4 corners of your screen will raise a FailSafeException and stop the script.
    pyautogui.FAILSAFE = True
    
    # Start the idle loop
    prevent_idle()
