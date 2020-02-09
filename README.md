## Audio Catcher
Uh, this will play the Unreal Tournament announcer's famous "Headshot" audio clip when your `netcat` listener catches a connection. None of this code is good, but it is necessary. 

All testing done on Kali, with a default `root` user. 

## Installation
`git clone https://github.com/h0mbre/AudioCatcher`

`pip3 install -r requirements.txt`

## Bashrc Alias??
`alias nc="/usr/bin/python3 <path to AudioCatcher.py>"`

## Tips
Might be better to hardcode the filepath for "headshot.wav", right now it's set to `~/AudioCatcher/headshot.wav`
