import sys
import platform
from datetime import datetime


print(f"Python version: {sys.version}")
print(f"Platform: {platform.system()} {platform.release()}")
print(f"Current date and time: {datetime.now()}")
