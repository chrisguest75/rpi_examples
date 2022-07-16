# README

Demonstrate how to get a webcam working.  

## Install

Use pygame to capture from the camera

```sh
export PIPENV_VENV_IN_PROJECT=1
pipenv install

pipenv shell

code .
```

## Cleanup

```sh
# cleanup
pipenv --rm   
```

## fswebcam

```sh
# install 
sudo apt install fswebcam  
#show options
fswebcam --help
# get devices
lsusb
# save from device to disk  
fswebcam --device /dev/video0 ./output.jpg  
```

## Motion

Motion has an admin interface and a page for an image stream  

```sh
# install 
sudo apt install motion      
# set to yes
sudo nano /etc/default/motion   
# turn off the localhost setings
sudo nano /etc/motion/motion.conf  

sudo service motion start

# ufw to allow http://192.168.1.110:8081 or http://192.168.1.110:8080
sudo ufw disable
sudo ufw status

# get the ip address
hostname -I 

sudo service motion stop  
```

## v4l2 - video fr linux

```sh
sudo apt install v4l-utils   

# list devices and details about device
v4l2-ctl --list-devices
sudo v4l2-ctl --device=/dev/video0 --all

# save an image
v4l2-ctl --device /dev/video2 --set-fmt-video=width=352,height=288,pixelformat=MJPG --stream-mmap --stream-to=./output.jpg --stream-count=1

# save a video
v4l2-ctl --device /dev/video2 --set-fmt-video=width=352,height=288,pixelformat=MJPG --stream-mmap --stream-to=./output.mjpg --stream-count=120

# convert mjpg to something that will work in vlc
ffmpeg -i ./output.mjpg -vcodec copy muxed.mkv
```

## Resources

* Basic Setup Motion [here](https://motion-project.github.io/motion_config.html)
* How To Set Up a Firewall with UFW on Ubuntu 18.04 [here](https://www.digitalocean.com/community/tutorials/how-to-set-up-a-firewall-with-ufw-on-ubuntu-18-04)
* An application to control video4linux drivers [here](https://www.mankier.com/1/v4l2-ctl)
* How to check available webcams from the command line? [here](https://askubuntu.com/questions/348838/how-to-check-available-webcams-from-the-command-line)
* Saving video as Motion JPEG (MJPEG) file #335 [here](https://github.com/waveform80/picamera/issues/335)  
