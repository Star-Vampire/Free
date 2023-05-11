import os, platform, time, sys

try:
 import requests
except:os.system("pip uninstall requests -y;pip install requests")

print('Checking For Update...')
os.system('git pull --quiet 2>/dev/null')
bit = platform.architecture()[0]
if bit == '64bit':
 import Free
