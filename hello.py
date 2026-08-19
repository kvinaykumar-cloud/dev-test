import platform
import sys

print("Hello from Linux WSL!")
print(f"Python Version: {sys.version.split()[0]}")
print(f"OS Platform: {platform.system()} {platform.release()}")
