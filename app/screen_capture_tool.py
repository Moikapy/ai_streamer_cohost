import mss
import mss.tools
from langchain.tools import Tool

def capture_screen(_=None) -> str:  # Accept an optional argument
    with mss.mss() as sct:
        # Capture the primary monitor
        monitor = sct.monitors[1]
        screenshot = sct.grab(monitor)
        
        # Save the screenshot to a file
        filename = "screenshot.png"
        mss.tools.to_png(screenshot.rgb, screenshot.size, output=filename)
        return filename

# Define the screen capture tool
def screen_capture_tool():
    return Tool(
        name="screen_capture",
        func=capture_screen,
        description="Captures the current screen and saves it as an image."
    )
