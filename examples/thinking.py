#Thinking Animation (LED cycling through different colors to simulate "thinking")
import time
from opineo import OPiNeo

def thinking_animation(neo, delay=0.1):
    colors = [
        (255, 255, 0),  # Yellow
        (0, 0, 255),  # Blue
        (0, 255, 0),  # Green
        (255, 0, 0)  # Red
    ]
    for _ in range(5):  # Cycle through the colors 5 times
        for color in colors:
            neo.fill_strip(*color)
            neo.update_strip()
            time.sleep(delay)

# Initialize OPiNeo with 10 LEDs
neo = OPiNeo('/dev/spidev1.1', 10, 800)
thinking_animation(neo)
